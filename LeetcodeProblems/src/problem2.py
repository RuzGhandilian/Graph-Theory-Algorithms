# Problem 2: Target Sum

def find_target_sum_ways(nums, target):
    total = sum(nums)
    # check if target is valid
    if total < abs(target) or (total + target) % 2 != 0:
        return 0

    s = (total + target) // 2

    # dp[i] = number of ways to reach sum i
    dp = [0] * (s + 1)
    dp[0] = 1  # one way to reach 0

    for num in nums:
        for j in range(s, num - 1, -1):
            dp[j] += dp[j - num]

    return dp[s]
