arr = [2, 8, 9, 48, 8, 2, -12, 2]

print(arr)

result = [x + 2 for x in arr if x > 5]
result2 = set(result)
print(result)