from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import numpy as np

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
learning_rate =0.001  # 学习率
training_iters = 100000  # 训练实例数
batch_size = 120  # 批大小
display_step = 10  # 训练10批显示1个
n_input = 28  # 每28个作为一个输入层的节点数
n_steps = 28  # 28个连续序列
n_hidden = 128  # 隐含层的节点数
n_classes = 10  # 输出的节点数

x = tf.placeholder("float", [None, n_steps, n_input])  # 构建输入节点
istate = tf.placeholder("float", [None, 2*n_hidden])  # 构建隐藏节点
y = tf.placeholder("float", [None, n_classes])  # 构建输出节点

weights = {
    'hidden': tf.Variable(tf.random_normal([n_input, n_hidden])),
    'out': tf.Variable(tf.random_normal([n_hidden, n_classes]))
}
biases = {
    'hidden': tf.Variable(tf.random_normal([n_hidden])),
    'out': tf.Variable(tf.random_normal([n_classes]))
}


# _X:批训练数据 _istate:隐藏节点
def RNN(_X, _istate, _weights, _biases):
    _X = tf.transpose(_X, [1, 0, 2])  # batch_size, n_steps, n_input->n_steps, batch_size, n_input
    _X = tf.reshape(_X, [-1, n_input])  # n_steps*batch_size, n_input
    _X = tf.matmul(_X, _weights['hidden'] + biases['hidden'])
    lstm_ceil = tf.nn.rnn_cell.BasicLSTMCell(n_hidden, forget_bias=1.0, state_is_tuple=False)
    _X = tf.split(_X, n_steps, 0)  # 序列切片，每片是一个(batch_size, n_hidden)
    outputs, states = tf.nn.static_rnn(lstm_ceil, _X, initial_state=_istate)
    return tf.matmul(outputs[-1], _weights['out']+_biases['out'])

pred = RNN(x, istate, weights, biases)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

# tf.argmax vector中的最大值
correct_pred = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

init = tf.global_variables_initializer()
sess = tf.InteractiveSession()
sess.run(init)
step = 1
while step * batch_size < training_iters:
    batch_xs, batch_ys = mnist.train.next_batch(batch_size)
    batch_xs = batch_xs.reshape(batch_size, n_steps, n_input)
    sess.run(optimizer, feed_dict={x:batch_xs, y:batch_ys, istate:np.zeros((batch_size, 2*n_hidden))})
    if step % display_step == 0:
        acc = sess.run(accuracy, feed_dict={x:batch_xs, y:batch_ys, istate:np.zeros((batch_size, 2*n_hidden))})
        loss = sess.run(cost, feed_dict={x:batch_xs, y:batch_ys, istate:np.zeros((batch_size, 2*n_hidden))})
        print('iter ' + str(step*batch_size) + ", minbatch loss= " + "{:.6f}".format(loss)
              + ", training accuracy= " + "{:.5f}".format(acc))
    step += 1
print('optimization finished')

test_len = 256
test_data = mnist.test.images[:test_len].reshape((-1, n_steps, n_input))
test_label = mnist.test.labels[:test_len]
print("test accuracy:",
      sess.run(accuracy, feed_dict={x: test_data, y: test_label, istate: np.zeros((test_len, 2 * n_hidden))}))
