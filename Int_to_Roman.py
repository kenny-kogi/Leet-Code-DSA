import matplotlib.pyplot as plt
import numpy as np
week=np.array([1,2,3,4,5,6,7,8,9])
weight=np.array([24.3,25,26.15,27.88,30.37,34.23,40.57,45.38,50.38])
plt.plot(week, weight, 'go:')
plt.xlabel("weeks")
plt.ylabel("weight")
plt.title('weight gain of a buffalo calf during the first 9 weeks')
plt.grid()
plt.show()
