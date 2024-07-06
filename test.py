#! /usr/bin/env python3

import time, cProfile

def add_up_numbers():
    total = 0
    for i in range(1, 1000001):
        total += i
    return total

cProfile.run('add_up_numbers()')