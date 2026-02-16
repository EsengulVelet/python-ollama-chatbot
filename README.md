🚀 Qwen ChatBot & Code Analyzer
Bu proje, PyQt6 kütüphanesi kullanılarak geliştirilmiş, yerel ağda çalışan (Ollama tabanlı) gelişmiş bir yapay zeka sohbet ve kod analizi arayüzüdür. Kullanıcıların hem günlük sohbetler yapmasına hem de karmaşık kod bloklarını detaylıca analiz etmesine olanak tanır.

✨ Özellikler
Modern Arayüz: Temiz, kullanıcı dostu ve Bootstrap renk paletinden esinlenmiş şık tasarım.

İkili Mod:

Sohbet Modu: Genel sorularınız için hızlı ve akıllı yanıtlar.

Kod Analiz Modu: Kodun işlevini, güçlü/zayıf yanlarını ve iyileştirme önerilerini sunan derinlemesine inceleme.

Dinamik Kod Biçimlendirme: Gelen yanıtlardaki kod bloklarını otomatik olarak tespit eder ve koyu tema ile okunabilirliği artırır.

Yerel Güvenlik: Verileriniz dış sunuculara gitmez, tamamen yerel makinenizde (Ollama üzerinden) çalışır.

🛠️ Kurulum
Projeyi yerelinizde çalıştırmak için aşağıdaki adımları izleyin:

1. Gereksinimler

Sisteminizde Python 3.8+ ve Ollama yüklü olmalıdır.

2. Ollama'yı Hazırlayın

Uygulamanın çalışması için qwen2:1.5b modelinin sisteminizde yüklü olduğundan emin olun:

Bash
ollama run qwen2:1.5b
3. Kütüphaneleri Yükleyin

Gerekli Python paketlerini yüklemek için terminale şu komutu yazın:

Bash
pip install PyQt6 requests
4. Çalıştırın

Bash
python main.py
📸 Ekran Görüntüleri
Özellik	Açıklama
Sohbet Paneli	Kullanıcı ve yapay zeka arasındaki mesajlaşma akışı.
Kod Analizi	Kod bloklarının özel bir bölümde analiz edilmesi ve raporlanması.
⚙️ Teknik Detaylar
Dil: Python

Arayüz Framework: PyQt6

API: Ollama (localhost:11434)

Model: Qwen2-1.5B (Varsayılan)

🤝 Katkıda Bulunma
Bu depoyu çatallayın (Fork).

Özellik dalınızı oluşturun (git checkout -b feature/yeniOzellik).

Değişikliklerinizi kaydedin (git commit -m 'Yeni özellik eklendi').

Dalınıza gönderin (git push origin feature/yeniOzellik).

Bir Çekme İsteği (Pull Request) açın.

Geliştirici: Esengül Velet