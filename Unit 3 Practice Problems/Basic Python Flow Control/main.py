def fizzBuzz(n):
    answer = []
    for i in range(1, n + 1):
        if i % 3 == i % 5 == 0:
            answer.append("FizzBuzz")
        elif i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(f"{i}")
    return answer

if __name__ == '__main__':
    ''' test cases '''
    print(fizzBuzz(3))
    print(fizzBuzz(5))
    print(fizzBuzz(15))

