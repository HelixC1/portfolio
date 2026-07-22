# HIL-FAULT

> Banc Hardware-in-the-Loop avec injection de fautes et suite de tests automatisée

[![CI](https://img.shields.io/badge/CI-GitHub%20Actions-blue)]()
[![Tests](https://img.shields.io/badge/Tests-pytest-green)]()

## Problème

Valider le comportement firmware face aux pannes (capteur HS, bus bloqué, reset) sans risquer le matériel réel à chaque itération.

## Solution

| Composant | Rôle |
|-----------|------|
| `FaultInjector` | Simulation pannes capteur / bus / alim |
| `HILRunner` | Orchestration scénarios |
| `SafetyMonitor` | Vérification mode dégradé |
| CI GitHub Actions | 32 scénarios à chaque push |

## Scénarios couverts

- Capteur offline / valeurs aberrantes
- Timeout bus I2C / SPI
- Reset watchdog / brown-out
- Perte communication UART
- Recovery automatique

## Structure

```
src/
├── hil_fault/
│   ├── __init__.py
│   ├── fault_injector.py
│   ├── hil_runner.py
│   └── safety_monitor.py
tests/
├── test_fault_injection.py
├── test_degraded_mode.py
└── test_recovery.py
requirements.txt
pytest.ini
```

## Lancer les tests

```bash
cd projects/hil-fault
pip install -r requirements.txt
pytest tests/ -v
```

## Stack

`Python · pytest · GitHub Actions · STM32 (target HIL)`

## Auteur

Nicolas Lecomte — ECE Bordeaux · Stage Dassault Aviation
