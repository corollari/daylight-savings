import matplotlib.pyplot as plt
from simulation import *

SAMPLES=100
latitude=np.arange(0,70)
savings=list(map(lambda x:(simulate(x, False, SAMPLES) - simulate(x, True, SAMPLES)), latitude))
plt.plot(latitude, savings)
plt.show()
