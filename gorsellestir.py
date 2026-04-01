import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Veriyi oku
df = pd.read_csv('veri.csv')

# Grafik figürü oluştur
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

columns = [('gunluk_adim_sayisi', 'Günlük Adım Sayısı', 'Adım'), 
           ('yakit_kalori', 'Yakılan Kalori', 'Kalori (kcal)')]

for ax, (col, title, xlabel) in zip(axes, columns):
    data = df[col]
    
    # Histogram
    ax.hist(data, bins=30, density=True, alpha=0.6, color='steelblue', edgecolor='black')
    
    # Çan eğrisi için veriler (ortalama ve standart sapma)
    mu, std = data.mean(), data.std()
    
    xmin, xmax = ax.get_xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    
    # Çan eğrisini çiz
    ax.plot(x, p, 'k', linewidth=2, label='Normal Dağılım')
    
    # Ortalama ve Std Sapma değerlerini yazdır
    textstr = f'Ortalama: {mu:.1f}\nStd Sapma: {std:.1f}'
    props = dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.8, edgecolor='gray')
    ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=12,
            verticalalignment='top', bbox=props)
            
    # Görsel düzenlemeler
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel('Yoğunluk (Density)', fontsize=12)
    ax.legend(loc='upper right')
    ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()

# Sonucu grafik.png olarak kaydet (ve plt.show() kullanma)
plt.savefig('grafik.png', dpi=300)
print("Grafikler başarıyla 'grafik.png' olarak kaydedildi.")
