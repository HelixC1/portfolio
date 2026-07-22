#!/usr/bin/env python3
"""MESH-DRONE LOC — Simplified 2D EKF demo for relative positioning."""

import math
import random


class SimpleEKF:
    """Constant-velocity EKF in 2D (x, y, vx, vy)."""

    def __init__(self):
        self.state = [0.0, 0.0, 0.0, 0.0]  # x, y, vx, vy
        self.P = [[1.0 if i == j else 0.0 for j in range(4)] for i in range(4)]

    def predict(self, dt: float) -> None:
        x, y, vx, vy = self.state
        self.state = [x + vx * dt, y + vy * dt, vx, vy]

    def update_range(self, anchor: tuple[float, float], measured_m: float) -> None:
        x, y, _, _ = self.state
        ax, ay = anchor
        dx, dy = x - ax, y - ay
        predicted = math.hypot(dx, dy)
        if predicted < 1e-6:
            return
        residual = measured_m - predicted
        gain = 0.15
        self.state[0] += gain * residual * (dx / predicted)
        self.state[1] += gain * residual * (dy / predicted)


def main() -> None:
    ekf = SimpleEKF()
    anchor = (0.0, 0.0)
    true_pos = [2.0, 1.5]

    print("MESH-DRONE LOC — EKF demo (2D TWR fusion)")
    print(f"{'step':>4} | {'true_x':>6} {'true_y':>6} | {'est_x':>6} {'est_y':>6} | err(cm)")
    print("-" * 55)

    for step in range(20):
        dt = 0.1
        true_pos[0] += 0.05
        true_pos[1] += 0.02
        ekf.predict(dt)

        noisy_range = math.hypot(true_pos[0], true_pos[1]) + random.gauss(0, 0.05)
        ekf.update_range(anchor, noisy_range)

        err_cm = math.hypot(ekf.state[0] - true_pos[0], ekf.state[1] - true_pos[1]) * 100
        print(
            f"{step:4d} | {true_pos[0]:6.2f} {true_pos[1]:6.2f} | "
            f"{ekf.state[0]:6.2f} {ekf.state[1]:6.2f} | {err_cm:5.1f}"
        )


if __name__ == "__main__":
    main()
