'''
One solution to the zombit_monitoring Google foobar challenge.
Created on Feb 10, 2015

@author: sql.sith
'''


def answer(intervals):
    intervals.sort()
    coverage = 0
    a = b = None

    for c, d in intervals:
        if a is None:
            # new range:
            a = c
            b = d
        elif b < c:
            # no merge possible, increment coverage:
            coverage += (b-a)
            a, b = c, d
        elif b <= d:
            # merge producing (a,d):
            b = d

    if a is not None:
        coverage += (b-a)

    return(coverage)

intervals = [[10, 14], [4, 18], [19, 20], [19, 20], [13, 20], [1,2]]
print(answer(intervals))
