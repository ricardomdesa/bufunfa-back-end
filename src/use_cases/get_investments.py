import logging

from business_exceptions.use_case_exceptions import EmptyDatabaseError
from repositories.investment_repository import InvestmentRepository
from repositories.stock_repository import StockRepository
from singleton import Singleton

LOGGER = logging.getLogger(__name__)


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
            updated_investments = self.__get_updated_current_price(investments)
            dict_updated_inv = [inv.format_as_dict() for inv in updated_investments]
            self.__investment_repo.update_all_by_username(dict_updated_inv)
            return self.__presenter.respond(dict_updated_inv)
        except EmptyDatabaseError as error:
            LOGGER.exception(error)
            return self.__presenter.respond_with_error(f"Erro ao pegar investimentos: {error}")
        except Exception as error:
            LOGGER.error(f"Erro ao pegar investimentos: {error}")
            return self.__presenter.respond_with_error(f"Erro ao pegar investimentos: {error}")

    def __get_updated_current_price(self, investments):
        if investments:
            return list(
                map(
                    lambda investment: investment.complement_with_stock_current_price(
                        self.__stock_repo.get_stock_by_code(investment.codigo).current_price
                    ),
                    investments,
                )
            )
        raise EmptyDatabaseError()
