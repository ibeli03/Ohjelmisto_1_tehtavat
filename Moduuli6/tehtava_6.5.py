def no_unevens(numbers):
    return [num for num in numbers if num % 2 == 0]

list = [1,2,4,5,6,7]

print(f"The original list is {list}")
print(f"The even list is {no_unevens(list)}")


