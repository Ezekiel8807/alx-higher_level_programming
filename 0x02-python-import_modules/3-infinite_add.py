#!/usr/bin/python3
import sys

def main():
    list_arguments = sys.argv
    total_sum = 0  # Use a different variable name
    for count in range(1, len(list_arguments)):
        total_sum += int(list_arguments[count])
    print("{}".format(total_sum))

if __name__ == "__main__":
    main()

