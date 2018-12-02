result = 0
with open('input.txt') as f:
    for line in f:
        try:
            result += int(line)
        except ValueError:
            # Invalid value, skip
            pass
return result
