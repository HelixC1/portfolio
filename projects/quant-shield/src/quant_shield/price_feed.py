"""Simulated async price feed."""

import asyncio
import random
from typing import AsyncIterator


class SimulatedPriceFeed:
    def __init__(self, symbols: list[str], base_prices: dict[str, float] | None = None):
        self.symbols = symbols
        self.prices = base_prices or {s: 100.0 for s in symbols}
        self._prev: dict[str, float] = dict(self.prices)

    async def stream(self, interval: float = 0.3) -> AsyncIterator[dict[str, float]]:
        while True:
            changes: dict[str, float] = {}
            for symbol in self.symbols:
                delta = random.uniform(-0.03, 0.03)
                self._prev[symbol] = self.prices[symbol]
                self.prices[symbol] *= 1 + delta
                changes[symbol] = delta * 100
            yield {"prices": dict(self.prices), "changes_pct": changes}
            await asyncio.sleep(interval)

    def change_since_last(self, symbol: str) -> float:
        if self._prev[symbol] == 0:
            return 0.0
        return ((self.prices[symbol] - self._prev[symbol]) / self._prev[symbol]) * 100
