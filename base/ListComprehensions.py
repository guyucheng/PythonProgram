# a list comprehension
cubes = [i**3 for i in range(5)]
nums = [i*2 for i in range(10)]
print(cubes)
print(nums)

evens=[i**2 for i in range(10) if i**2 % 2 == 0]

print(evens)