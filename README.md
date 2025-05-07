Bu proje, Selenium tabanlı web otomasyonlarını insan kullanıcı davranışlarına benzeterek daha doğal ve tespit edilemez hale getirmek için geliştirilmiştir.
Sistem, özelleştirilebilir kullanıcı profilleri kullanarak farklı davranış kalıplarını simüle eder.

Temel Özellikler:

Profil Tabanlı Davranış Modelleme:

TXT dosyalarında tanımlanmış çoklu kullanıcı profilleri

Her profil için özel hız, hata oranı ve hareket parametreleri

İnsan Benzeri Etkileşimler:

Doğal fare hareketleri (Bezier eğrileri ile)

Gerçekçi klavye kullanımı (rastgele hatalar ve düzeltmeler)

İnsan benzeri scroll davranışları

Gelişmiş Önlemler:

Bot tespit sistemlerini atlatmaya yönelik mikro hareketler

Rastgele bekleme süreleri ve davranış varyasyonları

Dinamik element bulma stratejileri

Kullanım Senaryoları
Test Otomasyonu:

Gerçek kullanıcı deneyimine yakın test senaryoları

Bot tespit sistemlerini atlayan testler

Veri Toplama:

İnsan benzeri tarama davranışlarıyla web scraping

Anti-scraping önlemlerini aşma

Eğitim ve Simülasyon:

Kullanıcı davranışı simülasyonları

UI/UX testleri için gerçekçi etkileşimler

Proje, özellikle modern bot koruma sistemlerine (Cloudflare, Distil Networks vb.) karşı etkili olacak şekilde tasarlanmıştır. 
Profil sisteminin esnek yapısı sayesinde yeni davranış kalıpları kolayca eklenebilir.

Detaylı İş Akışı:

Profil Yükleme:

[Dosya Sistemi] -> [profiles.txt] -> [ProfileManager] -> [Profil Ayarları]

Otomasyon Akışı:

[Tarayıcı Başlat] -> [Profil Seç] -> [Sayfa Yükle] -> [Element Bul] 
-> [İnsan Benzeri Hareket] -> [Etkileşim] -> [Sonuçları Kaydet]

İnsan Benzeri Hareketler:

[Fare Hareketi] -> Bezier Eğrisi Hesaplama -> Mikro Hareketler -> Tıklama
[Klavye Girişi] -> Rastgele Hız -> Hata Simülasyonu -> Düzeltme


