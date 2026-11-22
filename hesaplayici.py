
# GEP1316 - Odev 3
# Cozelti Konsantrasyonu Hesaplayicisi

program_adi = "Cozelti Konsantrasyonu Hesaplayicisi"
surum = 1

print(f"{program_adi} - Surum {surum}")

cevap = input("Hesaplama yapmak ister misiniz? (E/H): ")
hesaplama_aktif = cevap.strip().lower() == "e"

if hesaplama_aktif:

    try:
        # Kullanicidan veri al ve float tipine donustur
        kutle = float(input("Cozunen madde miktari (g): "))
        hacim = float(input("Cozeltinin son hacmi (mL): "))

        # Girilen degerleri kontrol et
        gecerli = kutle >= 0 and hacim > 0

        if gecerli:
            # Konsantrasyonu hesapla
            konsantrasyon = (kutle / hacim) * 100

            # Sonucu yazdir
            print(f"Konsantrasyon: %{konsantrasyon:.2f} (w/v)")
        else:
            print("Hata: Kutle negatif olamaz ve hacim sifirdan buyuk olmalidir.")

    except ValueError:
        # Sayisal olmayan girdiler icin hata mesaji
        print("Hata: Lutfen gecerli bir sayi giriniz.")

else:
    print("Hesaplama iptal edildi.")

