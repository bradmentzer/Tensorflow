import tensor_intro as tf # imports tf module
print(tf.version)

# Tensors
#Generalization of vectors and matrices to higher dimentions
#example tensors with value and defines data type
string = tf.Variable("this is a string", tf.string)
number = tf.Variable(324, tf.int16)
floating = tf.Variable(3.567, ft.float64)

# Degree of tensor --> number of dimentions in tensor
# Degree determined by deepest level of nested list
# scalars are 0 dimentional, array has rank 1
rank1_tensor = tf.Variable(["Test", "Ok", "Brad"], tf.string)
#List inside of a list makes rank 2 tensor (matrix)
rank2_tensor = tf.Variable(["test", ok], ["test", "yes"], tf.string)

#Determine rank
tf.rank(rank1_tensor)

# Shape is the amount of elemebts in each dimention
rank1_tensor.shape

# Changing shape
tensor1 = tf.ones([1,2,3]) # creates a shape [1,2,3] tensor full of ones
tensor2 = tf.reshape(tensor1, [2,3,1]) # # reshape dataset to shape [2,3,1]
tensor3 = tf.reshape(tensor2, [3,-1]) # -1 tells the tensor to calculate the size of the dimension in that plate
                                      # this will reshape the tensor to [3,2]

#the number of elements in reshaped tensor byst match origional

print(tensor1)
print(tensor2)
print(tensor3)


# Types of tensors
# Variable
# Constant
# Placeholder
# SparseTensor
# All types except for variable are immutable

# To evaluate a tensor, create a session
with tf.Session as sess: #creates a session with default graph
    tensor.eval() #tensor will be the name of tensor