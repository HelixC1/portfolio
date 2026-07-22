"""Tests for HIL scenario recovery."""

from hil_fault.fault_injector import FaultEvent, FaultType
from hil_fault.hil_runner import HILRunner


def test_scenario_sensor_fault_degraded_ok():
    runner = HILRunner()
    faults = [FaultEvent(FaultType.SENSOR_OFFLINE, channel=0)]
    status = [False, True, True, True, True, True, True, True]
    result = runner.run_scenario("sensor_0_offline", faults, status)
    assert result.passed


def test_scenario_multiple_faults():
    runner = HILRunner()
    faults = [
        FaultEvent(FaultType.SENSOR_OFFLINE, channel=0),
        FaultEvent(FaultType.SENSOR_OFFLINE, channel=1),
        FaultEvent(FaultType.BUS_TIMEOUT, channel=2),
    ]
    status = [False, False, False, True, True, True, True, True]
    result = runner.run_scenario("triple_fault", faults, status)
    assert result.passed


def test_scenario_total_failure():
    runner = HILRunner()
    faults = [FaultEvent(FaultType.POWER_BROWNOUT)]
    status = [False] * 8
    result = runner.run_scenario("brownout", faults, status)
    assert not result.passed
