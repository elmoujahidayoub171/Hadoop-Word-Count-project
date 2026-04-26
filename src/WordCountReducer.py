#!/usr/bin/env python3
import sys

total = 0
lastword = None

for line in sys.stdin:
    line = line.strip()

    word, count = line.split("\t")
    count = int(count)

    if lastword is None:
        lastword = word
        total = count

    elif word == lastword:
        total += count

    else:
        print("%s\t%d occurrences" % (lastword, total))
        lastword = word
        total = count

if lastword is not None:
    print("%s\t%d occurrences" % (lastword, total))
