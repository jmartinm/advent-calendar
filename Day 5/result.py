def get_content_size(content):
    i = 0
    while i < len(content) - 1:
        if (content[i] != content[i+1]) and (content[i].lower() == content[i+1].lower()):
            content = content[:i] + content[i+2:]
            if i > 0:
                i -= 1
        else:
            i += 1

    return len(content)

def main():
    with open('input.txt') as f:
        content = f.read().strip()

        # Part 1
        print(get_content_size(content))

        best = 1e10
        for letter in set(content.lower()):
            tmp = content.replace(letter, '').replace(letter.upper(), '')
            size = get_content_size(tmp)
            best = min(best, size)

        # Part 2
        print(best)


if __name__ == '__main__':
    main()
