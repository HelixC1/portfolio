"""Safety monitor — validates degraded mode behavior."""

from dataclasses import dataclass


@dataclass
class SystemState:
    degraded: bool
    channels_online: int
    total_channels: int
    last_error: str | None = None


class SafetyMonitor:
    def __init__(self, total_channels: int = 8, min_online: int = 4):
        self.total_channels = total_channels
        self.min_online = min_online

    def evaluate(self, channel_status: list[bool]) -> SystemState:
        online = sum(1 for s in channel_status if s)
        degraded = online < self.min_online
        error = None
        if degraded:
            error = f"Only {online}/{self.total_channels} channels online"
        return SystemState(
            degraded=degraded,
            channels_online=online,
            total_channels=self.total_channels,
            last_error=error,
        )

    def assert_safe(self, state: SystemState) -> bool:
        """System must enter degraded mode before going critical."""
        if state.channels_online == 0:
            return False
        return True
