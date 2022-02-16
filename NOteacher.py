import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class Parceptron:
    """
    Выполнить подгонку модели под тренировочные данные.
    Параметры
    Х - тренировочные данные: массив, размерность - X[n_samples, n_features],
    где
    n_samples - число образцов,
    п _features - число признаков,
    у - Целевые значения: массив, размерность - y[n_samples]
    Возвращает
    self: object
    """

    def __init__(self, speed=0.01, n=10) -> None:
        self.speed = speed # Speed of learning
        self.n = n # number of iterations
        
    # Process of learning
    def fit(self, X, y):
        # weights after learning
        # weights of neurons
        self.w = np.zeros(1 + X.shape[1])

        self.errors = []
        
        for _ in range(self.n):
            errors = 0

            for xi, target in zip(X, y):
                update = self.speed * (target - self.predict(xi))

                self.w[1:] += update * xi
                self.w[0] += update

                errors += int(update != 0.0)
            self.errors.append(errors)
        return self

    # clear input()
    def net_input(self, X):
        return np.dot(X, self.w[1:]) + self.w[0]

    # return target of class after ones jump
    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)



url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
df = pd.read_csv(url, header=None)
print('Данные об ирисах')
print(df.to_string())
df.to_csv('Iris.csv')


X = df.iloc[0:100, [0, 2]].values

print("Значения X - 100")
print(X)

y = df.iloc[0:100, 4].values
y = np.where(y == "Iris-setosa", -1, 1)
# Значение название цветков в виде -1 и 1, Y - 100
print(y)



# # Первые 50 элементов обучающей выборки (строки 0-50, столбцы - 0, 1)
# plt.scatter(
#     X[0:50, 0], 
#     X[0:50, 1], 
#     c='red', 
#     marker='o', 
#     label='щетинистый'
# )
# # Следующие 50 элементов обучающей выборки (строки 50-100, столбцы - 0, 1)
# plt.scatter(
#     X[50:100, 0], 
#     X[50:100, 1], 
#     c='blue', 
#     marker='x',
#     label='разноцветный'
# )
# # Формирование названий осей и вывод графика на экран
# plt.xlabel('Длина чашелистика') 
# plt.ylabel('Длина лепестка')

# plt.legend(loc='upper left')
# plt.show()

p = Parceptron(
    speed=0.01,
    n=10
)
p.fit(X, y)

plt.plot(range(1, len(p.errors) + 1), p.errors, marker='o')
plt.xlabel('Эпохи')
plt.ylabel('Чиcлo случаев ошибочной классификации')
plt.show()


