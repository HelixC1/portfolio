#!/usr/bin/env python3
"""
CIPHER-NODE — Lightweight IDS demo (port scan detection).
Production target: Raspberry Pi CM4 + iptables integration.
"""

import argparse
import time
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Alert:
    source_ip: str
    event: str
    timestamp: float


class PortScanDetector:
    def __init__(self, threshold: int = 5, window_sec: float = 2.0):
        self.threshold = threshold
        self.window_sec = window_sec
        self._hits: dict[str, list[float]] = defaultdict(list)

    def report_probe(self, source_ip: str, port: int) -> Alert | None:
        now = time.time()
        hits = self._hits[source_ip]
        hits.append(now)
        self._hits[source_ip] = [t for t in hits if now - t <= self.window_sec]

        if len(self._hits[source_ip]) >= self.threshold:
            return Alert(source_ip=source_ip, event=f"PORT_SCAN ({port})", timestamp=now)
        return None


def run_demo() -> None:
    detector = PortScanDetector(threshold=5, window_sec=2.0)
    attacker = "192.168.1.99"
    print("CIPHER-NODE IDS — port scan demo")
    for port in range(20, 30):
        alert = detector.report_probe(attacker, port)
        if alert:
            print(f"[ALERT] {alert.source_ip} — {alert.event} @ t={alert.timestamp:.2f}")
            break
        time.sleep(0.1)
    else:
        print("No alert (increase probe rate)")


def main() -> None:
    parser = argparse.ArgumentParser(description="CIPHER-NODE IDS monitor")
    parser.add_argument("--demo", action="store_true", help="Run port scan simulation")
    args = parser.parse_args()
    if args.demo:
        run_demo()
    else:
        print("Use --demo for simulation. Production: integrate with netfilter logs.")


if __name__ == "__main__":
    main()
