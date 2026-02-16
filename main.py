import sys
import requests
import json
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QTextEdit, QPushButton, QBoxLayout, QGroupBox, QScrollArea)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import re

PENCERE_BASLAGI = "Qwen ChatBot:"
PENCERE_BOYUTU = (1000, 800)

MODEL_AYARLARI = {
    "model": "qwen2:1.5b",
    "temperature": 0.7,
    "top_p": 0.9,
    "system_prompt": "Sen Yardimci bir assistansin  ve sana sordugum sorulari duzgun bir sekilde cevaplamalisin.",
    "stream"  : False,
}

STILLER = {
    "sohbet_gecmisi": """
        QTextEdit {
            background-color: #f8f9fa;
            color: #212529;
            border: none;
            padding: 10px;
        }""",

    "kaydirma_alani": """
        QScrollArea {
            border: none;
            background-color: #f8f9fa;
        }
        QScrollBar:vertical {
            border: none;
            background: #f8f9fa;
            width: 10px;
            margin: 0px;
        }
        QScrollBar::handle:vertical {
            background: #6c757d;
            min-height: 20px;
            border-radius: 5px;
        }
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            border: none;
            background: none;
        } """,
    "kod_grubu":"""
        QGroupBox {
            border: 1px solid #dee2e6;
            border-radius: 5px;
            background-color: #f8f9fa;
            margin-top: 10px;
            padding: 15px;
        }
        QGroupBox::title {
            color: #495057;
            subcontrol-origin: margin;
            left:10px;
            padding: 0 5px;
        }""",
    "kod_girisi": """
        QTextEdit {
            background-color: #ffffff;
            color: #212529;
            border: 1px solid #ced4da;
            border-radius: 5px;
            padding: 10px;
        }""",
    "analiz_butonu":"""
        QPushButton {
            background-color: #20c997;
            color: #ffffff;
            border: none;
            border-radius: 5px;
            padding: 8px 15px;
            font-weight: bold;
        }
        QPushButton:hover {
            background-color: #1ba87e;
        }
        QPushButton:pressed {
            background-color: #168e69;
        }""",
    "giris_kapsayici": """
            QWidget {
            background-color: #f8f9fa;
            border-radius: 5px;
            padding: 5px;
        }""",
    "mesaj-girisi":"""
        QTextEdit {
            background-color: #ffffff;
            color: #212529;
            border: 1px solid #ced4da;
            border-radius: 5px;
            padding: 10px;
        }""",
    "gonder-butonu":"""
        QPushButton {
            background-color: #6f42c1;
            color: #ffffff;
            border: none;
            border-radius: 5px;
            padding: 8px 15px;
            font-weight: bold;
        }
        QPushButton:hover {
            background-color: #5e37a6;
        }
        QPushButton:pressed {
            background-color: #4c2d89;
        }"""
}

def kod_bloklarini_formatla(metin):
    kod_blok_pattern = r"```(.*?)```"
    formatli_yazi = metin

    for match in re.finditer(kod_blok_pattern, metin, re.DOTALL):
        code_block = match.group(1)
        formatli_blok = f'''
            <div style="
                background-color: #343a40;
                padding: 15px;
                overflow-x: auto;
                font-family: Arial;
                border-radius: 5px;
                white-space: pre-wrap;
                max-width: 95%;
                margin: 10px 0;
                color: #e9ecef;
                ">
                {code_block}
                </div>
            '''
        formatli_yazi = formatli_yazi.replace(match.group(0), formatli_blok)
    return f'''
            <div style="
                max-width: 95%;
                word-wrap: break-word;
                margin: 10px 0;
                ">
            {formatli_yazi}
            </div>
            '''

def modele_mesaj_gonder(mesaj):
    try:
        yanit = requests.post(
            "http://localhost:11434/api/generate",
            json={**MODEL_AYARLARI, "prompt": mesaj}
        )
        if yanit.status_code == 200:
            return True, yanit.json()["response"]
        else:
            return False, f"API HATASI: {yanit.status_code}"
    except Exception as hata:
        return False, f"Bağlanti Hatasi: {str(hata)}"
    
def mesajlasma_bilesenleri_olustur():
    kapsayici = QWidget()
    kapsayici.setStyleSheet(STILLER["giris_kapsayici"])
    layout  = QVBoxLayout(kapsayici)
    layout.setContentsMargins(10, 10, 10, 10)
    layout.setSpacing(10)

    mesaj_girisi = QTextEdit()
    mesaj_girisi.setMaximumHeight(100)
    mesaj_girisi.setFont(QFont("Arial", 11))
    mesaj_girisi.setPlaceholderText("Mesajinizi buraya yazin...")
    mesaj_girisi.setStyleSheet(STILLER["mesaj-girisi"])
    layout.addWidget(mesaj_girisi)

    gonder_butonu = QPushButton("Gönder")
    gonder_butonu.setMinimumWidth(100)
    gonder_butonu.setStyleSheet(STILLER["gonder-butonu"])
    layout.addWidget(gonder_butonu)

    return kapsayici, mesaj_girisi, gonder_butonu

def kod_analizi_bilesenleri_olustur():
    grup = QGroupBox("Kod Analizi")
    grup.setStyleSheet(STILLER["kod_grubu"])
    layout = QVBoxLayout(grup)
    layout.setContentsMargins(10, 10, 10, 10)
    layout.setSpacing(10)

    kod_girisi = QTextEdit()
    kod_girisi.setMinimumHeight(150)
    kod_girisi.setFont(QFont("Arial", 11))
    kod_girisi.setPlaceholderText("Analiz Edilecek Kodu Giriniz...")
    kod_girisi.setStyleSheet(STILLER["kod_girisi"])
    layout.addWidget(kod_girisi)
    
    analiz_butonu = QPushButton("Analiz Et")
    analiz_butonu.setStyleSheet(STILLER["analiz_butonu"])
    layout.addWidget(analiz_butonu)
    
    return grup, kod_girisi, analiz_butonu

def sohbet_gecmisi_olustur():
    kaydirma_alani = QScrollArea()
    kaydirma_alani.setWidgetResizable(True)
    kaydirma_alani.setStyleSheet(STILLER["kaydirma_alani"])

    chat_container = QWidget()
    chat_layout = QVBoxLayout(chat_container)
    chat_layout.setContentsMargins(10, 10, 10, 10)
    chat_layout.setSpacing(10)

    sohbet_gecmisi = QTextEdit()
    sohbet_gecmisi.setReadOnly(True)
    sohbet_gecmisi.setFont(QFont("Arial", 11))
    sohbet_gecmisi.setStyleSheet(STILLER["sohbet_gecmisi"])
    chat_layout.addWidget(sohbet_gecmisi)
    kaydirma_alani.setWidget(chat_container)

    return kaydirma_alani, sohbet_gecmisi

def ana_pencere_olustur():
    pencere = QMainWindow()
    pencere.setWindowTitle(PENCERE_BASLAGI)
    pencere.setMinimumSize(*PENCERE_BOYUTU)

    ana_widget = QWidget()
    pencere.setCentralWidget(ana_widget)
    yerlesim=QVBoxLayout(ana_widget)
    yerlesim.setContentsMargins(20, 20, 20, 20)
    yerlesim.setSpacing(15)

    kaydirma_alani, sohbet_gecmisi = sohbet_gecmisi_olustur()
    yerlesim.addWidget(kaydirma_alani)

    kod_grubu, kod_girisi, analiz_butonu = kod_analizi_bilesenleri_olustur()
    yerlesim.addWidget(kod_grubu)

    giris_kapsayici, mesaj_girisi, gonder_butonu = mesajlasma_bilesenleri_olustur()
    yerlesim.addWidget(giris_kapsayici)

    def mesaj_gonder():
        mesaj=mesaj_girisi.toPlainText().strip()
        if not mesaj:
            return
        sohbet_gecmisi.append(f'''
            <div style="
                max-width:95%;
                margin: 10px 0;
                padding:10px;
                background-color:#495057;
                border-radius:5px;
            ">
            <p style="color:#f8f9fa;margin:0;font-weight:bold;">Sen:</p>
            <p style="margin:5px 0 0 0;color:#e9ecef;">{mesaj}</p>
            </div>
        ''')    
        mesaj_girisi.clear()
        basari, yanit = modele_mesaj_gonder(mesaj)
        if basari:
            formatli_yanit = kod_bloklarini_formatla(yanit)
            sohbet_gecmisi.append(f'''
                <div style="
                    max-width:95%;
                    margin: 10px 0;
                    padding:10px;
                    background-color:#6f42c1;
                    border-radius:5px;
                ">
                <p style="color:#f8f9fa;margin:0;font-weight:bold;">Qwen:</p>  
                {formatli_yanit}
                </div>
            ''')
        else:
            sohbet_gecmisi.append(f"<p style='color:#dc3545;'>HATA: {yanit}</p>")
        
        sohbet_gecmisi.verticalScrollBar().setValue(sohbet_gecmisi.verticalScrollBar().maximum())

    def kod_analiz_et():
        kod = kod_girisi.toPlainText().strip()
        if not kod:
            sohbet_gecmisi.append(f"<p style='color:#dc3545;'>HATA: Kod alani boş olamaz!</p>")
            return
        
        istek=f"""
            Aşağidaki detaylari göz önünde bukundurarak kodu detayli şekilde analiz et:
            1.Kodun amaci ve işlevi nedir?
            2.Kullanilan önemli fonksiyonlar ve siniflar nelerdir?
            3.Kodun güçlü ve zayif yönleri nelerdir?
            4.Varsa iyileştirme önerilerin nelerdir?
            Kod:
            ```
            {kod}
            ```
        """
        basari, yanit = modele_mesaj_gonder(istek)
        if basari:
            formatli_yanit = kod_bloklarini_formatla(yanit)
            sohbet_gecmisi.append(f'''
                <div style="max-width:95%; margin: 10px 0;">
                    <p style="color:#212529;font-weight:bold;">Analiz Edilen Kod:</p>
                    <div style="background-color:#343a40; padding:15px; border-radius:5px; font-family:Arial; white-space:pre-wrap; overflow-x:auto; color:#e9ecef;">{kod}</div>
                    <p style="color:#212529;font-weight:bold;margin-top:15px;">Kod Analizi:</p>
                    {formatli_yanit}
                </div>            
        ''')
        else:
            sohbet_gecmisi.append(f"<p style='color:#dc3545;'>HATA: {yanit}</p>")
    gonder_butonu.clicked.connect(mesaj_gonder)
    analiz_butonu.clicked.connect(kod_analiz_et)

    return pencere
def main():
    uygulama = QApplication(sys.argv)
    pencere = ana_pencere_olustur()
    pencere.show()
    sys.exit(uygulama.exec())

if __name__ == "__main__":
    main()