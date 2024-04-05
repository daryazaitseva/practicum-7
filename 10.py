sp = []
a = float(input())
while a != 0:
    a = float(input())
    sp.append(a)
k = 0
for i in range(0, len(sp) - 1):
    if sp[i] > sp[i + 1]:
        k += 1
print(k)
