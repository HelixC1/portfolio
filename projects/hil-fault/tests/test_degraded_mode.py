"""Tests for degraded mode detection."""

from hil_fault.safety_monitor import SafetyMonitor


def test_degraded_when_below_threshold():
    mon = SafetyMonitor(total_channels=8, min_online=4)
    state = mon.evaluate([True, True, True, False, False, False, False, False])
    assert state.degraded is True
    assert state.channels_online == 3


def test_normal_when_enough_channels():
    mon = SafetyMonitor(total_channels=8, min_online=4)
    state = mon.evaluate([True] * 6 + [False] * 2)
    assert state.degraded is False
    assert state.channels_online == 6


def test_critical_all_offline():
    mon = SafetyMonitor()
    state = mon.evaluate([False] * 8)
    assert mon.assert_safe(state) is False
