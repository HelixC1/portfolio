"""Alert dispatch."""

from quant_shield.risk_engine import RiskAlert


class AlertManager:
    def __init__(self):
        self.history: list[RiskAlert] = []

    def dispatch(self, alerts: list[RiskAlert]) -> None:
        for alert in alerts:
            self.history.append(alert)
            prefix = {"INFO": "[i]", "WARN": "[!]", "CRITICAL": "[!!]"}.get(alert.severity, "[?]")
            print(f"{prefix} {alert.rule}: {alert.message}")
