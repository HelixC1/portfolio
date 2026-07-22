# QUANT-SHIELD

> Surveillance temps réel de portefeuille crypto avec alertes et gestion du risque

[![Python](https://img.shields.io/badge/Python-3.11+-blue)]()
[![Async](https://img.shields.io/badge/Async-asyncio-green)]()

## Problème

Suivre plusieurs actifs crypto, détecter les mouvements anormaux et appliquer des règles de risque sans intervention manuelle constante.

## Solution

| Module | Rôle |
|--------|------|
| `price_feed` | Agrégation prix via API publique (simulation) |
| `risk_engine` | Stop-loss, drawdown max, allocation |
| `alert_manager` | Notifications console / webhook |
| `portfolio` | Positions, P&L, historique |

## Métriques (backtest démo)

- Latence alerte : **< 500 ms**
- Règles configurables : **12**
- Actifs suivis : **8**

## Structure

```
src/
├── quant_shield/
│   ├── __init__.py
│   ├── portfolio.py
│   ├── risk_engine.py
│   ├── price_feed.py
│   └── alert_manager.py
├── demo.py
tests/
└── test_risk_engine.py
requirements.txt
```

## Démo

```bash
cd src
pip install -r ../requirements.txt
python demo.py
```

## Stack

`Python · asyncio · dataclasses · pytest`

## Auteur

Nicolas Lecomte — ECE Bordeaux
