a = [5, 1, 4, 2, 3]

for p in range(len(a) - 1):
    for i in range(len(a) - 1 - p):
        j = i + 1
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print(a)            