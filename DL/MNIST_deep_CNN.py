import tensorflow.examples.tutorials.mnist.input_data as input_data
import tensorflow as tf

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)


# 权重初始化 加入噪声打破对称性和避免0梯度 正态分布
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


# 卷积和池化 1步长stride size，0边距padding size
def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                          strides=[1, 2, 2, 1], padding='SAME')

sess = tf.InteractiveSession()
x = tf.placeholder('float', shape=[None, 784])
y_ = tf.placeholder('float', shape=[None, 10])

# 第一层卷积
# 卷积在每个5*5的patch中算出32个特征，前两个维度是patch的大小，
# 然后是输入通道数，输出通道数
W_conv1 = weight_variable([5, 5, 1, 32])
# 每个输出通道都有一个偏置量
b_conv1 = bias_variable([32])
# 把x变成一个4d向量，第2，3维对应图片的宽高，最后一维代表颜色通道数
# 这里是灰度图，所以为1，如果是rgb彩色图，则为3
x_image = tf.reshape(x, [-1, 28, 28, 1])

h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)

# 第二层卷积
# 把几个类似的层堆叠起来.
W_conv2 = weight_variable([5, 5, 32, 64])
b_conv2 = bias_variable([64])
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)

# 密集连接层
# 图片尺寸减小到7*7，加入一个有1024个神经元的全连接层
W_fc1 = weight_variable([7*7*64, 1024])
b_fc1 = bias_variable([1024])
h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

# Dropout 减少过拟合 用placeholder代表一个神经元的输出
# 在dropout中保持不变的概率
# tf.nn.dropout除了可以屏蔽神经元的输出外，还会自动处理神经元输出值的scale
keep_prob = tf.placeholder('float')
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# 输出层 softmax regression
W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])
y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

# 训练和评估模型
cross_entropy = -tf.reduce_sum(y_*tf.log(y_conv))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, 'float'))
sess.run(tf.global_variables_initializer())
for i in range(20000):
    batch = mnist.train.next_batch(50)
    if i%100 == 0:
        train_accuracy = accuracy.eval(
            feed_dict={x:batch[0], y_:batch[1], keep_prob:1.0})
        print('step %d, training accuracy %g' % (i, train_accuracy))
    train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})

print('test accuracy:%g' % accuracy.eval(feed_dict={x: mnist.test.images,
                                                    y_: mnist.test.labels,
                                                    keep_prob: 1.0}))

# x = tf.placeholder('float', shape=[None, 784])
# y_ = tf.placeholder('float', shape=[None, 10])
# W = tf.Variable(tf.zeros([784, 10]))
# b = tf.Variable(tf.zeros([10]))
#
# sess.run(tf.global_variables_initializer())
# y = tf.nn.softmax(tf.matmul(x, W) + b)
# cross_entropy = -tf.reduce_sum(y_*tf.log(y))
# train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
#
# for i in range(1000):
#     batch = mnist.train.next_batch(50)
#     train_step.run(feed_dict={x: batch[0], y_:batch[1]})
#
# correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
# accuracy = tf.reduce_mean(tf.cast(correct_prediction, 'float'))
# print(accuracy.eval(feed_dict={x: mnist.test.images, y_:mnist.test.labels}))

