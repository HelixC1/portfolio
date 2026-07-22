"""Fault injection primitives for HIL testing."""

from dataclasses import dataclass
from enum import Enum, auto


class FaultType(Enum):
    SENSOR_OFFLINE = auto()
    SENSOR_SPIKE = auto()
    BUS_TIMEOUT = auto()
    POWER_BROWNOUT = auto()
    UART_DROP = auto()
    WATCHDOG_RESET = auto()


@dataclass
class FaultEvent:
    fault_type: FaultType
    channel: int = 0
    duration_ms: int = 100


class FaultInjector:
    def __init__(self):
        self.active: list[FaultEvent] = []
        self.history: list[FaultEvent] = []

    def inject(self, event: FaultEvent) -> None:
        self.active.append(event)
        self.history.append(event)

    def clear(self) -> None:
        self.active.clear()

    def is_active(self, fault_type: FaultType, channel: int = -1) -> bool:
        for event in self.active:
            if event.fault_type != fault_type:
                continue
            if channel >= 0 and event.channel != channel:
                continue
            return True
        return False

    def simulate_sensor_value(self, channel: int, nominal: float) -> float | None:
        if self.is_active(FaultType.SENSOR_OFFLINE, channel):
            return None
        if self.is_active(FaultType.SENSOR_SPIKE, channel):
            return nominal * 10.0
        return nominal
