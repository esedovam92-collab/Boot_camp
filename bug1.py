def divide_numbers(a, b):
    return a / b

numbers = [20, 10, 0]

for i in range(len(numbers)):
    print(divide_numbers(numbers[i], numbers[i + 1]))