🛡️ cyberSecurity

Geliştirme aşamasında olan, modüler yapıda tasarlanmış açık kaynak bir siber güvenlik aracı seti.

Bu proje; ağ taramaları, güvenlik analizleri, sızma testi senaryoları ve raporlama işlemleri için hem Python CLI araçları, hem de Node.js tabanlı web arayüzü sunmayı hedefler.


--------------------------------------
🎯 Projenin Amacı

Modern siber güvenlik süreçlerinde ihtiyaç duyulan temel araçları tek bir yerde toplamak

Hem eğitim amaçlı hem de gerçek kullanım senaryolarında çalışabilecek bir yapı sağlamak

Açık kaynak ve katkıya açık bir proje oluşturmak

Modüler mimariye sahip, geliştirilebilir ve genişletilebilir bir altyapı oluşturmak


-------------------------------------
🧱 Kullanılan Teknolojiler
Backend / CLI

Python

Port tarama

Açık tarama mekanizmaları

Raporlama fonksiyonları

Web / API

Node.js (Express)

API uç noktaları

Web UI için backend

Statik dosya sunucusu

Frontend

HTML / JS

static ve templates klasörleri üzerinden çalışan basit arayüz

Gelecekte grafiksel raporlama ve dashboard planlanıyor


----------------------------------
🔧 Yapılacaklar (Roadmap)
Kısa Vadeli (1 Hafta)

README.md dokümantasyonunun tamamlanması

Python tarafında temel tarama modülünün tamamlanması

Node.js yapı düzenlemeleri

Orta Vadeli (1 Ay)

Web arayüzü üzerinden tarama başlatma özelliği

Tarama sonuçlarının görüntülenmesi

Port tarayıcı + zafiyet kontrol modülü eklenmesi

Uzun Vadeli (3 Ay)

JSON/CSV/PDF raporlama sistemi

Dashboard + grafiksel analiz ekranları

Katkı rehberi (CONTRIBUTING.md)

Otomatik testler

Modül plug-in sistemi

-------------------------------------

## 📁 Proje Yapısı

```bash
cyberSecurity/
│
├── scanner.py       # Python tarama motoru
├── app.js           # Node.js backend
├── package.json     # Bağımlılıklar
│
├── static/          # Frontend statik dosyalar
├── templates/       # HTML sayfalar
├── node_modules/    # NPM kütüphaneleri
│
└── README.md        # Bu dosya
```





------------------------------------

⚙️ Kurulum & Çalıştırma

Bu projeyi kendi bilgisayarında çalıştırmak için hem Python ortamı, hem de Node.js ortamı gereklidir. Aşağıdaki adımlarla projeyi sorunsuz şekilde çalıştırabilirsin.

----------------------------------

📥 1. Gerekli Bağımlılıkları Yükle
Python Gereksinimleri

Python 3.8+

pip (Python paket yöneticisi)

Node.js Gereksinimleri

Node.js 16+

npm (Node Package Manager)


---------------------------------
📦 2. Depoyu Klonla

git clone https://github.com/DemirCodes/cyberSecurity
cd cyberSecurity


--------------------------------
🐍 3. Python Modüllerini Kur

Projenin Python kısmı tarama motorunu çalıştırır.

pip install -r requirements.txt

-------------------------------
🌐 4. Node.js Bağımlılıklarını Kur

npm install

-------------------------------
▶️ 5. Projeyi Çalıştırma
Python Tarama Motoru
python3 scanner.py

Node.js Web Arayüzü
node app.js


Genelde şu adreste çalışır:

http://localhost:3000


Eğer port farklıysa terminal zaten gösterir.
