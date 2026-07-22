"""Tests for fault injection."""

from hil_fault.fault_injector import FaultEvent, FaultInjector, FaultType


def test_sensor_offline_returns_none():
    inj = FaultInjector()
    inj.inject(FaultEvent(FaultType.SENSOR_OFFLINE, channel=2))
    assert inj.simulate_sensor_value(2, 25.0) is None


def test_nominal_value_passthrough():
    inj = FaultInjector()
    assert inj.simulate_sensor_value(0, 42.0) == 42.0


def test_sensor_spike():
    inj = FaultInjector()
    inj.inject(FaultEvent(FaultType.SENSOR_SPIKE, channel=1))
    assert inj.simulate_sensor_value(1, 10.0) == 100.0


def test_fault_history():
    inj = FaultInjector()
    inj.inject(FaultEvent(FaultType.BUS_TIMEOUT, channel=0))
    assert len(inj.history) == 1


def test_clear_active_faults():
    inj = FaultInjector()
    inj.inject(FaultEvent(FaultType.UART_DROP))
    inj.clear()
    assert not inj.is_active(FaultType.UART_DROP)
