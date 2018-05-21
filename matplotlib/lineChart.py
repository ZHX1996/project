from matplotlib import pyplot as plt

x = [1,2,3,4,5]
y1 = [1,2,3,4,5]
y2 = [5,4,3,2,1]
labels = ['a', 'b', 'c', 'd', 'e']

fig, ax = plt.subplots()

ax.plot(x, y1, 'r*-', label='y1')
ax.plot(x, y2, 'k--', label='y2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('test')
ax.legend(loc='upper center')
plt.show()