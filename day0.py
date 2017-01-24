#!/usr/bin/env python
# Given an array, X, of N integers, calculate and print the the respective mean, median, and mode on separate lines.
# If your array contains more than one modal value, choose the numerically smallest one.
#
# mean:     sum all elements together then divide by the amount of elements
# median:   order all elements then select the middle (if total is even, take middle two elements and average them)
# mode:     the element that occurs most frequently
#
# sample input:
#
# 10
# 64630 11735 14216 99233 14470 4978 73429 38120 51135 67060

if __name__ == '__main__':
    import fileinput

    lines = []
    mean = 0
    median = 0
    mode = 0

    for line in fileinput.input():
        lines.append(line)
    assert len(lines) == 2

    try:
        data = [int(n) for n in lines[1].split()]
        data_len = len(data)
    except:
        print 'invalid input'
        exit(-1)

    if not data_len:
        print 'you must provide some input'
        exit(-1)

    data.sort()

    # mean
    mean = sum(data) / max(float(data_len), 1)

    # median
    middle_element_index = data_len / 2
    if data_len % 2:
        median = data[middle_element_index]
    else:
        median = (data[middle_element_index - 1] + data[middle_element_index]) / 2.0

    # mode
    occurences = [(n, data.count(n)) for n in data]
    occurences.sort()

    mode = max(occurences, key=lambda x: x[1])
    mode = mode[0]

    print '{0:.1f}\n{1:.1f}\n{2:.0f}'.format(mean, median, mode)
