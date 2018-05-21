import tensorflow as tf
sess = tf.InteractiveSession()

x = tf.Variable([1.0, 2.0])
a = tf.constant([3.0, 3.0])
# 使用初始化器initializer op的run() 方法初始化'x'
x.initializer.run()

sub = tf.subtract(x, a)
print(sub.eval())
