from collections import defaultdict

def main():
    counts = defaultdict(int)
    with open('input.txt') as f:
        all_lines = f.readlines()
        for i in range(len(all_lines)):
            for j in range(i+1, len(all_lines)):
                differences = 0
                x, y = 0, 0
                result = ''
                while x < len(all_lines[i]) and y < len(all_lines[j]):
                    if all_lines[i][x] != all_lines[j][y]:
                        differences += 1
                    else:
                        result += all_lines[i][x]
                    if differences > 1:
                        break
                    x += 1
                    y += 1
                if differences == 1:
                    print(result)
                    return

if __name__ == '__main__':
    main()
