#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    array = []

    for _ in range(6):
        array.append(list(map(int, input().split())))

    maximum = -2147483647

    for i in range(6):
        for j in range(6):
            if i + 2 < 6 and j + 2 < 6:
                result = array[i][j] + array[i][j+1] + array[i][j+2] + \
                        array[i+1][j+1] + \
                        array[i+2][j] + array[i+2][j+1] + array[i+2][j+2]

                if result > maximum:
                    maximum = result

    print(maximum)
