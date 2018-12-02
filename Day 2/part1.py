from collections import defaultdict

def main():
    counts = defaultdict(int)
    with open('input.txt') as f:
        for line in f:
            local_counts = defaultdict(int)
            for letter in line:
                local_counts[letter] += 1
            seen = set()
            for value in local_counts.values():
                if value in (2, 3) and value not in seen:
                    counts[value] += 1
                    seen.add(value)
    result = 1
    for count in counts.values():
        result *= count
    print(result)


if __name__ == '__main__':
    main()
