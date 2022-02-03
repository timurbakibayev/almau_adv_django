from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass
class Car:
    model: str
    speed: int
    color: str
    id: UUID
