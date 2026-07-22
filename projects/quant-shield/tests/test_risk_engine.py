"""Tests for risk engine."""

from quant_shield.risk_engine import RiskEngine


def test_drawdown_alert():
    engine = RiskEngine(max_drawdown_pct=5.0)
    engine.peak_value = 10_000
    alerts = engine.evaluate(
        portfolio_value=9_400,
        initial_value=10_000,
        asset_weights={"BTC": 0.5},
        price_changes={"BTC": -1.0},
    )
    assert any(a.rule == "MAX_DRAWDOWN" for a in alerts)


def test_no_alert_on_small_move():
    engine = RiskEngine()
    engine.peak_value = 10_000
    alerts = engine.evaluate(
        portfolio_value=9_900,
        initial_value=10_000,
        asset_weights={"BTC": 0.3},
        price_changes={"BTC": -0.5},
    )
    assert len(alerts) == 0
