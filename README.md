🚀 Qwen ChatBot & Code Analyzer
This project is an advanced AI chat and code analysis interface developed using the PyQt6 library, running locally (Ollama-based). It allows users to engage in daily conversations and perform detailed analysis of complex code blocks.

✨ Features
Modern UI: A clean, user-friendly, and stylish design inspired by the Bootstrap color palette.

Dual Mode:

Chat Mode: Fast and intelligent answers for your general inquiries.

Code Analysis Mode: In-depth review providing the purpose of the code, its functions, strengths/weaknesses, and improvement suggestions.

Dynamic Code Formatting: Automatically detects code blocks in responses and enhances readability with a dark theme.

Local Security: Your data never leaves your machine; it runs entirely locally via Ollama.

🛠️ Installation
Follow these steps to run the project on your local machine:

1. Prerequisites

You must have Python 3.8+ and Ollama installed on your system.

2. Prepare Ollama

Ensure the qwen2:1.5b model is installed on your system for the application to work:

Bash
ollama run qwen2:1.5b
3. Install Dependencies

Install the required Python packages using the following command:

Bash
pip install PyQt6 requests
4. Run the Application

Bash
python main.py
📸 Screenshots
Feature	Description
Chat Panel	Messaging flow between the user and the AI.
Code Analysis	Detailed analysis and reporting of code blocks in a dedicated section.
⚙️ Technical Details
Language: Python

UI Framework: PyQt6

API: Ollama (localhost:11434)

Model: Qwen2-1.5B (Default)

🤝 Contributing
Fork this repository.

Create your feature branch (git checkout -b feature/AmazingFeature).

Commit your changes (git commit -m 'Add some AmazingFeature').

Push to the branch (git push origin feature/AmazingFeature).

Open a Pull Request.

Developer: Esengül Velet

-----------TR------------

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