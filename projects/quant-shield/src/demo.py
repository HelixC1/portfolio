#!/usr/bin/env python3
"""QUANT-SHIELD — Demo asyncio monitoring loop."""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from quant_shield.alert_manager import AlertManager
from quant_shield.portfolio import Portfolio, Position
from quant_shield.price_feed import SimulatedPriceFeed
from quant_shield.risk_engine import RiskEngine


async def main() -> None:
    symbols = ["BTC", "ETH", "SOL"]
    portfolio = Portfolio(
        cash_usd=2000.0,
        positions={
            "BTC": Position("BTC", 0.05, 60_000),
            "ETH": Position("ETH", 1.2, 3_200),
            "SOL": Position("SOL", 20, 140),
        },
    )
    initial = portfolio.total_value({"BTC": 60_000, "ETH": 3_200, "SOL": 140})
    feed = SimulatedPriceFeed(symbols, {"BTC": 60_000, "ETH": 3_200, "SOL": 140})
    engine = RiskEngine(max_drawdown_pct=8.0, stop_loss_pct=4.0)
    alerts = AlertManager()

    print("QUANT-SHIELD — monitoring demo (Ctrl+C pour arrêter)")
    print(f"Valeur initiale: ${initial:,.0f}\n")

    tick = 0
    async for update in feed.stream(interval=0.4):
        prices = update["prices"]
        value = portfolio.total_value(prices)
        weights = {
            s: (portfolio.positions[s].quantity * prices[s]) / value
            for s in symbols
            if s in portfolio.positions
        }
        risk_alerts = engine.evaluate(value, initial, weights, update["changes_pct"])
        if risk_alerts:
            alerts.dispatch(risk_alerts)

        tick += 1
        print(f"t={tick:02d} | Valeur: ${value:,.0f} | P&L: {portfolio.pnl_pct(prices, initial):+.2f}%")
        if tick >= 15:
            break


if __name__ == "__main__":
    asyncio.run(main())
