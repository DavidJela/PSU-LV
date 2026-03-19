import numpy as np
import matplotlib.pyplot as plt

# a) Učitavanje datoteke mtcars.csv
data = np.loadtxt(open("mtcars.csv", "rb"), delimiter=",", skiprows=1, usecols=(1,2,3,4,5,6))

# Raspodjela podataka u varijable
# Stupci: mpg(0), cyl(1), disp(2), hp(3), drat(4), wt(5)
mpg = data[:, 0]    # Potrošnja (mile per gallon)
cyl = data[:, 1]    # Broj cilindaraa
disp = data[:, 2]   # Displacement
hp = data[:, 3]     # Konjske snage
drat = data[:, 4]   # Rear axle ratio
wt = data[:, 5]     # Težina vozila

print("=" * 60)
print("ANALIZA AUTOMOBILA - mtcars.csv")
print("=" * 60)

# b) i c) Scatter plot: mpg vs hp sa veličinom točkica prema težini
plt.figure(figsize=(10, 6))

# Skaliranje težine za veličinu točkica (normalizacija da bude vidljiva)
sizes = (wt - wt.min()) / (wt.max() - wt.min()) * 300 + 50

scatter = plt.scatter(hp, mpg, s=sizes, alpha=0.6, c=wt, cmap='viridis', edgecolors='black', linewidth=0.5)

plt.xlabel('Konjske snage (hp)', fontsize=12)
plt.ylabel('Potrošnja - mpg (milja/galon)', fontsize=12)
plt.title('Ovisnost potrošnje automobila o konjskim snagama\n(Veličina točkice predstavlja težinu vozila)', fontsize=13)
plt.grid(True, alpha=0.3)

# Colorbar za prikaz težine
colorbar = plt.colorbar(scatter)
colorbar.set_label('Težina vozila (1000 lbs)', fontsize=11)

plt.tight_layout()
plt.savefig('mtcars_scatter.png', dpi=150)
plt.show()

print("\nGraf je spreman: mtcars_scatter.png")

# d) Min, max, srednje vrijednosti za potrošnju (mpg) - svi automobili
print("\n" + "=" * 60)
print("d) STATISTIKA POTROŠNJE (mpg) - SVI AUTOMOBILI")
print("=" * 60)

mpg_min = np.min(mpg)
mpg_max = np.max(mpg)
mpg_mean = np.mean(mpg)
mpg_median = np.median(mpg)
mpg_std = np.std(mpg)

print(f"Minimalna potrošnja (mpg): {mpg_min:.2f}")
print(f"Maksimalna potrošnja (mpg): {mpg_max:.2f}")
print(f"Srednja vrijednost (mjenjač) (mpg): {mpg_mean:.2f}")
print(f"Medijana (mpg): {mpg_median:.2f}")
print(f"Standardna devijacija: {mpg_std:.2f}")
print(f"Broj automobila: {len(mpg)}")

# e) Statistika za automobile sa 6 cilindaraa
print("\n" + "=" * 60)
print("e) STATISTIKA POTROŠNJE (mpg) - SAMO 6-CILINDRIČNI AUTOMOBILI")
print("=" * 60)

# Filtriranje podataka za automobile sa 6 cilindaraa
mask_6cyl = cyl == 6
mpg_6cyl = mpg[mask_6cyl]

if len(mpg_6cyl) > 0:
    mpg_6cyl_min = np.min(mpg_6cyl)
    mpg_6cyl_max = np.max(mpg_6cyl)
    mpg_6cyl_mean = np.mean(mpg_6cyl)
    mpg_6cyl_median = np.median(mpg_6cyl)
    mpg_6cyl_std = np.std(mpg_6cyl)
    
    print(f"Minimalna potrošnja (mpg): {mpg_6cyl_min:.2f}")
    print(f"Maksimalna potrošnja (mpg): {mpg_6cyl_max:.2f}")
    print(f"Srednja vrijednost (mjenjač) (mpg): {mpg_6cyl_mean:.2f}")
    print(f"Medijana (mpg): {mpg_6cyl_median:.2f}")
    print(f"Standardna devijacija: {mpg_6cyl_std:.2f}")
    print(f"Broj 6-cilindričnih automobila: {len(mpg_6cyl)}")
else:
    print("Nema automobila sa 6 cilindaraa!")

print("\n" + "=" * 60)
print("Analiza završena!")
print("=" * 60)
