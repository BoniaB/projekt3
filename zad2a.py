import numpy as np
import matplotlib.pyplot as plt


epsilon1 = 1.25
epsilon2 = 0.5
gamma1 = 0.5
gamma2 = 0.2
h1 = 0.1
h2 = 0.2
h = 0.01
t = np.arange(0, 50, h)

N1 = np.zeros(t.shape[0])
N2 = np.zeros(t.shape[0])

N1[0], N2[0] = 3, 4

for i in range(1, t.shape[0]):
    dN1 = (epsilon1 - gamma1 * (h1 * N1[i-1] + h2 * N2[i-1])) * N1[i-1]
    dN2 = (epsilon2 - gamma2 * (h1 * N1[i-1] + h2 * N2[i-1])) * N2[i-1]
    k1_N1 = h * dN1
    k1_N2 = h * dN2

    k2_N1 = h * ((epsilon1 - gamma1 * (h1 * (N1[i-1] + 0.5 * k1_N1) + h2 * (N2[i-1] + 0.5 * k1_N2))) * (N1[i-1] + 0.5 * k1_N1))
    k2_N2 = h * ((epsilon2 - gamma2 * (h1 * (N1[i-1] + 0.5 * k1_N1) + h2 * (N2[i-1] + 0.5 * k1_N2))) * (N2[i-1] + 0.5 * k1_N2))

    k3_N1 = h * ((epsilon1 - gamma1 * (h1 * (N1[i-1] + 0.5 * k2_N1) + h2 * (N2[i-1] + 0.5 * k2_N2))) * (N1[i-1] + 0.5 * k2_N1))
    k3_N2 = h * ((epsilon2 - gamma2 * (h1 * (N1[i-1] + 0.5 * k2_N1) + h2 * (N2[i-1] + 0.5 * k2_N2))) * (N2[i-1] + 0.5 * k2_N2))

    k4_N1 = h * ((epsilon1 - gamma1 * (h1 * (N1[i-1] + k3_N1) + h2 * (N2[i-1] + k3_N2))) * (N1[i-1] + k3_N1))
    k4_N2 = h * ((epsilon2 - gamma2 * (h1 * (N1[i-1] + k3_N1) + h2 * (N2[i-1] + k3_N2))) * (N2[i-1] + k3_N2))

    N1[i] = N1[i-1] + (k1_N1 + 2*k2_N1 + 2*k3_N1 + k4_N1) / 6
    N2[i] = N2[i-1] + (k1_N2 + 2*k2_N2 + 2*k3_N2 + k4_N2) / 6

    N1[i] = max(N1[i], 0)
    N2[i] = max(N2[i], 0)

    if N1[i] == 0 and N2[i] == 0:
        break

plt.figure(figsize=(10, 6))
plt.plot(t, N1, color='darksalmon', label='N1')
plt.plot(t, N2, color='darkorchid', label='N2')
plt.xlabel('Czas')
plt.ylabel('Liczba osobników')
plt.legend()
plt.show()

#Wniosek: liczba osobników w populacji N1 jest większa niż w populacji N2
#po pewnym czasie w obu populacjach przestaje się zwiększać liczba osobników
