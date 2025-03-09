def count_ways(coins, n, amount):
    if amount==0:
        return 1

    if amount < 0:
        return 0

    if n<= 0 and amount >= 1:
        return 0
    
    return count_ways(coins, n-1, amount) + count_ways(coins, n, amount - coins[n-1])

coins = [1, 2, 5]
amount = 5
n=len(coins)

print(f"The number of ways to divde {amount} with coins {coins}: {count_ways(coins, n, amount)}")
    
