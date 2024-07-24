# Spell-Checking
Projede geliştirilen, İngilizce metinlerde yazım hatalarını tespit edip düzelten bir uygulamadır. Tkinter ile oluşturulmuş bir GUI kullanarak kullanıcıların metinlerini hızlı ve etkili bir şekilde kontrol etmelerini sağlar.

# Yazım Denetleyici (Spell Checker)

Yazım Denetleyici, Türkçe metinlerde yazım hatalarını tespit edip düzelten bir uygulamadır. Tkinter ile oluşturulmuş bir GUI kullanarak kullanıcıların metinlerini hızlı ve etkili bir şekilde kontrol etmelerini sağlar.

## Özellikler

- Metin dosyasından alınan verileri işleyerek kelime frekanslarını hesaplama.
- Girilen metindeki yazım hatalarını düzeltme.
- Alternatif öneriler sunma.

## Kurulum

1. Bu depoyu yerel makinenize klonlayın:
    ```bash
    git clone https://github.com/kadirbeskardes/spell-checker.git
    ```
2. Gerekli Python paketlerini yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

## Kullanım

1. `big.txt` dosyasını proje dizinine ekleyin. Bu dosya, yazım denetiminde kullanılacak büyük bir metin veri seti içermelidir.
2. Uygulamayı başlatın:
    ```bash
    python main.py
    ```
3. Metin giriş alanına yazım hatası olduğunu düşündüğünüz metni girin ve "Düzelt" butonuna tıklayın.
4. Düzeltilmiş metin ve alternatif öneriler metin kutusunda görüntülenecektir.

## Bağımlılıklar

- Python 3.x
- Tkinter
- collections
- re
- time
- spellchecker

## Katkıda Bulunma

1. Bu projeyi forklayın.
2. Kendi dalınızı oluşturun (`git checkout -b özellik/AmazingFeature`).
3. Değişikliklerinizi commitleyin (`git commit -m 'AmazingFeature ekledim'`).
4. Dalınıza push edin (`git push origin özellik/AmazingFeature`).
5. Bir Pull Request açın.
