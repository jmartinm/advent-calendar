def find_duplicate(f, frequencies, result):
    f.seek(0)  # Needed for second iteration of the file
    for line in f:
        try:
            result += int(line)
        except ValueError:
            # Invalid value, skip
            pass
        if result in frequencies:
            return (result, True)
        else:
            frequencies.add(result)
    return (result, False)

def main():
    frequencies = set()
    result = 0
    frequencies.add(result)
    solution_found = False
    with open('input.txt') as f:
        while not solution_found:
            result, solution_found = find_duplicate(f, frequencies, result)
        print(result)

if __name__ == '__main__':
    main()
