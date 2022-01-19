

def NekoParceptron(sensor = list()):
    b = 2
    s = sum((sensor[i] * weight[i] for i in range(len(sensor))))

    # 0 - Neko (猫) - Cat
    # 1 - Inu (犬) - Dog
    return (0, 1)[s >= b]




if __name__ == "__main__":
    # S1 = 1 (лапы длинные), S1 = О (лапы короткие);
    # S2 = 1 (шерсть имеет ровный, однотонный окрас), S2 = О (шерсть разноцветная);
    # SЗ = 1 (голова имеет вытянутую форму), SЗ = О (голова имеет округлую форму).
    from random import randint

    lenline = 3

    weight = tuple(1 for _ in "-" * lenline)
    s = tuple(randint(0, 1) for _ in "-" * lenline)

    