# Nicolas Lecomte — Portfolio Ingénieur

[![ECE Bordeaux](https://img.shields.io/badge/ECE-Bordeaux-blue)](https://www.ece.fr)
[![Embedded Systems](https://img.shields.io/badge/Specialty-Embedded%20Systems-orange)]()
[![Dassault Aviation](https://img.shields.io/badge/Internship-Dassault%20Aviation-0066CC)]()

> **Ingénieur ECE · Majeur Systèmes embarqués**  
> Firmware temps réel · Cybersécurité embarquée · Traitement du signal · Intégration HW/SW

Stage en cours chez **Dassault Aviation (Mérignac)**.  
Recherche **alternance 2 ans** à partir de septembre–octobre 2026.

---

## Contact

| | |
|---|---|
| Email | lecomte.ece@gmail.com |
| Téléphone | 06 28 46 19 96 |
| Localisation | Bordeaux / Paris, France |
| GitHub | [HelixC1](https://github.com/HelixC1) |
| LinkedIn | *(à compléter)* |
| ComeUp | *(à compléter)* |

---

## Stack technique

```
Langages     C · C++ · Python · Bash
Embarqué     STM32 · FreeRTOS · ESP32 · Linux embarqué · Arduino
Bus / IO     I2C · SPI · UART · CAN · ADC/DMA
Outils       Git · CMake · pytest · Docker · GitHub Actions
Domaines     Avionique · IoT · Cybersécurité · Robotique · Fintech
```

---

## Projets

| Projet | Description | Stack | Dossier |
|--------|-------------|-------|---------|
| **AERO-SENTINEL** | Supervision multi-capteurs temps réel | STM32 · FreeRTOS · C | [`projects/aero-sentinel`](projects/aero-sentinel) |
| **CIPHER-NODE** | Passerelle IoT sécurisée + IDS embarqué | Linux · Python · TLS | [`projects/cipher-node`](projects/cipher-node) |
| **FLIGHT-LOGGER EDGE** | Enregistreur vol IMU/GPS | ESP32 · C++ · Python | [`projects/flight-logger-edge`](projects/flight-logger-edge) |
| **QUANT-SHIELD** | Détection anomalies crypto temps réel | Python · asyncio · ML | [`projects/quant-shield`](projects/quant-shield) |
| **MESH-DRONE LOC** | Localisation relative UWB multi-drones | STM32 · UWB · EKF | [`projects/mesh-drone-loc`](projects/mesh-drone-loc) |
| **HIL-FAULT** | Banc HIL injection de fautes + CI | Python · pytest · STM32 | [`projects/hil-fault`](projects/hil-fault) |

---

## Architecture globale

```
┌─────────────────────────────────────────────────────────────────┐
│                     PORTFOLIO — VUE SYSTÈME                      │
├──────────────┬──────────────┬──────────────┬────────────────────┤
│  AERO-SENT   │ FLIGHT-LOG   │ MESH-DRONE   │   Edge Acquisition │
│  STM32 RTOS  │ ESP32 IMU    │ UWB + EKF    │   Capteurs / RF    │
├──────────────┴──────────────┴──────────────┴────────────────────┤
│  CIPHER-NODE (Security Gateway)  │  QUANT-SHIELD (Data/ML)      │
├──────────────────────────────────┴─────────────────────────────┤
│  HIL-FAULT — Test automation · Fault injection · CI/CD           │
└─────────────────────────────────────────────────────────────────┘
```

---

## Métriques clés (synthèse)

| Indicateur | Valeur |
|------------|--------|
| Projets documentés | 6 |
| Langages | C, C++, Python |
| Latence min (AERO-SENTINEL) | < 8 ms |
| Couverture tests (HIL-FAULT) | 32 scénarios automatisés |
| Précision UWB (MESH-DRONE) | ±15 cm LOS |

---

## Structure du dépôt

```
portfolio/
├── README.md                 ← Vous êtes ici
├── LICENSE
├── .gitignore
├── docs/
│   └── CV-portfolio-summary.md
└── projects/
    ├── aero-sentinel/
    ├── cipher-node/
    ├── flight-logger-edge/
    ├── quant-shield/         ← Démo Python exécutable
    ├── mesh-drone-loc/
    └── hil-fault/            ← Tests pytest exécutables
```

---

## Démarrage rapide

### QUANT-SHIELD (démo Python)

```bash
cd projects/quant-shield
pip install -r requirements.txt
python src/demo.py
pytest tests/ -v
```

> Sur Windows, si `pytest` n'est pas reconnu : `python -m pytest tests/ -v`

### HIL-FAULT (tests)

```bash
cd projects/hil-fault
pip install -r requirements.txt
pytest tests/ -v
```

> Sur Windows, si `pytest` n'est pas reconnu : `python -m pytest tests/ -v`

### FLIGHT-LOGGER (analyse logs)

```bash
cd projects/flight-logger-edge/tools
python analyze_log.py sample_flight.csv
```

### CIPHER-NODE (IDS démo)

```bash
cd projects/cipher-node/scripts
python ids_monitor.py --demo
```

### MESH-DRONE LOC (EKF démo)

```bash
cd projects/mesh-drone-loc/simulation
python ekf_demo.py
```

### AERO-SENTINEL (superviseur démo)

```bash
cd projects/aero-sentinel/supervisor
python dashboard.py
```

---

## Parcours

- **2023–2026** — ECE Bordeaux, cursus ingénieur
- **2026** — Obtention 3ᵉ année · Majeur **Systèmes embarqués**
- **2026** — Stage **Dassault Aviation**, Mérignac
- **2026** — Recherche alternance 2 ans (Thales, TDM, secteur ASD)

---

## Licence

Code source : [MIT](LICENSE).  
Documentation et assets : © Nicolas Lecomte.

---

*Portfolio maintenu par Nicolas Lecomte — ECE Bordeaux*
