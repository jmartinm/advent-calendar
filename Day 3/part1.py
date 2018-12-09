def main():
    input = open('input.txt')
    area = []
    for i in range(1000):
        area.append([0] * 1000)

    for line in input:
        _, _, position, measures = line.split()
        left_pos = int(position[:-1].split(',')[0])
        top_pos = int(position[:-1].split(',')[1])
        width = int(measures.split('x')[0])
        height = int(measures.split('x')[1])
        for row in range(top_pos, top_pos + height):
            for col in range(left_pos, left_pos + width):
                area[row][col] += 1

    result = 0
    for x in range(1000):
        for y in range(1000):
            if area[x][y] > 1:
                result += 1

    print(result)

    input.seek(0)
    for line in input:
        id, _, position, measures = line.split()
        left_pos = int(position[:-1].split(',')[0])
        top_pos = int(position[:-1].split(',')[1])
        width = int(measures.split('x')[0])
        height = int(measures.split('x')[1])
        unique = True
        for row in range(top_pos, top_pos + height):
            for col in range(left_pos, left_pos + width):
                if area[row][col] > 1:
                    unique = False
        if unique:
            print(id)

if __name__ == '__main__':
    main()
