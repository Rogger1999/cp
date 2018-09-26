#!/bin/python

if __name__ == '__main__':
    year = int(raw_input())

def is_leap(year):
    leap = False

    if not (year % 400):
        leap = True
    elif not (year % 100):
        leap = False
    elif not (year % 4):
        leap = True
    else:
        leap = False

    return leap

print is_leap(year)