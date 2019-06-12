import random
import math
class perceptron():

    weights = []
    lr = 0.01

    def __init__(self, input_size):
        random.seed(None, 2)
        for i in range(0, input_size):
            self.weights.append(random.uniform(-1, 1))

    def guess(self, inputs):
        sum = 0
        for i in range(0, len(self.weights)):
            sum += inputs[i] * self.weights[i]
        return self.activation(sum, "sign")

    def activation(self, value, Type='sigmoid'):
        if (Type == 'sign'):
            return 1 if(value >= 0) else -1
        elif (Type == 'sigmoid'):
            return 1 / (1+math.exp(-value))
        

    def train(self, inputs, target):
        result_guess = self.guess(inputs)
        error = target - result_guess

        for i in range(0, len(self.weights)):
            self.weights[i] += error * inputs[i] * self.lr

        return result_guess

    def guessY(self, x):
        w0 = self.weights[0]
        w1 = self.weights[1]
        w2 = self.weights[2]

        return - (w2 / w1) - (w0 / w1) * x