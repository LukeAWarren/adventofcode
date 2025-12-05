# Chat GPT
import os

FILE = '2025/aoc_day_05.dat'


def load_ranges(file_name):
    """Read only the ranges from the input file."""
    ranges = []
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or '-' not in line:
                continue
            start, end = map(int, line.split('-', 1))
            ranges.append((start, end))
    return ranges


def merge_ranges(ranges):
    """Merge overlapping or adjacent ranges to avoid huge expansions."""
    if not ranges:
        return []
    # Tuples sort by first element by default, so we can avoid a lambda here.
    ranges.sort()
    merged = [ranges[0]]
    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    return merged


def count_ids(merged_ranges):
    """Count how many IDs are covered by the merged ranges (inclusive)."""
    return sum(end - start + 1 for start, end in merged_ranges)


def main():
    ranges = load_ranges(FILE)
    merged_ranges = merge_ranges(ranges)
    total_ids = count_ids(merged_ranges)

    print(f"Original ranges: {len(ranges)}")
    print(f"Merged ranges:   {len(merged_ranges)}")
    print(f"Total IDs:       {total_ids}")

    # If the covered set is small (e.g., sample input), show the IDs.
    if total_ids <= 200:
        ids = []
        for start, end in merged_ranges:
            ids.extend(range(start, end + 1))
        print("IDs:", ids)


if __name__ == "__main__":
    main()
