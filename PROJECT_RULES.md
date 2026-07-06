# Atlas Core

Version: 1.0

Status: ACTIVE

---

# Mission

Build the most reliable Decision Support System for Iranian Commodity Funds.

The system MUST help investors make better decisions.

The system MUST NOT generate random or unexplained signals.

---

# Core Principles

1. Every decision must be explainable.

2. No fake data.

3. No hardcoded market values.

4. Every feature must be backtestable.

5. Every signal must have evidence.

6. Every module has ONE responsibility.

7. Data collection must be independent from analysis.

8. Strategy must be independent from data source.

9. Every important action must be logged.

10. Missing data is better than wrong data.

---

# Data Rules

Historical data is immutable.

Never overwrite historical candles.

Append only.

Every candle must be validated.

Duplicate dates are forbidden.

Missing dates must be reported.

---

# NAV Rules

NAV must be stored independently.

Premium must always be calculated.

If NAV is unavailable:

Premium = Unknown

Never estimate NAV.

---

# Signal Rules

BUY

SELL

WAIT

are generated only after

Data Validation

Indicators

Risk Check

Quality Check

Score Engine

Decision Engine

---

# Backtest Rules

Never use future data.

Every decision must only use information available on that date.

Look Ahead Bias is forbidden.

---

# Code Rules

No duplicated logic.

No duplicated files.

No magic numbers.

Everything configurable.

Readable code first.

Performance second.

Premature optimization is forbidden.

---

# Logging

Every update

Every signal

Every error

Every warning

must be logged.

---

# Future Ready

The architecture must support

Unlimited funds

Unlimited strategies

Multiple data providers

Machine Learning modules

REST API

Dashboard

Without rewriting the core.

---

# Golden Rule

When uncertain,

DO NOT GUESS.

Validate.
