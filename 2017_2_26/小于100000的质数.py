import math

array = range(2, 100001)
i = 0
while i < len(array):
    if_delete = 0
    tmp = math.sqrt(array[i])
    j = 0
    while array[j] <= tmp:
        if array[i] % array[j] == 0:
            del array[i]
            if_delete = 1
            break
        j += 1
    if if_delete == 0:
        i += 1
print array
raw_input("press any key to exit")