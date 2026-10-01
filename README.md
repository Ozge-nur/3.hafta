# Sentetik Veri Üretimi ve Görselleştirme: Adım Sayısı ve Kalori

Bu projede 600 hayali yetişkin için günlük adım sayısı ile yakılan kalori arasındaki ilişkiyi temsil eden **sentetik bir veri seti** üretilir, CSV'ye yazılır ve grafikle görselleştirilir.

## Veri Seti Açıklaması

Bu veri seti, 600 hayali yetişkin bireyin günlük adım sayısı ile yaktığı kalori miktarı arasındaki ilişkiyi temsil etmektedir. Birinci değişken `gunluk_adim_sayisi` (birim: adım/gün), ikinci değişken ise `yakit_kalori` (birim: kcal) olup iki değişken arasında yaklaşık 0.75 korelasyon bulunmaktadır.

### Alanlar

| Alan | Tip | Birim | Açıklama |
|---|---|---|---|
| `gunluk_adim_sayisi` | Tam sayı | adım/gün | Bireyin bir günde attığı adım |
| `yakit_kalori` | Sayı | kcal | Bireyin o gün yaktığı kalori |

- Satır sayısı: 600 (başlık satırı hariç)
- Veri tamamen sentetiktir; gerçek kişi verisi içermez.

## Dosyalar

| Dosya | Görev |
|---|---|
| `veri_uret.py` | Sentetik veriyi üretir ve `veri.csv` dosyasına yazar |
| `veri.csv` | Üretilen veri seti |
| `gorsellestir.py` | Veriyi okuyup grafiği çizer |
| `grafik.png` | Üretilen grafik |

## Çalıştırma

```bash
python veri_uret.py     # veri.csv dosyasını üretir
python gorsellestir.py  # grafik.png dosyasını üretir
```
