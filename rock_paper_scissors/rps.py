#!/usr/bin/python

import sys

# if n >= 1:
#         for i in range(0, n):

#             for item in arr:
#                 for item2 in arr:
#                     tempArr = []
#                     tempArr.append(item)
#                     tempArr.append(item2)
#                     print('for2: ', tempArr)
#                     resultArr.append(tempArr)
#             print(resultArr)
#             print(resultArr * n)
#             return resultArr * n


def rock_paper_scissors(n):
    arr = ['rock', 'paper', 'scissors']
    resultArr = []
    if n >= 1:
        for item in arr:
            tempArr = [item]
            for i in range(0, n):
                print('first Temp: ', tempArr)
                tempArr.append(arr[n])
                resultArr.append(tempArr)
                print('first Result: ', resultArr)
                rock_paper_scissors(n-1)

    return resultArr


rock_paper_scissors(2)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
