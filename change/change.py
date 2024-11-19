def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")

    dp = [float("inf")] * (target + 1)
    dp[0] = 0
    coins_used = [None] * (target + 1)

    for coin in coins:
        for i in range(coin, target + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coins_used[i] = coin

    if dp[target] == float("inf"):
        raise ValueError("can't make target with given coins")

    result = []
    cur = target
    while cur > 0:
        result.append(coins_used[cur])
        cur -= coins_used[cur]

    if cur < 0:
        raise ValueError("can't make target with given coins")

    return sorted(result)


def find_fewest_coins_alt1(coins, target):
    memo = {}  # holds target sum -> (min coins count, [which coins])

    def solution(target):
        if target == 0:  # zero coins and coins_used list is empty
            return (
                0,
                [],
            )

        if target < 0:  # unachievable target
            return (
                float("inf"),
                [],
            )

        if target in memo:  # Already solved
            return memo[target]

        min_coins, coins_used = float("inf"), []
        for coin in coins:
            result, coins_combo = solution(target - coin)
            if result != float("inf") and result + 1 < min_coins:
                min_coins = result + 1
                coins_used = coins_combo + [coin]

        memo[target] = (
            min_coins,
            sorted(coins_used),
        )

        return memo[target]

    if target < 0:
        raise ValueError("target can't be negative")
    min_coins, coins_used = solution(target)
    if min_coins == float("inf"):
        raise ValueError("can't make target with given coins")

    return coins_used
