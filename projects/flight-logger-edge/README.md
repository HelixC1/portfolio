# FLIGHT-LOGGER EDGE

> Enregistreur de vol embarqué basse consommation — GPS + IMU + flash

[![MCU](https://img.shields.io/badge/MCU-STM32L4-blue)]()
[![Power](https://img.shields.io/badge/Power-%3C%201mA%20sleep-green)]()

## Problème

Logger les données de vol (altitude, vitesse, attitude) sur plusieurs heures sans drain batterie ni perte de données en cas de coupure.

## Solution

| Fonction | Détail |
|----------|--------|
| Acquisition | GPS NMEA + IMU 100 Hz |
| Stockage | Flash ring buffer avec CRC32 |
| Mode veille | < 1 mA entre sessions |
| Export | CSV via script Python |

## Métriques

- Autonomie cible : **8 h+** sur batterie LiPo 1000 mAh
- Fréquence IMU : **100 Hz**
- Perte données (tests) : **0 %** sur 50 000 samples

## Structure

```
firmware/
├── App/
│   ├── gps_parser.c/h
│   ├── imu_driver.c/h
│   └── flash_logger.c/h
tools/
├── analyze_log.py
└── sample_flight.csv
docs/
└── power-budget.md
```

## Analyse d'un vol (démo)

```bash
cd tools
python analyze_log.py sample_flight.csv
```

## Stack

`C · STM32L4 · I2C/SPI · FatFS · Python · pandas`

## Auteur

Nicolas Lecomte — ECE Bordeaux · Pilotage privé
