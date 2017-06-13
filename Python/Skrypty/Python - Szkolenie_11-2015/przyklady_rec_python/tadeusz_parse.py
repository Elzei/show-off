#!/usr/bin/env python2.7

from collections import Counter

def parse_file(file_name):
    answer = []
    for line in open(file_name, "rb"):
        answer.append(line)
    return answer

def count_words(line_list):
    c = Counter()
    for line in line_list:
        for word in line.split(" "):
            c[word] += 1
    return c


if __name__ == '__main__':
    c = count_words(parse_file('pan-tadeusz.txt'))
    for word, count in c.most_common(5):
        print word, ":", count

