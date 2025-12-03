import os

battery_banks = []

def load_battery_banks(file_name, battery_banks):
    file = open(file_name)
    for battery_bank in file.readlines():
        battery_banks.append(battery_bank)
    file.close()

load_battery_banks('2025/aoc_day_03.dat', battery_banks)

# from ChatGPT
def max_subsequence(s: str, k: int) -> str:
    """
    Returns the lexicographically largest subsequence of length k
    from the digit string s.
    """
    drop = len(s) - k     # how many characters we are allowed to discard
    stack = []

    for c in s:
        # Pop smaller digits to try to improve the number,
        # but only if we still have drops left.
        while drop and stack and stack[-1] < c:
            stack.pop()
            drop -= 1
        stack.append(c)

    # If we didn't drop enough characters, trim from the end.
    return "".join(stack[:k])

def corey_lambs_get_largest_num(number: str, digit_count: int) -> str:
    # Base cases
    if len(number) == 0 or digit_count <= 0:
        return ""
    if len(number) == digit_count:
        return number

    # We can only pick the first digit from this window:
    # number[0 : len(number) - (digit_count - 1)]
    search_limit = len(number) - (digit_count - 1)
    window = number[:search_limit]

    # Find max digit and its index in the window
    max_digit = '-1'
    max_index = -1
    for i, ch in enumerate(window):
        if ch > max_digit:
            max_digit = ch
            max_index = i

    # Select max_digit, then recurse on the remainder
    return max_digit + corey_lambs_get_largest_num(number[max_index + 1:], digit_count - 1)

# another from ChatGPT
def max_subsequence_dp(s: str, k: int) -> str:
    n = len(s)
    dp = [[""] * (k + 1) for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(1, k + 1):
            # Option 1: skip s[i]
            best = dp[i + 1][j]

            # Option 2: take s[i] if enough digits remain
            if n - i >= j:
                candidate = s[i] + dp[i + 1][j - 1]
                if candidate > best:
                    best = candidate

            dp[i][j] = best

    return dp[0][k]


sum_of_joltage = 0

for battery_bank in battery_banks:
    #max_joltage = max_subsequence(battery_bank.rstrip(), 12)
    max_joltage = corey_lambs_get_largest_num(battery_bank.rstrip(), 12)
    # max_joltage = max_subsequence_dp(battery_bank.rstrip(), 12)
    sum_of_joltage = sum_of_joltage + int(max_joltage)

print(f'sum_of_joltage = {sum_of_joltage}')
