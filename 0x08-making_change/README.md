# 0x08. Making Change Algorithm

## Overview

This project tackles a classic problem from the domain of dynamic programming and greedy algorithms: the coin change problem. The objective is to find the minimum number of coins required to make up a given total amount, given a list of coin denominations. By applying algorithms and problem-solving strategies, you'll devise a solution that's both correct and efficient.

### Project Details

- **Language:** Python
- **Weight:** 1
- **Start:** Apr 29, 2024 4:00 AM
- **End:** May 3, 2024 4:00 AM
- **Checker Released:** Apr 30, 2024 4:00 AM
- **Auto Review:** Will be launched at the deadline

## Problem Description

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

### Prototype

```python
def makeChange(coins, total)
Return
The fewest number of coins needed to meet the total.

If total is 0 or less, return 0
If total cannot be met by any number of coins you have, return -1
Constraints
Allowed Editors: vi, vim, emacs
Interpreted/Compiled: Ubuntu 20.04 LTS using Python3 (version 3.4.3)
Code should use PEP 8 style (version 1.7.x)
All files must be executable
Tasks
0. Change comes from within
Prototype: def makeChange(coins, total)
Return: fewest number of coins needed to meet total
If total is 0 or less, return 0
If total cannot be met by any number of coins you have, return -1
coins is a list of the values of the coins in your possession
The value of a coin will always be an integer greater than 0
You can assume you have an infinite number of each denomination of coin in the list
Your solution’s runtime will be evaluated in this task
Example
python

makeChange([1, 2, 25], 37) => 7
makeChange([1256, 54, 48, 16, 102], 1453) => -1
Repository Information
GitHub Repository: alx-interview
Directory: 0x08-making_change
File: 0-making_change.py
