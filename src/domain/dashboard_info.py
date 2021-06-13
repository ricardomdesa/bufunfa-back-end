from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class DashboardInfo:
    assets: float
    income: float

    def format_as_dict(self):
        return asdict(self)
