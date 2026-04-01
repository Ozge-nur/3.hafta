import numpy as np
import pandas as pd
import os

# Sabit rastgelelik için seed
np.random.seed(42)

# Parametreler
n = 600
mean_steps, std_steps = 8000, 2000
mean_cal, std_cal = 350, 80
corr = 0.75

# Kovaryans matrisi
covs = [[std_steps**2, std_steps * std_cal * corr], 
        [std_steps * std_cal * corr, std_cal**2]]

# Normal dağılımlı, 0.75 korelasyonlu veriyi üret
data = np.random.multivariate_normal([mean_steps, mean_cal], covs, n)

# Sınırlandırmalar (Kırpma) ve tiplerini ayarlama
adim = np.clip(np.round(data[:, 0]), 1000, 20000).astype(int)
kalori = np.clip(np.round(data[:, 1], 1), 50, 800)

# DataFrame oluştur
df = pd.DataFrame({
    'gunluk_adim_sayisi': adim,
    'yakit_kalori': kalori
})

# CSV olarak kaydet
df.to_csv('veri.csv', index=False)
print("Veri başarıyla 'veri.csv' dosyasına kaydedildi.")
