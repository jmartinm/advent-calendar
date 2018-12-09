from collections import Counter, defaultdict
import re

LINE_REGEX = '\[(.*)\]\s(.*)'

def main():
    guards_sleeps = defaultdict(int)
    guards_sleep_hours = defaultdict(list)
    with open('input.txt') as f:
        data = f.readlines()
        data.sort()
        current_guard = None
        for line in data:
            matches = re.search(LINE_REGEX, line)
            date, text = matches.groups()
            if 'Guard' in text:
                current_guard = int(text.split()[1][1:])
            elif 'asleep' in text:
                start_time = int(date[-2:])
            else:
                end_time = int(date[-2:])
                guards_sleeps[current_guard] += end_time - start_time
                guards_sleep_hours[current_guard].extend(range(start_time, end_time))

    max_sleeps = -1
    max_guard = None
    for guard, sleeps in guards_sleeps.items():
        if sleeps > max_sleeps:
            max_sleeps = sleeps
            max_guard = guard

    count_sleeps = Counter(guards_sleep_hours[max_guard])
    max_hour = count_sleeps.most_common()[0][0]

    # Part 1
    print(max_guard * max_hour)

    max_hour = -1
    max_guard = None
    for guard, hours in guards_sleep_hours.items():
        count_hours = Counter(hours)
        hour = count_hours.most_common()[0][0]
        if hour > max_hour:
            max_hour = hour
            max_guard = guard

    # Part 2
    print(max_guard * max_hour)


if __name__ == '__main__':
    main()
