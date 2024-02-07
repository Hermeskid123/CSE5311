import numpy as np
import matplotlib.pyplot as plt
import time 

def f(n):
    x = 1
    y = 1
    for i in range(0, n):
        for j in range(0, n):
            x = x + 1
            y = i + j
    return y


_n  = np.arange(1, 2000, 10)
times = np.zeros(len(_n))

def benchMark():
    totalTime = [] 
    for i in range(0,len(_n)):
        start = time.time()
        f( _n[i]  )
        end = time.time()
        totalTime.append(end-start)

    return totalTime
    

times = benchMark()

plt.figure()
plt.plot(_n, times, 'o-' ,linewidth=1, label='Data')
plt.xlabel('n')
plt.ylabel('time')
plt.grid(True)

p = np.polyfit(_n, times, 2)
n_0 = 500 
lower_bound = 0.7 * np.polyval(p, _n)  
upper_bound = 1.5 * np.polyval(p, _n) 
fitted_curve = np.polyval(p, _n)
plt.plot(_n, fitted_curve, '--', linewidth=1, label='Fitted')
plt.plot(_n, lower_bound, ':', linewidth=1, label='Lower')
plt.plot(_n, upper_bound, ':', linewidth=1, label='Upper')
plt.scatter(n_0, np.polyval(p, n_0), s=150, c='green', label='n_0')


plt.legend()
plt.show()


