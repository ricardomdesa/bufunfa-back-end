from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class User:
    username: str
    password: str
    name: str

    def format_as_dict(self):
        return asdict(self)
