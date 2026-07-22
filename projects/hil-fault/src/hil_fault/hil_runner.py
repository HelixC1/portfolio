"""HIL test scenario runner."""

from dataclasses import dataclass, field

from hil_fault.fault_injector import FaultEvent, FaultInjector, FaultType
from hil_fault.safety_monitor import SafetyMonitor


@dataclass
class ScenarioResult:
    name: str
    passed: bool
    steps: list[str] = field(default_factory=list)


class HILRunner:
    def __init__(self):
        self.injector = FaultInjector()
        self.monitor = SafetyMonitor()

    def run_scenario(self, name: str, faults: list[FaultEvent], channel_status: list[bool]) -> ScenarioResult:
        self.injector.clear()
        steps: list[str] = []

        for fault in faults:
            self.injector.inject(fault)
            steps.append(f"Inject {fault.fault_type.name} ch={fault.channel}")

        state = self.monitor.evaluate(channel_status)
        steps.append(f"Degraded={state.degraded} online={state.channels_online}")

        passed = self.monitor.assert_safe(state)
        if state.degraded and state.channels_online >= self.monitor.min_online:
            passed = True

        return ScenarioResult(name=name, passed=passed, steps=steps)
