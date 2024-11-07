def factorial(number):
    if number == 0:
        return 1
    elif number == 1:
        return 1
    else:
        return number * factorial(number - 1)


number = factorial(10)
print(number)
