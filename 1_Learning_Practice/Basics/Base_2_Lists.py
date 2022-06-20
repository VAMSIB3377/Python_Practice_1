
nums = [32, 4, 56, 78, 56, 65, 3, 42]

names = ['abc', 'bcd', 'cde', 'def']

values = [9.5, 'abc', 25]

mil = [nums, names, values]

nums.sort()
print(nums)
print(nums[0])
print(len(nums))
nums.append(45)
print(nums)
print(nums.count(56))
print(nums[3:])
print(nums[:-3])
print(nums[::-1])
print(names)
print(values)
print(mil)
nums.insert(3,14)
print(nums)
nums.remove(56)
print(nums)
print(nums.index(56))
print(nums.pop())
print(nums.pop(5))
del nums[5:]
print(nums)

nums.extend([35,45,67,86,54])
nums.sort()
print(nums)
