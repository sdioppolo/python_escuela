t1 = int(0)
t2 = int(1)
print(t1, t2, end = ' ')
for t in range(3,11):
    ts = t1 + t2
    print(ts, end = ' ')
    t1 = t2
    t2 = ts
print()
