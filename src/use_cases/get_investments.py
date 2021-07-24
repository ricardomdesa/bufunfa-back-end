from repositories.investment_repository import InvestmentRepository
from repositories.stock_repository import StockRepository
from singleton import Singleton


class GetInvestments(metaclass=Singleton):
    def __init__(
        self,
        investment_repo: InvestmentRepository,
        stock_repo: StockRepository,
        get_investment_presenter,
    ):
        self.__investment_repo = investment_repo
        self.__stock_repo = stock_repo
        self.__presenter = get_investment_presenter

    def run(self):
        try:
            investments = self.__investment_repo.get_investments_by_username()
            updated_investments = list(
                map(
                    lambda investment: investment.complement_with_stock_current_price(
                        self.__stock_repo.get_stock_by_code(investment.codigo).current_price
                    ),
                    investments,
                )
            )
            dict_updated_inv = list(map(lambda x: x.format_as_dict(), updated_investments))
            self.__investment_repo.update_all_by_username(dict_updated_inv)
            list_to_presenter = list(map(lambda investment: investment.format_as_dict(), updated_investments))
            return self.__presenter.respond(list_to_presenter)
        except Exception:
            return self.__presenter.respond_with_error()
