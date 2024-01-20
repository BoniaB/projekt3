import numpy as np
import matplotlib.pyplot as plt

def population_model(epsilon1, gamma1, h1, epsilon2, gamma2, h2, warunki_poczatkowe):
    h = 0.001
    t = np.arange(0, 50, h)
    N1 = np.zeros(t.shape[0])
    N2 = np.zeros(t.shape[0])

    N1[0], N2[0] = warunki_poczatkowe

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

    return N1, N2


epsilon1 = 0.8
epsilon2 = 0.4
gamma1 = 1
gamma2 = 0.5
h1 = 0.3
h2 = 0.4
warunki_poczatkowe_c = (4, 8)
warunki_poczatkowe_d = (8, 8)
warunki_poczatkowe_e = (12, 8)

N1_c, N2_c = population_model(epsilon1, gamma1, h1, epsilon2, gamma2, h2, warunki_poczatkowe_c)
N1_d, N2_d = population_model(epsilon1, gamma1, h1, epsilon2, gamma2, h2, warunki_poczatkowe_d)
N1_e, N2_e = population_model(epsilon1, gamma1, h1, epsilon2, gamma2, h2, warunki_poczatkowe_e)

fig, ax = plt.subplots()
ax.plot(N1_c, N2_c, color='lightslategray', label='c')
ax.plot(N1_d, N2_d, color='chocolate', label='d')
ax.plot(N1_e, N2_e, color='tomato', label='e')
ax.scatter([4, 8, 12], [8, 8, 8], color='hotpink', label='Warunki początkowe', marker='D')
ax.set_xlabel('Liczba osobników populacji N1')
ax.set_ylabel('Liczba osobników populacji N2')
ax.set_title('Portret fazowy')
ax.legend()
ax.grid(True)  
plt.show()

#Wniosek: wszystkie krzywe zblizają się do punktu równowagi, gdzie przestaną rosnąć
#w krzywej c populacja N2 dominuje nad N1
#w krzywej d obie populacje osiągają stan równowagi i mają taką samą liczbę osobników
#w krzywej e populacja N1 dominuje nad N2



