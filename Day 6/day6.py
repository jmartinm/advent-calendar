from collections import defaultdict

def get_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_grid(lowest_x, lowest_y, highest_x, highest_y, points):
    for i in range(lowest_x, highest_x + 1):
        for j in range(lowest_y, highest_y + 1):
            yield i, j

def is_infinite(lowest_x, lowest_y, highest_x, highest_y, point, distances):
    x, y = point[0], point[1]

    infinite = True
    while x >= lowest_x:
        if distances[x, y] != point:
            infinite = False
        x -= 1

    if infinite:
        return True

    x, y = point[0], point[1]

    infinite = True
    while y >= lowest_y:
        if distances[x, y] != point:
            infinite = False
        y -= 1

    if infinite:
        return True

    x, y = point[0], point[1]

    infinite = True
    while x <= highest_x:
        if distances[x, y] != point:
            infinite = False
        x += 1

    if infinite:
        return True

    x, y = point[0], point[1]

    infinite = True
    while y <= highest_y:
        if distances[x, y] != point:
            infinite = False
        y += 1

    if infinite:
        return True

    return False


def main():
    point_to_distances = {}
    position_counter = defaultdict(list)
    with open('input.txt') as f:
        points = []
        lowest_x = None
        lowest_y = None
        highest_x = None
        highest_y = None
        for line in f:
            x, y = line.split(',')
            x, y = int(x), int(y)
            if lowest_x is None:
                lowest_x = x
            else:
                lowest_x = min(x, lowest_x)
            if highest_x is None:
                highest_x = x
            else:
                highest_x = max(x, highest_x)
            if lowest_y is None:
                lowest_y = y
            else:
                lowest_y = min(y, lowest_y)
            if highest_y is None:
                highest_y = y
            else:
                highest_y = max(y, highest_y)

            points.append((x,y))

        for x, y in get_grid(lowest_x-1, lowest_y-1, highest_x+1, highest_y+1, points):
            for point in points:
                distance = get_distance(point, (x,y))
                position_counter[(x, y)].append((point, distance))

        closest_counter = defaultdict(int)

        result = {}

        for key, value in position_counter.items():
            value.sort(key=lambda x: x[1])

            if value[0][1] != value[1][1]:
                closest_counter[value[0][0]] += 1
                result[key] = value[0][0]
            else:
                result[key] = None

        max_distance = -1
        for key, value in closest_counter.items():
            if value > max_distance and not is_infinite(lowest_x, lowest_y, highest_x, highest_y, key, result):
                max_distance = value

        # Part 1

        print(max_distance)

        # Part 2

        result = 0
        for key, value in position_counter.items():
            total = sum(x[1] for x in value)
            if total < 10000:
                result += 1

        print(result)

if __name__ == '__main__':
    main()
