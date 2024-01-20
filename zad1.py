import numpy as np
import matplotlib.pyplot as plt

K = 100000
r = 0.4
t0 = 75
x0 = 10
lambda_ = r
dt = 0.1
t_max = 150

t_values = [t0]
x_gompertz_wartosci = [x0]
x_verhulst_wartosci = [x0]

for t in np.arange(t0, t_max, dt):
    dx_gompertz = r * x_gompertz_wartosci[-1] * np.log(K / x_gompertz_wartosci[-1])
    x_gompertz_wartosci.append(x_gompertz_wartosci[-1] + dx_gompertz * dt)
    
    dx_verhulst = lambda_ * x_verhulst_wartosci[-1] * (1 - x_verhulst_wartosci[-1] / K)
    x_verhulst_wartosci.append(x_verhulst_wartosci[-1] + dx_verhulst * dt)
    
    t_values.append(t + dt)


plt.figure(figsize=(10, 6))

plt.plot(t_values, x_gompertz_wartosci, color='cornflowerblue', label='Model Gompertza')
plt.plot(t_values, x_verhulst_wartosci, color='firebrick', label=' Model Verhulsta')

plt.xlabel('Czas')
plt.ylabel('Rozmiar guza')
plt.title('Porównanie modelu Gompertza i Verhulsta')
plt.legend()
plt.show()
