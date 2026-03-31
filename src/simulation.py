import numpy as np
import pandas as pd

# Parâmetros simples
M = 1  # massa do buraco negro
n_points = 2000

# Equação simplificada de trajetória (toy model)
def photon_trajectory(r0, phi0):
    phi = np.linspace(0, 10, n_points)
    r = r0 / (1 + 0.1 * np.sin(phi))  # perturbação
    x = r * np.cos(phi + phi0)
    y = r * np.sin(phi + phi0)
    return x, y

data = []

for i in range(10):
    x, y = photon_trajectory(r0=5 + i*0.2, phi0=i)
    for xi, yi in zip(x, y):
        data.append([xi, yi])

df = pd.DataFrame(data, columns=["x", "y"])
df.to_csv("../data/trajectories.csv", index=False)

print("Data saved.")
