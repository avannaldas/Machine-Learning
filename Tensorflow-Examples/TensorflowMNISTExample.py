'''
MNIST Example with Tensorflow's inbuilt dataset

'''
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

MNIST = input_data.read_data_sets("/tmp/data/", one_hot=True)
HL1_NODES = 500
HL2_NODES = 500
HL3_NODES = 500

OUT_NODES = 10
BATCH = 100

X = tf.placeholder('float', [None, 784])
Y = tf.placeholder('float')

def neuralnetworkmodel(data):
    '''
    Neural Network Model for MNIST Image Recognition
    '''
    h_layer1 = {'weights':tf.Variable(tf.random_normal([784, HL1_NODES])),
                'biases':tf.Variable(tf.random_normal([HL1_NODES]))}
    h_layer2 = {'weights':tf.Variable(tf.random_normal([HL1_NODES, HL2_NODES])),
                'biases':tf.Variable(tf.random_normal([HL2_NODES]))}
    h_layer3 = {'weights':tf.Variable(tf.random_normal([HL2_NODES, HL3_NODES])),
                'biases':tf.Variable(tf.random_normal([HL3_NODES]))}
    output_layer = {'weights':tf.Variable(tf.random_normal([HL3_NODES, OUT_NODES])),
                    'biases':tf.Variable(tf.random_normal([OUT_NODES]))}
    l1_out = tf.nn.relu(tf.add(tf.matmul(data, h_layer1['weights']), h_layer1['biases']))
    l2_out = tf.nn.relu(tf.add(tf.matmul(l1_out, h_layer2['weights']), h_layer2['biases']))
    l3_out = tf.nn.relu(tf.add(tf.matmul(l2_out, h_layer3['weights']), h_layer3['biases']))
    output = tf.matmul(l3_out, output_layer['weights']) + output_layer['biases']
    return output

def trainneuralnetwork(xinput):
    '''
    Trains the neural network model and optimizes the weights, biases
    '''
    prediction = neuralnetworkmodel(xinput)
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(prediction, Y))
    optimizer = tf.train.AdamOptimizer().minimize(cost)
    iterations = 12
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for itr in range(iterations):
            iter_loss = 0
            for _ in range(int(MNIST.train.num_examples/BATCH)):
                iter_x, iter_y = MNIST.train.next_batch(BATCH)
                _, itercost = sess.run([optimizer, cost], feed_dict={xinput:iter_x, Y:iter_y})
                iter_loss += itercost
            print("Step %d of %d | Loss: %d" % (itr, iterations, iter_loss))
            correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(Y, 1))
        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
        print('Accuracy:', accuracy.eval({xinput:MNIST.test.images, Y:MNIST.test.labels}))

trainneuralnetwork(X)
