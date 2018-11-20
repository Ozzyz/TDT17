import matplotlib.pyplot as plt
plt.style.use('ggplot')

data = [(0, 1), (1,0), (1,1), (0,0)]

xval = [x[0] for x in data]
yval = [x[1] for x in data]



plt.scatter(xval[0:2], yval[0:2], color='blue')
plt.scatter(xval[2:], yval[2:], color='red')
plt.show()
