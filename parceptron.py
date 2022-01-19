

# Укаждого сеносра свой вес
def parceptron(sensor = list()):
    b = 7
    s = sum((int(sensor[i]) * weight[i] for i in range(len(sensor))))

    return (False, True)[s >=b]


if __name__ == "__main__":
    from random import randint

    lenght_line = 15

    weight = tuple(1 for _ in range(lenght_line))
    num1 = tuple(str(randint(0, 1)) for _ in "_" * lenght_line)
    num2 = tuple(str(randint(0, 1)) for _ in "-" * lenght_line)

    print(weight)
    print(num1)
    print(parceptron(num1))

    print(num2)
    print(parceptron(num2))
