from functools import reduce

from singleton_decorator import singleton

from domain.dashboard_info import DashboardInfo


@singleton
class GetDashboardInfo:
    def __init__(self,
                 investment_repo,
                 dashboard_info_presenter):
        self.__investment_repo = investment_repo
        self.__presenter = dashboard_info_presenter

    def run(self):
        try:
            investments = self.__investment_repo.get_investments_by_username()
            import pdb; pdb.set_trace()
            assets = self.__calculate_assets(investments)
            income = self.__calculate_income(investments)
            dashboard = DashboardInfo(assets, income)
            return self.__presenter.respond(dashboard.format_as_dict())
        except Exception:
            return self.__presenter.respond_with_error()

    def __calculate_assets(self, investments):
        return reduce(lambda x: sum(x.format_as_dict()['valor_investido_atual']), investments)

    def __calculate_income(self, investments):
        return reduce(lambda x: sum(x.format_as_dict()['rendimento']), investments)
