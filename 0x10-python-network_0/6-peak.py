#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(ints):
    """Return a peak in from a list of unsorted integers."""
    if ints == []:
        return None

    size = len(ints)
    if size == 1:
        return ints[0]
    elif size == 2:
        return max(ints)

    mid = int(size / 2)
    peak = ints[mid]
    if peak > ints[mid - 1] and peak > ints[mid + 1]:
        return peak
    elif peak < ints[mid - 1]:
        return find_peak(ints[:mid])
    else:
        return find_peak(ints[mid + 1:])
