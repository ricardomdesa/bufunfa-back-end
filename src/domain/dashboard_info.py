from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class DashboardInfo:
    assets: float
    income_perc: float
    income_value: float

    def format_as_dict(self):
        return asdict(self)
