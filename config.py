# Atlas Core
# config.py
# Version: 1.0.0
# Purpose: Central configuration for all system modules

from dataclasses import dataclass

# -----------------------------
# GENERAL SETTINGS
# -----------------------------

MODE = "BACKTEST"   # BACKTEST | LIVE
BASE_CURRENCY = "IRT"

DEBUG = True

# -----------------------------
# DATA SETTINGS
# -----------------------------

DATA_PATH = "data/"
HISTORY_PATH = "data/history/"
NAV_PATH = "data/nav/"
SNAPSHOT_PATH = "data/snapshots/"
REPORT_PATH = "data/reports/"
CACHE_PATH = "data/cache/"

# -----------------------------
# FUNDS SETTINGS
# -----------------------------

FUNDS = {
    "NQRABI": {
        "name": "نقرابی",
        "symbol": "NQRABI",
        "active": True
    },
    "AYAR": {
        "name": "عیار",
        "symbol": "AYAR",
        "active": True
    },
    "NAHAL": {
        "name": "نهال",
        "symbol": "NAHAL",
        "active": True
    },
    "SYNERGY": {
        "name": "سینرژی",
        "symbol": "SYNERGY",
        "active": True
    }
}

# -----------------------------
# INDICATOR SETTINGS
# -----------------------------

EMA_FAST = 20
EMA_SLOW = 50

RSI_PERIOD = 14

MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9

ATR_PERIOD = 14

VOLUME_LOOKBACK = 20

# -----------------------------
# SCORE WEIGHTS
# -----------------------------

WEIGHTS = {
    "trend": 0.20,
    "macd": 0.10,
    "rsi": 0.10,
    "momentum": 0.10,
    "volume": 0.15,
    "nav": 0.20,
    "macro": 0.15
}

# -----------------------------
# RISK SETTINGS
# -----------------------------

MAX_ACCEPTABLE_PREMIUM = 0.05   # 5%
HIGH_RISK_THRESHOLD = 0.70

# -----------------------------
# SIGNAL SETTINGS
# -----------------------------

BUY_THRESHOLD = 75
SELL_THRESHOLD = 35

MIN_CONFIDENCE = 0.70

# -----------------------------
# BACKTEST SETTINGS
# -----------------------------

INITIAL_CAPITAL = 10000000  # 10M IRT
FEE = 0.0015  # 0.15%

SLIPPAGE = 0.001

# -----------------------------
# LOGGING SETTINGS
# -----------------------------

LOG_LEVEL = "INFO"
SAVE_LOGS = True
