import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('logg.txt', delimiter=',', unpack=True)
plt.plot(x, y, label='Loaded from file!')

print(x)
print(y)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Some Data')
plt.legend()
plt.show()
