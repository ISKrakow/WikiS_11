def minimum_coins(n):
    coins = [25, 10, 5, 1]
    result = []
    for coin in coins:
        count = n // coin
        result.append((coin, count))
        n %= coin
    return result

n = int(input("Enter the value of n: "))
coins_used = minimum_coins(n)
print(f"The minimum number of coins required to make {n} cents is:")
for coin, count in coins_used:
    print(f"{count} coins of {coin} cents")
