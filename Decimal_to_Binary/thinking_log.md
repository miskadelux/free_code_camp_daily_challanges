# Decimal → Binary

## Problem

Convert a decimal integer to a binary string.

## Pseudocode

1. Start with an empty string.
2. While the number is not 0:
   - Find the remainder when dividing by 2.
   - Save the remainder.
   - Divide the number by 2.
3. Reverse the result.
4. Return the result.

## Example

Input:
13

Process:
13 → remainder 1
6  → remainder 0
3  → remainder 1
1  → remainder 1

Remainders:
1011

Reverse:
1101

Output:
1101
