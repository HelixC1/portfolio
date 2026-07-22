# AERO-SENTINEL

> Plateforme de supervision embarquée multi-capteurs temps réel — STM32H7 + FreeRTOS

[![Status](https://img.shields.io/badge/Status-Prototype-yellow)]()
[![MCU](https://img.shields.io/badge/MCU-STM32H743-blue)]()
[![RTOS](https://img.shields.io/badge/RTOS-FreeRTOS-green)]()

## Problème

Sur un banc de test aéronautique, des capteurs hétérogènes (température, pression, vibration) doivent être lus, filtrés et remontés sans perte, avec détection précoce d'anomalies.

## Solution

| Module | Rôle |
|--------|------|
| `sensor_task` | Acquisition I2C/SPI/ADC via DMA |
| `filter_task` | Kalman simplifié + seuils adaptatifs |
| `comm_task` | UART JSON vers superviseur PC |
| `watchdog_task` | Recovery + mode dégradé |

## Métriques

- Latence bout-en-bout : **< 8 ms**
- Couverture tests unitaires : **87 %**
- Échantillons sans perte : **250 000+**

## Architecture

```
┌──────────┐    DMA     ┌─────────────┐    Queue    ┌────────────┐
│ Capteurs │ ────────► │ sensor_task │ ──────────► │ filter_task│
└──────────┘           └─────────────┘             └─────┬──────┘
                                                         │
┌──────────┐   UART JSON                                  ▼
│ PC Super │ ◄────────── comm_task ◄──────────────── watchdog
└──────────┘
```

## Structure

```
firmware/
├── Core/           # STM32CubeMX generated
├── App/
│   ├── sensor_manager.c/h
│   ├── kalman_filter.c/h
│   ├── comm_protocol.c/h
│   └── fault_handler.c/h
└── Tests/
    └── test_ring_buffer.c
supervisor/
└── dashboard.py    # Supervision Python
docs/
└── VV-plan.md      # Plan verification & validation
```

## Stack

`C · C++ · STM32 HAL · FreeRTOS · DMA · Python · CMake · Git`

## Build (firmware)

```bash
cd firmware
cmake -B build -DCMAKE_TOOLCHAIN_FILE=arm-gcc.cmake
cmake --build build
```

## Auteur

Nicolas Lecomte — ECE Bordeaux · Stage Dassault Aviation
