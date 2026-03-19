import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Učitavanje slike tiger.png
image_path = 'tiger.png'
img = Image.open(image_path)
img_array = np.array(img)

print("=" * 60)
print("MANIPULACIJA SLIKE - tiger.png")
print("=" * 60)
print(f"Originalna dimenzija slike: {img_array.shape}")

# Kreiramo figure za prikaz svih rezultata
fig, axes = plt.subplots(3, 2, figsize=(14, 12))
fig.suptitle('Manipulacija slike "tiger.png"', fontsize=16, fontweight='bold')

# 0) Originalna slika
axes[0, 0].imshow(img_array)
axes[0, 0].set_title('Originalna slika')
axes[0, 0].axis('off')

# a) Posvijetljavanje slike (povećanje brightness-a)
print("\na) Posvijetljavanje slike...")
brightness_factor = 1.5  # povećanje intenziteta za 50%
img_bright = np.clip(img_array * brightness_factor, 0, 255).astype(np.uint8)

axes[0, 1].imshow(img_bright)
axes[0, 1].set_title('a) Osvijetljena slika (x1.5)')
axes[0, 1].axis('off')
print(f"   Brightness povećan za {brightness_factor}x")

# b) Rotacija slike za 90 stupnjeva u smjeru kazaljke na satu
print("b) Rotacija slike za 90° (kazaljka na satu)...")
img_rotated = np.rot90(img_array, k=-1)  # k=-1 za rotaciju u smjeru kazaljke

axes[1, 0].imshow(img_rotated)
axes[1, 0].set_title('b) Rotacija 90° (kazaljka)')
axes[1, 0].axis('off')
print(f"   Nova dimenzija: {img_rotated.shape}")

# c) Zrcaljenje slike (horizontalno flip)
print("c) Zrcaljenje slike...")
img_flipped = np.fliplr(img_array)  # Horizontalno zrcaljenje

axes[1, 1].imshow(img_flipped)
axes[1, 1].set_title('c) Zrcalno zrcaljenje')
axes[1, 1].axis('off')

# d) Smanjenje rezolucije (npr. 10 puta)
print("d) Smanjenje rezolucije...")
reduction_factor = 10
reduced_h = img_array.shape[0] // reduction_factor
reduced_w = img_array.shape[1] // reduction_factor

# Smanjujemo sliku
img_reduced = img_array[::reduction_factor, ::reduction_factor]
# Povećavamo nazad na originalnu veličinu za prikaz
img_reduced_upscaled = np.repeat(np.repeat(img_reduced, reduction_factor, axis=0), reduction_factor, axis=1)

# Prilagođavanje na originalnu veličinu ako ima ostatka
img_reduced_upscaled = img_reduced_upscaled[:img_array.shape[0], :img_array.shape[1]]

axes[2, 0].imshow(img_reduced_upscaled)
axes[2, 0].set_title(f'd) Rezolucija smanjena na {reduced_h}x{reduced_w} (x{reduction_factor})')
axes[2, 0].axis('off')
print(f"   Originalna rezolucija: {img_array.shape[0]}x{img_array.shape[1]}")
print(f"   Smanjena rezolucija: {reduced_h}x{reduced_w}")

# e) Prikaz samo druge četvrtine slike po širini, a cijella po visini
print("e) Druga četvrtina slike po širini...")
height = img_array.shape[0]
width = img_array.shape[1]
quarter_width = width // 4

# Kreiramo crnu sliku
img_quarter = np.zeros_like(img_array)

# Stavljamo drugu četvrtinu u isti položaj kao originalni dio
img_quarter[:, quarter_width:2*quarter_width] = img_array[:, quarter_width:2*quarter_width]

axes[2, 1].imshow(img_quarter)
axes[2, 1].set_title('e) Druga četvrtina po širini')
axes[2, 1].axis('off')
print(f"   Širina slike: {width}")
print(f"   Prikazana druga četvrtina od {quarter_width} do {2*quarter_width}")

plt.tight_layout()
plt.savefig('tiger_manipulacija.png', dpi=100, bbox_inches='tight')
plt.show()

print("\n" + "=" * 60)
print("Sve manipulacije su gotove!")
print("Rezultat spreman u datoteci: tiger_manipulacija.png")
print("=" * 60)
