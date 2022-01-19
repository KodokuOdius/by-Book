

class Neuron:

    def __init__(self, inp, out) -> None:
        self.inp = int(inp)
        self.out = int(out)
        self.weight = 0.001
    
    def learning(self):
        count = 1
        while self.inp * self.weight != self.out:
            print("Итерация #", count, self.weight)
            if (self.inp * self.weight) == self.out:
                break
            else:
                if self.inp * self.weight < self.out:
                    self.weight = round(self.weight + 0.001, 4)
                else:
                    self.weight = round(self.weight - 0.001, 4)
            count += 1

    def predict(self, new_inp):
        return new_inp * self.weight


if __name__ == "__main__":
    start = 50
    end = 75
    mNeu = Neuron(50, 75)
    mNeu.learning()
    print(mNeu.predict(759))
    print(mNeu.weight)

