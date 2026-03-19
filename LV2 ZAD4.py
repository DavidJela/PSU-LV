import numpy as np
import matplotlib.pyplot as plt

def create_checkerboard(square_size, num_squares_height, num_squares_width):
    """
    Kreira sliku sa crno-bijelim kvadratima koji se naizmjenično pojavljuju (šahovska ploča).
    
    Args:
        square_size: Veličina kvadrata u pikselima
        num_squares_height: Broj kvadrata po visini
        num_squares_width: Broj kvadrata po širini
        
    Returns:
        numpy polje sa šahovskom pločom (grayscale slika)
    """
    
    rows = []
    
    # Kreiramo red za redom
    for i in range(num_squares_height):
        row_blocks = []
        
        # Kreiramo kvadrate u retku
        for j in range(num_squares_width):
            # Određujemo je li kvadrat crn ili bijel 
            # (i + j) % 2 == 0 znači da je (i,j) na "crnom" polju (kao šahovska ploča)
            if (i + j) % 2 == 0:
                # Crni kvadrat (vrijednost 0)
                block = np.zeros((square_size, square_size), dtype=np.uint8)
            else:
                # Bijeli kvadrat (vrijednost 255)
                block = np.ones((square_size, square_size), dtype=np.uint8) * 255
            
            row_blocks.append(block)
        
        # Horizontalno slaganje redaka (hstack)
        row = np.hstack(row_blocks)
        rows.append(row)
    
    # Vertikalno slaganje redaka (vstack)
    checkerboard = np.vstack(rows)
    
    return checkerboard

# ============================================================
# KREIRANJE ŠAHOVSKE PLOČE
# ============================================================

print("=" * 60)
print("GENERIRANJE ŠAHOVSKE PLOČE 4x5")
print("=" * 60)

# Kreiramo šahovsku ploču sa 4x5 kvadrata
print("\nKreiramo šahovsku ploču 4x5...")
img = create_checkerboard(60, 4, 5)
print(f"Dimenzija: {img.shape}")

# Prikaz slike
fig, ax = plt.subplots(figsize=(10, 8))
ax.imshow(img, cmap='gray', vmin=0, vmax=255)
ax.set_title('Šahovska ploča 4x5', fontsize=14, fontweight='bold')
ax.axis('off')

plt.tight_layout()
plt.savefig('checkerboard_4x5.png', dpi=100, bbox_inches='tight')
plt.show()

print("\n" + "=" * 60)
print("Šahovska ploča je generirana!")
print("Slika spremljena u datoteku: checkerboard_4x5.png")
print("=" * 60)
