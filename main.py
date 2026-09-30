a = (input('Введите числа через запятую: '))
b = a.split(',')
l = []
for i in b:
    l.append(int(i))
print(sum(l))
print(sum(l)/len(l))
print(max(l))