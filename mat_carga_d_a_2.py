import random

mat = [None] * 4
for f in range(4):
    mat[f] = [None] * 8

for n in range(16):
    for i in range(2):
        f = random.randint(0,3)
        c = random.randint(0,7)
        while(mat[f][c] != None):
            f = random.randint(0,3)
            c = random.randint(0,7)
        mat[f][c] = n

for f in range(4):
    for c in range(8):
        print(mat[f][c],'\t', end = ' ')
    print()

