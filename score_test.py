import random

def ordena_score(score):
    for i in range(len(score)-1):
        for j in range(i+1, len(score)):
            if(score[i][1] < score[j][1]):
                aux = score[i]
                score[i] = score[j]
                score[j] = aux



score = [['nn', 0],['nn', 0],['nn', 0],['nn', 0],['nn', 0]]
print(score)
for i in range(5):
    puntos = random.randint(100,999)
    if(score[4][1] < puntos):
        score[4][1] = puntos
        ordena_score(score)
        print(score)

