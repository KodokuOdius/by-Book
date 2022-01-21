
num0 = list('111101101101111')
    # 1 1 1     
    # 1 0 1     
    # 1 0 1
    # 1 0 1     
    # 1 1 1     

num1 = list('001001001001001')
    # 0 0 1 
    # 0 0 1
    # 0 0 1 
    # 0 0 1 
    # 0 0 1 

num2 = list('111001111100111')
    # 1 1 1 
    # 0 0 1 
    # 1 1 1 
    # 1 0 0 
    # 1 1 1 

num3 = list('111001111001111')
    # 1 1 1
    # 0 0 1 
    # 1 1 1
    # 0 0 1 
    # 1 1 1 

num4 = list('101101111001001')
    # 1 0 1 
    # 1 0 1 
    # 1 1 1 
    # 0 0 1 
    # 0 0 1 

num5 = list('111100111001111')
    # 1 1 1 
    # 1 0 0 
    # 1 1 1 
    # 0 0 1 
    # 1 1 1 

num6 = list('111100111101111')
    # 1 1 1 
    # 1 0 0 
    # 1 1 1 
    # 1 0 1 
    # 1 1 1 

num7 = list('111001001001001')
    # 1 1 1
    # 0 0 1 
    # 0 0 1 
    # 0 0 1 
    # 0 0 1 

num8 = list('111101111101111')
    # 1 1 1 
    # 1 0 1
    # 1 1 1
    # 1 0 1 
    # 1 1 1 

num9 = list('111101111001111') 
    # 1 1 1 
    # 1 0 1 
    # 1 1 1 
    # 0 0 1 
    # 1 1 1

nums = [
    num0, num1, num2,
    num3, num4, num5,
    num6, num7, num8,
    num9
]


sensors = 15
weights = [0 for _ in "_" * sensors]


def NumPars(sensor = list()):
    porog = 7
    s = sum([int(sensor[i]) * weights[i] for i in range(sensors)])
    if s >= porog: 
        return True
    else: 
        return False


def decrease(number = list()):
    for i in range(sensors):
        if int(number[i]) == 1:
            weights[i] -= 1

def increase(number = list()):
    for i in range(sensors):
        if int(number[i]) == 1:
            weights[i] += 1


theam = 5
n = 10000
for _ in "_" * n:
    from random import randint

    jn = randint(0, 9)
    result = NumPars(nums[jn])

    if jn != theam:
        if result:
            decrease(nums[jn])
    else:
        if not result:
            increase(nums[jn])


print(weights)

