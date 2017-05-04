#!/usr/bin/env python3


def minkowski(vec1, vec2, r=2):
    dist = 0
    for index, x in enumerate(vec1):
        dist += abs(vec1[index] - vec2[index]) ** r
    return dist ** (1/r)

def euclidean(vec1, vec2):
    return minkowski(vec1, vec2, r=1)

def manhattan(vec1, vec2):
    return minkowski(vec1, vec2, r=2)

def main():
    pass

if __name__ == "__main__":
    main()

