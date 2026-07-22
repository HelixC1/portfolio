"""Portfolio state and P&L tracking."""

from dataclasses import dataclass, field


@dataclass
class Position:
    symbol: str
    quantity: float
    avg_price: float

    @property
    def value(self) -> float:
        return self.quantity * self.avg_price


@dataclass
class Portfolio:
    cash_usd: float = 10_000.0
    positions: dict[str, Position] = field(default_factory=dict)

    def total_value(self, prices: dict[str, float]) -> float:
        total = self.cash_usd
        for symbol, pos in self.positions.items():
            total += pos.quantity * prices.get(symbol, pos.avg_price)
        return total

    def pnl_pct(self, prices: dict[str, float], initial: float) -> float:
        current = self.total_value(prices)
        return ((current - initial) / initial) * 100.0
