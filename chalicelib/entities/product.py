import dataclasses


@dataclasses.dataclass
class Product:
    code: str
    name: str
    value: float
