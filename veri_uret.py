import pandas as pd
import numpy as np

def veri_uret():
    # Üretilecek veri sayısı
    n = 600

    # Normal dağılımlı verilerin üretilmesi (Sabit sonuç için seed eklendi)
    np.random.seed(42)
    haftalik_calisma_saati = np.random.normal(loc=15, scale=5, size=n)
    sinav_skoru = np.random.normal(loc=70, scale=10, size=n)

    # DataFrame'e dönüştürme
    df = pd.DataFrame({
        'haftalik_calisma_saati': haftalik_calisma_saati,
        'sinav_skoru': sinav_skoru
    })

    # CSV olarak kaydetme
    df.to_csv('veri.csv', index=False)
    print("600 satırlık veri seti oluşturuldu ve 'veri.csv' olarak kaydedildi.")

if __name__ == "__main__":
    veri_uret()
