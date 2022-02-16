import random
from re import X

# Y = kX + C

# Вещественное число
k = random.uniform(-5, 5)
c = random.uniform(-5, 5)

# Набор точек Х:У
data = {
    22: 150, 
    23: 155, 
    24: 160, 
    25: 162, 
    26: 171, 
    27: 174, 
    28: 180, 
    29: 183, 
    30: 189, 
    31: 192
}
speed = 0.0001


def process(x):
    return k*x + c


def test(x):
    for key in data.keys():
        if process(x) != data[key]:
            return False
    return True

print(f"Start: Y = {k} * X + {c}")
i = 0
while True:
    i -= -1
    x = random.choice(list(data.keys()))
    true_res = data[x]
    out = process(x)

    delta = true_res - out

    k += delta * x * speed
    c += delta * speed

    if test(x):
        print("TEST")
        break
    if i == 100000000:
        print("NON TEST")
        break
    




print(f"The End: Y = {k} * X + {c}")
