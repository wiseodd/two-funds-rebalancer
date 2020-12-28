# Two-Funds Buy-Only Portfolio Rebalancing Solver

**Requirements.** Only works for portfolios with two funds, e.g. the Couch Potato and classic two-funds 60-40 portfolios. Given your current portfolio value, desired allocation after rebalancing, and the amount of cash you have, this script will output how much of your cash should be used to buy stock/bonds (in percent).

### How to Use

1. Put your current portfolio value, target allocation, and the amount of cash into `input.json`.
2. Run `python rebalance.py`.

### Requirements

1. Python 3
2. NumPy
