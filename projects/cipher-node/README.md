# CIPHER-NODE

> Passerelle IoT sécurisée avec détection d'intrusion embarquée

[![Security](https://img.shields.io/badge/Security-TLS%201.3-green)]()
[![Platform](https://img.shields.io/badge/Platform-Linux%20Embedded-orange)]()

## Problème

Capteurs IoT exposés (ports ouverts, credentials par défaut) = pivot facile vers le réseau interne.

## Solution

| Composant | Fonction |
|-----------|----------|
| TLS terminateur | Chiffrement 100 % trafic sortant |
| Firewall dynamique | Règles iptables + blocklist |
| IDS léger | Détection port scan < 2 s |
| Secure logging | Logs signés HMAC-SHA256 |

## Métriques

- Trafic chiffré : **100 %**
- Détection port scan : **< 2 s**
- Overhead latence : **+12 ms**
- Scénarios attaque testés : **14**

## Architecture

```
[ IoT Sensors ] ──MQTT──► [ CIPHER-NODE ] ──TLS──► [ Cloud / Broker ]
                              │
                         IDS + Firewall
                         Secure Logs
```

## Structure

```
config/
├── firewall.rules
└── tls/
scripts/
├── setup_hardening.sh
├── ids_monitor.py
└── log_signer.py
docs/
└── threat-model.md
```

## Démo IDS (simulation)

```bash
cd scripts
python ids_monitor.py --demo
```

## Stack

`Linux embarqué · Python · OpenSSL · MQTT · iptables · Bash`

## Auteur

Nicolas Lecomte — ECE Bordeaux
