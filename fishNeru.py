import numpy as np

# Activation functions
def onestep(x): # 1 or 0
    return (0, 1)[x >= 5]

def sigmoid(x): # {0. , 1.}
    return round(1 / (1 + np.exp(-x)), 4)

def th(x): # {-1. , 1.}
    # Hyperbolic tangent
    # Гиперболический тангенс
    return np.tanh(x)
    

class Neuron:
    
    def __init__(self, weight):
      self.weight = weight

    def y(self, x):
        # Сумма произведений массивов
        # Точечное произведение
        # s = w1 * x1 + w2 * x2 + ... + wn * xn
        s = np.dot(self.weight, x) 
        return th(s)


if __name__ == "__main__":
    # ветер - х1
    # атмосферное давление - x2
    # яркость солнца - x3
    # перепад температуры воды - х4

    xi = np.array([0, 0, 0, 0])
    wi = np.array([5, 4, 3, 1])

    n = Neuron(wi)
    
    print("Решение:")
    print("Y =", n.y(xi))
