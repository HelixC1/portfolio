#!/usr/bin/env python3
"""AERO-SENTINEL — Supervision dashboard (simulation mode)."""

import json
import time
import random


def simulate_frame() -> dict:
    return {
        "timestamp": time.time(),
        "channels": [
            {"id": i, "value": round(20 + random.uniform(-2, 2), 2), "status": "OK"}
            for i in range(8)
        ],
        "degraded": False,
    }


def main() -> None:
    print("AERO-SENTINEL Supervisor — demo mode")
    print("-" * 40)
    for _ in range(5):
        frame = simulate_frame()
        print(json.dumps(frame, indent=2))
        time.sleep(0.5)


if __name__ == "__main__":
    main()
