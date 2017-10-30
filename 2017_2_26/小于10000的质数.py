array = range(2, 10001)
i = 0
while i < len(array):
    j = i + 1
    while j < len(array):
        if array[j] % array[i] == 0:
            del array[j]
        else:
            j += 1
    i += 1
print array
raw_input("press any key to exit")