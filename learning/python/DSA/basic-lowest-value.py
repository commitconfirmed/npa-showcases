#!/usr/bin/env python3

import random
import time

def main():
    list = [random.randint(1, 10000000) for _ in range(1000000)]
    start = time.time()
    lowest = list[0]
    for value in list:
        if value < lowest:
            lowest = value
    lowest_value = lowest
    # Or just do this, does the same thing and takes the same time it seems
    # lowest_value = min(list)
    print("Lowest value in the list:", lowest_value)
    end = time.time()
    print("Time taken to generate list:", end - start)

if __name__ == "__main__":
    main()

