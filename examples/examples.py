import numpy as np
from numpy_utils import hcat, vcat, add_dim, to_type, eq, make_array, make_constant, equals

split = '\n------------------------------'

# example array
arr = np.array([[2, 1],
                [-1, 0]])

print(split)

# horizontal and vertical concatenation with scalar
print('hcat scalar: \n', arr | hcat | 6, split)
print('hcat scalar: \n', 3 | hcat | arr, split)

print('vcat scalar: \n', arr | vcat | 6, split)
print('vcat scalar: \n', 3 | vcat | arr, split)

# horizontal and vertical concatenation with array
print('hcat array: \n', arr | hcat | arr, split)
print('vcat array: \n', arr | vcat | arr, split)

# horizontal and vertical concatenation with scalar and array
print('hcat scalar and array: \n', arr | hcat | 9 | hcat | arr, split)
print('vcat scalar and array: \n', arr | vcat | 9 | vcat | arr, split)

# add dimension using an integer
print('add_dim int: \n', (arr | add_dim | -1).shape, split)

# add dimension using a tuple
print('add_dim tuple: \n', (arr | add_dim | (0, 0, -1)).shape, split)

# convert array to a type
print('to_type float: \n', (arr | to_type | np.float), split)
print('to_type uint8: \n', (list(arr) | to_type | np.uint8), split)

# test equality between arrays, lists, tuples
print('equals array=array: \n', (arr | eq | arr), split)
print('equals array=list: \n', (arr | eq | list(arr)), split)
print('equals tuple=list: \n', (tuple(arr) | eq | list(arr)), split)
print('equals array=array: \n', (equals(arr, arr)), split)

# make constant array with shape
print('make_constant: \n', make_constant(1, (3, 1)), split)

# make array from list or array of specified shape
print('make_array row: \n', make_array([1, 2, 3], (1, 3)), split)
print('make_array column: \n', make_array([1, 2, 3], (3, 1)), split)