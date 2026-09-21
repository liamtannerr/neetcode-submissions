import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        tab = [math.inf] * (amount + 1)
        tab[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    tab[a] = min(tab[a], 1 + tab[a - c])

        return tab[amount] if tab[amount] != math.inf else -1