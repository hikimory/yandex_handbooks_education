import math

numbers = list(map(float, input().split()))
print(math.pow(math.prod(numbers), 1 / len(numbers)))