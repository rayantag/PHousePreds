from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

"""
Returns a fully connected neural network. 
Inputs:
    - num_layers: integer for how many layers you want
    - num_nodes: array where each ith element is the number of nodes in the i+1th layer
    - input_shape: tuple for shape of input
    - act_fns: array of activation functions for each layer

Returns:
Fully connected neural net with desired config
"""

def getBasicModel(num_layers, num_nodes, input_shape, act_fns):
    layers = [Dense(num_nodes[0], activation = act_fns[0], input_shape = input_shape)]
    layers += [Dense(num_nodes[layer], activation = act_fns[layer]) for layer in range(1, num_layers - 1)]
    layers += [Dense(1)]
    return Sequential(layers)