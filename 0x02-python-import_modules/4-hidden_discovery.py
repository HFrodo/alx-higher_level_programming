#!/usr/bin/python3.8
import hidden_4


def main():
    names = dir(hidden_4)
    for i in names:
        if i.startswith("__") is True:
            continue
        print(i)


if __name__ == "__main__":
    main()
