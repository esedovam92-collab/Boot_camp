def calculate_average(numbers):
    total = 0

    for number in numbers:
        total += number

    average = total / len(numbers)

    return total

scores = [80, 90, 100]

print("Average score:", calculate_average(scores))