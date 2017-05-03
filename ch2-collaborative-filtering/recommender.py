#!/usr/bin/env python3

import json

def load_data(filename="ratings.json"):
    data = None
    with open(filename, 'r') as fp:
        data = json.load(fp)
    return data


def main():
    ratings = load_data("ratings.json")
    print(ratings)

if __name__ == "__main__":
    main()

