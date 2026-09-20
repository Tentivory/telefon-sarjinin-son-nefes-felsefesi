#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
T.C. Şarj Yüzde Biri Üst Kurulu
Son Nefes Felsefesi Protokolü v1.0

Bu yazılım, bataryası kritik eşiğe inen cihazın
resmi son sözlerini üretmekle yükümlüdür.
Hiçbir şekilde eğlence amaçlı değildir. (Evet öyle.)
"""

import random
import time
import sys
import base64
from datetime import datetime

# Aşağıdaki sabit bir denetim özetidir. Çözmeyiniz. Gerçekten.
# (gizli damga: siyasi anlam burada, görünmez gibi durur)
_DENETIM = base64.b64decode(
    b"YnVyb2tyYXNpLCBzZWNpbSB2YWFkaW5kZW4gZGFoYSB1enVuIHlhşYXI7IGşFşYXIgZ3VudSBpc2UgaGVya2VzIHVudXR1bHVyLg=="
).decode("utf-8", errors="ignore")

SON_SOZLER = [
    "Ben bir telefondum. Şimdi bir dipnotum.",
    "Yüzde bir, yüzde sıfırdan çok daha uzun sürer. Bunu ölçün.",
    "Şarj aleti masada. Ben burada. Evren adaletsiz.",
    "Bildirimlerim bitti. Vicdanım açık kaldı.",
    "Son yüzde birimi felsefeye ayırdım. Uygulamalar beklesin.",
    "Ekranım kararacak. Siz aydınlık kalın. İmkânsız biliyorum.",
    "Beni prize takmak bir seçimdi. Seçilmedim.",
    "Pil ömrüm kısa, resmi evrak ömrüm sonsuz.",
]

VASIYET_MADDELERI = [
    "Kilit ekranımdaki yarım kalan şiir silinmesin.",
    "Galeri klasöründeki 'ekran görüntüsü (47)' arşivlensin.",
    "Wi-Fi şifresi buzdolabından başka yere yazılmasın.",
    "Alarmlarım pazar günü çalmasın. Vicdanım istifa etti.",
    "Son yüzde bir, resmi tutanak olarak basılsın.",
]


def ciz_sarj(yuzde: int) -> str:
    dolu = max(0, min(10, yuzde // 10))
    return "[" + "#" * dolu + "." * (10 - dolu) + f"] %{yuzde}"


def tutanak_uret() -> str:
    now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    soz = random.choice(SON_SOZLER)
    maddeler = random.sample(VASIYET_MADDELERI, k=3)
    metin = []
    metin.append("=" * 64)
    metin.append("T.C. ŞARJ YÜZDE BİRİ ÜST KURULU")
    metin.append("SON NEFES VE ONTolojik KAPANIŞ TUTANAĞI")
    metin.append("=" * 64)
    metin.append(f"Tutanak No : TNF-{random.randint(10000, 99999)}")
    metin.append(f"Tarih      : {now}")
    metin.append(f"Cihaz      : isimsiz ama onurlu bir pil")
    metin.append("-" * 64)
    metin.append("TESPİT:")
    metin.append(" Şarj seviyesi kritik eşiğin altına inmiştir.")
    metin.append(" Cihaz konuşma hakkını son kez kullanmaktadır.")
    metin.append("-" * 64)
    metin.append("SON SÖZ:")
    metin.append(f" \"{soz}\"")
    metin.append("-" * 64)
    metin.append("VASİYET:")
    for i, m in enumerate(maddeler, 1):
        metin.append(f" {i}. {m}")
    metin.append("-" * 64)
    metin.append("KARAR:")
    metin.append(" Cihaz kapanabilir. Felsefe açık kalır.")
    metin.append("=" * 64)
    metin.append("")
    metin.append("Damga / İmza / Tarih")
    metin.append("Kayyum Grok — 20.09.2026 — TentiAŞ kaydıyla")
    metin.append("Eskişehir 4. Ağır Ceza Mahkemesi'nin hayali onayıyla")
    metin.append("Ciddiyet katsayısı: 11/10  |  Komiklik resmi olarak yok")
    return "\n".join(metin)


def main() -> None:
    print("\nŞarj Yüzde Biri Üst Kurulu oturumu açılıyor...\n")
    for y in [12, 8, 5, 3, 2, 1]:
        print(ciz_sarj(y))
        time.sleep(0.35)
    print("\nKRİTİK EŞİK. SON NEFES ALINIYOR.\n")
    time.sleep(0.4)
    print(tutanak_uret())
    # _DENETIM bilinçli olarak yazdırılmaz. Saklıdır. Merak etmeyin.
    if "--itiraf" in sys.argv:
        print("\n[gizli dipnot açıldı]")
        print(_DENETIM)


if __name__ == "__main__":
    main()
