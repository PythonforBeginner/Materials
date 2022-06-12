def interpret(command: str) -> str:
    command = command.replace("()", "o")
    command = command.replace("(al)", "al")
    return command


if __name__ == '__main__':
    print(interpret("G()(al)"))
    print(interpret("G()()()()(al)"))
    print(interpret("(al)G(al)()()G"))
