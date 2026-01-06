# 📝 Spell-Checking - İngilizce Yazım Denetleyici

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Tkinter-FF6F00?style=for-the-badge&logo=python&logoColor=white" alt="Tkinter"/>
  <img src="https://img.shields.io/badge/NLP-9B59B6?style=for-the-badge" alt="NLP"/>
</p>

**Spell-Checking**, İngilizce metinlerde yazım hatalarını tespit edip düzelten bir uygulamadır. Tkinter ile oluşturulmuş kullanıcı dostu bir GUI arayüzü sayesinde metinleri hızlı ve etkili bir şekilde kontrol edebilirsiniz. 

## 📋 İçindekiler

- [Özellikler](#-özellikler)
- [Algoritma](#-algoritma)
- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)
- [Proje Yapısı](#-proje-yapısı)
- [Katkıda Bulunma](#-katkıda-bulunma)

## ✨ Özellikler

- 🔍 **Yazım Hatası Tespiti**: Yanlış yazılmış kelimeleri otomatik algılama
- ✏️ **Otomatik Düzeltme**: En olası doğru kelimeyi önerme
- 📋 **Alternatif Öneriler**: Her hatalı kelime için birden fazla öneri
- 🖥️ **Kullanıcı Dostu GUI**: Tkinter ile modern arayüz
- ⚡ **Hızlı İşlem**: Optimize edilmiş algoritma ile hızlı sonuç
- 📊 **Kelime Frekansı**:  Büyük korpus üzerinden eğitilmiş model

## 🧮 Algoritma

### Edit Distance (Düzenleme Mesafesi)

Uygulama, Peter Norvig'in popüler yazım denetleme algoritmasını temel alır:

1. **Edit Distance 1**: Bir düzenleme uzaklığındaki kelimeler
   - **Silme**: Bir karakter çıkarma (`hello` → `helo`)
   - **Yer Değiştirme**: İki bitişik karakteri değiştirme (`hello` → `hlelo`)
   - **Değiştirme**: Bir karakteri başka biriyle değiştirme (`hello` → `hallo`)
   - **Ekleme**: Bir karakter ekleme (`hello` → `helloo`)

2. **Edit Distance 2**: İki düzenleme uzaklığındaki kelimeler

3. **Kelime Frekansı**: En yaygın kullanılan kelimeye öncelik verme

```
┌─────────────────────────────────────────────────────────────┐
│                    Input:  "helo wrld"                       │
├─────────────────────────────────────────────────────────────┤
│  1.  Preprocessing (Ön İşleme)                               │
│     - Küçük harfe çevirme                                   │
│     - Özel karakterleri temizleme                           │
├─────────────────────────────────────────────────────────────┤
│  2. Tokenization (Kelimelere Ayırma)                        │
│     - ["helo", "wrld"]                                      │
├─────────────────────────────────────────────────────────────┤
│  3. Candidate Generation (Aday Oluşturma)                   │
│     - Edit distance 1 kelimeleri                            │
│     - Edit distance 2 kelimeleri                            │
├─────────────────────────────────────────────────────────────┤
│  4. Selection (Seçim)                                       │
│     - Korpusta bulunan adaylar                              │
│     - En yüksek frekanslı kelime                            │
├─────────────────────────────────────────────────────────────┤
│                   Output: "hello world"                     │
└─────────────────────────────────────────────────────────────┘
```

## 🚀 Kurulum

### Gereksinimler
- Python 3.8+
- Tkinter (genellikle Python ile birlikte gelir)

### Adımlar

```bash
# Repository'yi klonlayın
git clone https://github.com/kadirbeskardes/Spell-Checking.git
cd Spell-Checking

# Bağımlılıkları yükleyin
pip install -r requirements.txt

# Uygulamayı çalıştırın
python project2.py
```

## 📖 Kullanım

1. Uygulamayı başlatın
2. Metin kutusuna kontrol etmek istediğiniz İngilizce metni yazın
3. **"Düzelt"** butonuna tıklayın
4. Düzeltilmiş metin ve alternatif öneriler görüntülenecektir

### Örnek

**Giriş:**
```
Ths is a smple txt with erors
```

**Çıkış:**
```
This is a simple text with errors

Alternatif Öneriler:
'ths' için öneriler:  this, the, thus
'smple' için öneriler: simple, sample, ample
'txt' için öneriler: text, tax, next
'erors' için öneriler:  errors, eros, era
```

## 📁 Proje Yapısı

```
Spell-Checking/
├── project2.py              # Ana uygulama dosyası
├── big. txt                  # Eğitim korpusu (~6MB)
├── requirements.txt         # Python bağımlılıkları
└── README.md               # Dokümantasyon
```

## 🔧 Teknik Detaylar

### MetinMadenciligi Sınıfı

| Metod | Açıklama |
|-------|----------|
| `preprocess_text()` | Metni küçük harfe çevirir ve özel karakterleri temizler |
| `tokenize()` | Metni kelimelere ayırır |
| `word_frequencies()` | Kelime frekanslarını hesaplar |
| `edits1()` | Bir düzenleme uzaklığındaki tüm kelimeleri üretir |
| `edits2()` | İki düzenleme uzaklığındaki kelimeleri üretir |
| `known()` | Korpusta bulunan kelimeleri filtreler |
| `candidates()` | Olası doğru kelimeleri listeler |
| `correction()` | En iyi düzeltmeyi seçer |

### Performans

- **Korpus Boyutu**: ~6MB metin dosyası
- **İşlem Süresi**: Ortalama < 1 saniye (kısa metinler için)
- **Doğruluk**: %80-90 (bağlama göre değişir)

## 🤝 Katkıda Bulunma

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/Improvement`)
3. Commit edin (`git commit -m 'Add Improvement'`)
4. Push edin (`git push origin feature/Improvement`)
5. Pull Request açın

## 📚 Referanslar

- [How to Write a Spelling Corrector - Peter Norvig](https://norvig.com/spell-correct.html)
- [Natural Language Processing with Python](https://www.nltk.org/book/)

## 📄 Lisans

MIT License

---

<p align="center">
  📝 <strong>Spell-Checking</strong> - Doğru yazının gücü!
</p>
