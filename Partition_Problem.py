import itertools
def canBeSplitEqually(values):
  listSum = sum(values)

  if listSum % 2 == 0 and len(values) > 1:
    permutations = list(itertools.permutations(values))
    for permutation in permutations:
      halfSum = listSum / 2
      for number in permutation:
        if halfSum - number >= 0:
          halfSum -= number
          if halfSum == 0: return True
  return False

import datetime
begin_time = datetime.datetime.now()

print(canBeSplitEqually([1, 3, 3, 4, 5]) == True)
print(canBeSplitEqually([2, 4, 5, 6]) == False)
print(canBeSplitEqually([-1, -1]) == True)
print(canBeSplitEqually([-2, 3, 5]) == True)
print(canBeSplitEqually([1, 2, 3, 4]) == True)
print(canBeSplitEqually([-2, -3, 1]) == True)
print(canBeSplitEqually([-2, 3, 1]) == True)
print(canBeSplitEqually([0]) == False)
print(canBeSplitEqually([-33, -101, 50, 6187, 0, -0, 5, 1]) == False)
print(canBeSplitEqually([2, 4]) == False)
print(canBeSplitEqually([2, 2, 2, 2, 2]) == False)
print(canBeSplitEqually([500000, 1021, 4123, 2319, -42811, 3249, 10438, 13461, -87421, 100000, 504379]) == True)
print(canBeSplitEqually([0, 0, 0, 0, -42811, 0, 10438, 0, -87421, -504379, -624173]) == True)
print(canBeSplitEqually([8, 6, 3, 3, 2, 2]) == True)

print("Time taken:")
print(datetime.datetime.now() - begin_time)
