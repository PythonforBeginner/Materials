def addStrings(num1: str, num2: str) -> str:
    n1 = int(num1)
    n2 = int(num2)
    return str(n1 + n2)


if __name__ == '__main__':
    print(addStrings("11", "123"))
    print(addStrings("456","77"))
    print(addStrings("0", "0"))
