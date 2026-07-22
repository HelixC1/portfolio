# MESH-DRONE LOC

> Localisation relative multi-drones par UWB + filtre de Kalman étendu (EKF)

[![UWB](https://img.shields.io/badge/UWB-DW1000-blue)]()
[![Accuracy](https://img.shields.io/badge/Accuracy-±15cm%20LOS-green)]()

## Problème

Coordonner plusieurs drones en essaim sans GPS fiable (intérieur, zones urbaines) nécessite une localisation relative précise et robuste aux pertes de mesure.

## Solution

| Module | Rôle |
|--------|------|
| `uwb_driver` | Time-of-flight DW1000 |
| `ekf_fusion` | Fusion TWR + IMU |
| `mesh_comm` | Diffusion positions inter-nœuds |
| `collision_avoid` | Seuils de séparation |

## Métriques

- Précision LOS : **±15 cm**
- Nœuds supportés : **8**
- Latence fusion : **< 20 ms**
- Recovery après perte TWR : **< 1 s**

## Architecture

```
  Drone A ◄──TWR──► Drone B
     │                 │
     └── mesh broadcast ──┘
              │
         EKF (pos + vel)
```

## Structure

```
firmware/
├── App/
│   ├── uwb_driver.c/h
│   ├── ekf_fusion.c/h
│   └── mesh_comm.c/h
simulation/
└── ekf_demo.py
docs/
└── calibration.md
```

## Démo EKF (Python)

```bash
cd simulation
python ekf_demo.py
```

## Stack

`C · STM32 · UWB · EKF · Python · NumPy`

## Auteur

Nicolas Lecomte — ECE Bordeaux
