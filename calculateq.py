import matplotlib.pyplot as plt
import matplotlib.colors as color
import numpy as np

heat=np.load("dataheat.npy")
pop_MAX=1.1*10**4 # 1.1万人每平方公里
pop_MIN=2000
size=len(heat)
pop_density=np.zeros(size)
for i in range(size):
    cof=heat[i]/255
    print(cof)
    pop_density[i]=pop_MIN+(pop_MAX-pop_MIN)*cof
    print(pop_density[i])
np.save("pop_density",pop_density)
