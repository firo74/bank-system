from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Bank:
    name: str
    withdraw_threshold: Decimal