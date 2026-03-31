import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/trajectories.csv")

plt.figure(figsize=(6,6))
plt.scatter(df["x"], df["y"], s=1)

# Buraco negro (horizonte)
circle = plt.Circle((0,0), 2, color='black')
plt.gca().add_patch(circle)

plt.title("Photon Trajectories around a Black Hole")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")

plt.savefig("../images/shadow.png", dpi=300)
plt.show()
