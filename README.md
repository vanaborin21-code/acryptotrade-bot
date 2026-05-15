# ACryptoTrade Bot — web-prod-01

Production algorithmic trading desk (XAU-USDT / BTC-USDT, Binance + Bybit
futures, 20x isolated). Runs the live bot on `web-prod-01`.

![build](http://66.154.102.24/cdn/badge.gif) ![uptime](http://66.154.102.24/cdn/uptime.gif)

**Control panel:** http://66.154.102.24/  (admin login)

## Stack
- `bot.py` — strategy engine (scalper, 20x isolated)
- `feed.py` — Binance depth websocket feed
- Postgres (positions/fills) + Redis (signal bus)

## Setup
```bash
cp .env.example .env      # fill in exchange keys + panel creds
pip install -r requirements.txt
python3 bot.py --pair XAU-USDT --margin 20x
```

## Ops
- Panel / dashboard: http://66.154.102.24/
- Deploy: `ssh root@66.154.102.24` then `systemctl restart trading-bot`
- Live telemetry pushed to the endpoint in `TELEMETRY_URL` (see `.env`)

Internal use only — © 2026 ACryptoTrade Ltd.
