list_ = [2, 4, 6, 8, 10]

# спосіб 1: цикл for
result = 0
for i in list_:
    result += i
print('for:', result)

# спосіб 2: цикл while
sum = 0
i = 0
length = len(list_)
while i < length:
    sum += list_[i]
    i += 1

print('while:', result)

# спосіб 3: рекурсія зі зміною даних
def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + sum_list(numbers[1:])

print('recursion with change:', sum_list(list_))

# спосіб 4: рекурсія з акумуляцією
def sum_accum(numbers, level = 0):
    if level == len(numbers):
        return 0
    return numbers[level] + sum_accum(numbers, level + 1)

print('recursion with accumulation:', sum_accum(list_))