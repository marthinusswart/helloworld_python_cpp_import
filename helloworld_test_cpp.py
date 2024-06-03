from lib.helloworld_python import *


def main():
    print("Main function")
    result: float = multiply(3, 3)
    print("Result {}".format(result))

    result = addList([1, 2, 3])
    print("Result {}".format(result))


if __name__ == "__main__":
    main()
