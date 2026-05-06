class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            row_sum = sum(customer)
            max_wealth = max(max_wealth, row_sum)
        return max_wealth