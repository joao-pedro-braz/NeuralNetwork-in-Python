from matrix import Matrix
from perceptron import perceptron
import math
import copy
import pickle
class NeuralNetwork():
    lr = 0.1
    inputNodes = 0
    HiddenNodes = 0
    OutputNodes = 0
    weights_ih = None
    weights_ho = None
    bias_ih = None
    bias_ho = None
    inputs = None
    hidden = None
    outputs = None

    def __init__(self, inputNodes, HiddenNodes, OutputNodes):
        self.inputNodes = inputNodes
        self.HiddenNodes = HiddenNodes
        self.OutputNodes = OutputNodes

        self.weights_ih = Matrix(self.HiddenNodes, self.inputNodes)        
        self.weights_ih.randomize()
        self.weights_ho = Matrix(self.OutputNodes, self.HiddenNodes)
        self.weights_ho.randomize()

        self.bias_ih = Matrix(self.HiddenNodes, 1)
        self.bias_ih.randomize()
        self.bias_ho = Matrix(self.OutputNodes, 1)
        self.bias_ho.randomize()


    def saveState(self):
        state = self 
        with open('NeuralNetworkState' + str(self.HiddenNodes) + str(self.inputNodes) + str(self.OutputNodes), 'wb') as NNState:
            pickle.dump(state, NNState)
        return state

    def recoverState(self):
        try:
            with open ('NeuralNetworkState' + str(self.HiddenNodes) + str(self.inputNodes) + str(self.OutputNodes), 'rb') as NNState:
                state = pickle.load(NNState)
            if (self.HiddenNodes == state.HiddenNodes):
                self.lr = state.lr
                self.inputNodes = state.inputNodes
                self.OutputNodes = state.OutputNodes
                self.weights_ih = state.weights_ih
                self.weights_ho = state.weights_ho
                self.bias_ih = state.bias_ih
                self.bias_ho = state.bias_ho
                self.inputs = state.inputs
                self.hidden = state.hidden
                self.outputs = state.outputs
            return state
        except Exception:
            pass

    def FeedForward(self, input_array):
        self.inputs = Matrix.fromArray(input_array)
        self.hidden = Matrix.MatrixMultiplication(self.weights_ih, self.inputs)
        self.hidden.add(self.bias_ih)
        Matrix.mapMatrix(self.hidden, NeuralNetwork.sigmoid)

        self.outputs = Matrix.MatrixMultiplication(self.weights_ho, self.hidden)
        self.outputs.add(self.bias_ho)
        Matrix.mapMatrix(self.outputs, NeuralNetwork.sigmoid)

        return self.outputs

    def guess(self, input_array):
        inputs = Matrix.fromArray(input_array)
        hidden = Matrix.MatrixMultiplication(self.weights_ih, inputs)
        hidden.add(self.bias_ih)
        Matrix.mapMatrix(hidden, NeuralNetwork.sigmoid)

        outputs = Matrix.MatrixMultiplication(self.weights_ho, hidden)
        outputs.add(self.bias_ho)
        Matrix.mapMatrix(outputs, NeuralNetwork.sigmoid)

        return outputs

    def train(self, input_array, targets):
        #error = targets - outputs
        inputs = Matrix.fromArray(input_array)
        hidden = Matrix.MatrixMultiplication(self.weights_ih, inputs)
        hidden.add(self.bias_ih)
        Matrix.mapMatrix(hidden, NeuralNetwork.sigmoid)

        outputs = Matrix.MatrixMultiplication(self.weights_ho, hidden)
        outputs.add(self.bias_ho)
        Matrix.mapMatrix(outputs, NeuralNetwork.sigmoid)

        output_errors = copy.deepcopy(outputs)
        output_errors.multiply(-1)
        targets = Matrix.fromArray(targets)
        output_errors.add(targets)
        #print(self.outputs.toArray())
        #print(output_errors.toArray())
        hidden_weights = Matrix.transpose(self.weights_ho)
        hidden_errors = Matrix.MatrixMultiplication(hidden_weights, output_errors)
        #print(hidden_errors.toArray())

        gradient = copy.deepcopy(outputs)
        Matrix.mapMatrix(gradient, NeuralNetwork.dsigmoid)  
        gradient.multiply(output_errors)
        gradient.multiply(self.lr)
        self.bias_ho.add(gradient)
        hidden_T = Matrix.transpose(hidden)
        weight_ho_deltas = Matrix.MatrixMultiplication(gradient, hidden_T)

        self.weights_ho.add(weight_ho_deltas)

        hidden_gradient = copy.deepcopy(hidden)
        Matrix.mapMatrix(hidden_gradient, NeuralNetwork.dsigmoid)  
        hidden_gradient.multiply(hidden_errors)
        hidden_gradient.multiply(self.lr)
        self.bias_ih.add(hidden_gradient)
        inputs_T = Matrix.transpose(inputs)
        weight_ih_deltas = Matrix.MatrixMultiplication(hidden_gradient, inputs_T)

        self.weights_ih.add(weight_ih_deltas)        

    def sigmoid(value):        
        return 1 / (1+ math.exp(-value))

    def dsigmoid(value):
        return value * (1 - value)