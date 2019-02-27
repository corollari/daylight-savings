import matplotlib.pyplot as plt
from simulation import *

DAY=1

time=np.arange(0,24*60)
radi=list(map(lambda x:solarRadiation(x, DAY, LATITUDE), time))
plt.plot(time, radi, 'o')
plt.show()
