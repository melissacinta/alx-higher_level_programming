#!/usr/bin/python3
if __name__ == "__main__":
    """perform calcualtions based on user input"""
    from calculator_1 import add, sub, mul, div
    import sys

    args = sys.argv

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif args[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        print("{} {} {} = ".format(args[1], args[2], args[3]), end="")
        if args[2] == "+":
            print("{}".format(add(int(args[1]), int(args[3]))))
        elif args[2] == "-":
            print("{}".format(sub(int(args[1]), int(args[3]))))
        elif args[2] == "*":
            print("{}".format(mul(int(args[1]), int(args[3]))))
        else:
            print("{}".format(div(int(args[1]), int(args[3]))))
        sys.exit(0)
