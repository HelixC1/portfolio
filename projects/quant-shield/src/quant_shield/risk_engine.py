"""Risk rules engine."""

from dataclasses import dataclass


@dataclass
class RiskAlert:
    rule: str
    message: str
    severity: str  # INFO | WARN | CRITICAL


class RiskEngine:
    def __init__(
        self,
        max_drawdown_pct: float = 10.0,
        stop_loss_pct: float = 5.0,
        max_single_asset_pct: float = 40.0,
    ):
        self.max_drawdown_pct = max_drawdown_pct
        self.stop_loss_pct = stop_loss_pct
        self.max_single_asset_pct = max_single_asset_pct
        self.peak_value = 0.0

    def evaluate(
        self,
        portfolio_value: float,
        initial_value: float,
        asset_weights: dict[str, float],
        price_changes: dict[str, float],
    ) -> list[RiskAlert]:
        alerts: list[RiskAlert] = []

        if portfolio_value > self.peak_value:
            self.peak_value = portfolio_value

        drawdown = 0.0
        if self.peak_value > 0:
            drawdown = ((self.peak_value - portfolio_value) / self.peak_value) * 100.0

        if drawdown >= self.max_drawdown_pct:
            alerts.append(
                RiskAlert(
                    rule="MAX_DRAWDOWN",
                    message=f"Drawdown {drawdown:.1f}% >= {self.max_drawdown_pct}%",
                    severity="CRITICAL",
                )
            )

        total_pnl = ((portfolio_value - initial_value) / initial_value) * 100.0
        if total_pnl <= -self.stop_loss_pct:
            alerts.append(
                RiskAlert(
                    rule="STOP_LOSS",
                    message=f"P&L global {total_pnl:.1f}%",
                    severity="WARN",
                )
            )

        for symbol, weight in asset_weights.items():
            if weight * 100 > self.max_single_asset_pct:
                alerts.append(
                    RiskAlert(
                        rule="CONCENTRATION",
                        message=f"{symbol} = {weight*100:.0f}% du portefeuille",
                        severity="WARN",
                    )
                )

        for symbol, change in price_changes.items():
            if change <= -self.stop_loss_pct:
                alerts.append(
                    RiskAlert(
                        rule="ASSET_STOP",
                        message=f"{symbol} -{abs(change):.1f}%",
                        severity="WARN",
                    )
                )

        return alerts
