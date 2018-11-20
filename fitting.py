

import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')
def myfunc(x):
    return x**2*np.sin(x) + np.cos(x)

x = np.linspace(0, 2*3.14, 8)
y = myfunc(x)

underfitting = np.poly1d(np.polyfit(x, y, deg=3))

good = np.poly1d(np.polyfit(x,y,deg=6))

overfitting = np.poly1d(np.polyfit(x,y, deg = 30))



xp = np.linspace(0, 2*3.14, 100)
yp = myfunc(xp)
plt.plot(x, y, '*', xp ,yp, '-', xp, underfitting(xp), '--')
plt.legend(['Sampled function', 'Actual function', 'Polynomial of degree 3'])
plt.figure()
plt.plot(x,y, '*', xp ,yp, '-', xp, good(xp), '--')
plt.legend(['Sampled function', 'Actual function', 'Polynomial of degree 6'])
plt.figure()
plt.plot(x,y, '*', xp,yp, '-', xp, overfitting(xp), '--')
plt.legend(['Sampled function', 'Actual function', 'Polynomial of degree 30'])
plt.show()




