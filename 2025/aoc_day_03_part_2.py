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


sum_of_joltage = 0

for battery_bank in battery_banks:
    max_joltage = max_subsequence(battery_bank.rstrip(), 12)
    sum_of_joltage = sum_of_joltage + int(max_joltage)

print(f'sum_of_joltage = {sum_of_joltage}')
