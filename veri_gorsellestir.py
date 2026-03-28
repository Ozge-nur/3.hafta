import pandas as pd
import matplotlib.pyplot as plt

def görselleştir():
    # Veriyi CSV dosyasından okuma
    try:
        df = pd.read_csv('veri.csv')
    except FileNotFoundError:
        print("Hata: 'veri.csv' dosyası bulunamadı. Lütfen önce veri_uret.py dosyasını çalıştırın.")
        return

    # Scatter plot oluşturma
    plt.figure(figsize=(10, 6))
    plt.scatter(df['haftalik_calisma_saati'], df['sinav_skoru'], alpha=0.7, color='teal', edgecolors='white', linewidth=0.5)
    
    # Eksen isimlendirmeleri ve başlık
    plt.title('Haftalık Çalışma Saati ve Sınav Skoru Arasındaki İlişki')
    plt.xlabel('Haftalık Çalışma Saati (saat)')
    plt.ylabel('Sınav Skoru (puan)')
    plt.grid(True, linestyle='--', alpha=0.5)

    # Grafiği dosya olarak kaydetme
    plt.savefig('veri_gorseli.png', dpi=300, bbox_inches='tight')
    print("Grafik 'veri_gorseli.png' olarak başarıyla kaydedildi.")

    # Grafiği ekranda gösterme
    plt.show()

if __name__ == "__main__":
    görselleştir()
