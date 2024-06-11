#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    attributes = dir(hidden_4)
    for attr_name in attributes:
        if not attr_name.startswith("_"):
            print(attr_name)

