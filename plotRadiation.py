import matplotlib.pyplot as plt
from simulation import *

DAY=1

time=np.arange(0,24*60)
radiation=list(map(lambda x:solarRadiation(x, DAY, 40), time))
plt.plot(time, radiation, 'o')
plt.show()
