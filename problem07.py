import math

lenghtWagons = list(map(int, input().split(" ")))
lenghtStation = int(input())

counter = 0

# 1st get all combinations

# 2nd find all possible arrangemnts of a combination
def count_arrangments(nPositions, nWagons):
    return int(math.factorial(nPositions) / (math.factorial(nWagons) * math.factorial(nPositions - nWagons)))


print(count_arrangments(4, 2))



