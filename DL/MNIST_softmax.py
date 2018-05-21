import tensorflow.examples.tutorials.mnist.input_data as input_data
import tensorflow as tf

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# 每张图片包含28*28=784个像素点
# mnist.train.images是一个形状为[60000,784]的张量
# 标签介于0到9之间，除某一位数字是1之外其余各维度都是0，10维向量
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x, W) + b)

y_ = tf.placeholder('float', [None, 10])
# 交叉熵 y是预测的概率分布，y_是实际的分布 用来衡量预测描述真相的低效性
cross_entropy = -tf.reduce_sum(y_*tf.log(y))
# 用梯度下降法以0.01的学习效率最小化交叉熵
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
# 布尔值转换成浮点数后求平均值
accuracy = tf.reduce_mean(tf.cast(correct_prediction, 'float'))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_:mnist.test.labels}))
