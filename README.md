# 📝 Spell-Checking - İngilizce Yazım Denetleyici

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Tkinter-FF6F00?style=for-the-badge&logo=python&logoColor=white" alt="Tkinter"/>
  <img src="https://img.shields.io/badge/NLP-9B59B6?style=for-the-badge" alt="NLP"/>
  <img src="https://img.shields.io/badge/Text_Mining-27AE60?style=for-the-badge" alt="Text Mining"/>
</p>

<p align="center">
  <b>Metin Madenciliği teknikleri kullanarak İngilizce metinlerdeki yazım hatalarını tespit eden ve düzelten masaüstü uygulaması</b>
</p>

---

## 📋 İçindekiler

- [Proje Hakkında](#-proje-hakkında)
- [Özellikler](#-özellikler)
- [Teknik Mimari](#-teknik-mimari)
- [Algoritma Detayları](#-algoritma-detayları)
- [Sınıf ve Metot Yapısı](#-sınıf-ve-metot-yapısı)
- [Korpus Bilgisi](#-korpus-bilgisi)
- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)
- [Proje Dosya Yapısı](#-proje-dosya-yapısı)
- [Bağımlılıklar](#-bağımlılıklar)
- [Performans](#-performans)

---

## 🎯 Proje Hakkında

**Spell-Checking**, Peter Norvig'in ünlü yazım denetleme algoritmasını temel alan, Tkinter GUI framework'ü ile geliştirilmiş bir İngilizce yazım denetleyici uygulamasıdır. 

Uygulama, **Metin Madenciliği (Text Mining)** prensiplerine dayanarak çalışır:
- Büyük bir metin korpusu üzerinden kelime frekansları hesaplanır
- Kullanıcının girdiği metin ön işlemeden geçirilir
- Edit Distance algoritması ile olası düzeltmeler bulunur
- En yüksek frekanslı kelime öneri olarak sunulur

### Neden Bu Proje?

| Özellik | Açıklama |
|---------|----------|
| 📚 **Eğitimsel** | Metin madenciliği ve NLP temellerini öğrenmek için ideal |
| 🔧 **Pratik** | Gerçek dünya problemi çözen çalışan bir uygulama |
| 🎨 **Görsel** | Tkinter ile kullanıcı dostu arayüz |
| ⚡ **Performanslı** | Süre ölçümü ile optimize edilmiş algoritma |

---

## ✨ Özellikler

### Ana Özellikler

| Özellik | Açıklama |
|---------|----------|
| 🔍 **Yazım Hatası Tespiti** | Yanlış yazılmış kelimeleri sözlük tabanlı algılama |
| ✏️ **Otomatik Düzeltme** | En olası doğru kelimeyi otomatik seçme |
| 📋 **Alternatif Öneriler** | Her hatalı kelime için en fazla 5 alternatif öneri |
| 🖥️ **GUI Arayüz** | Tkinter ile modern ve kullanımı kolay arayüz |
| ⏱️ **Performans Ölçümü** | İşlem süresini konsola yazdırma |
| 📊 **Frekans Tabanlı Seçim** | Korpustaki kelime sıklığına göre önceliklendirme |

### Metin İşleme Özellikleri

- ✅ Küçük harfe dönüştürme
- ✅ Özel karakter temizleme (noktalama, sayılar vb.)
- ✅ Tokenizasyon (kelimelere ayırma)
- ✅ Kelime frekansı hesaplama

---

## 🏗️ Teknik Mimari

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           UYGULAMA MİMARİSİ                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────────────────────────┐ │
│  │   big.txt    │────▶│  Ön İşleme   │────▶│  Kelime Frekans Sözlüğü     │ │
│  │  (Korpus)    │     │              │     │     (Counter Dict)          │ │
│  └──────────────┘     └──────────────┘     └──────────────────────────────┘ │
│                                                          │                   │
│                                                          ▼                   │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────────────────────────┐ │
│  │  Kullanıcı   │────▶│  Metin       │────▶│   Edit Distance Kontrolü    │ │
│  │   Girişi     │     │  İşleme      │     │   (edits1 + edits2)         │ │
│  └──────────────┘     └──────────────┘     └──────────────────────────────┘ │
│                                                          │                   │
│                                                          ▼                   │
│                                            ┌──────────────────────────────┐ │
│                                            │   Düzeltilmiş Çıktı +        │ │
│                                            │   Alternatif Öneriler        │ │
│                                            └──────────────────────────────┘ │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Veri Akışı

```
Kullanıcı Metni → preprocess_text() → create_new_text() → correction() → candidates() → Sonuç
                       │                                        │
                       └─── tokenize() ───────────────────────▶ known()
                                                                  │
                                                         ┌───────┴───────┐
                                                         │               │
                                                     edits1()        edits2()
```

---

## 🧮 Algoritma Detayları

### 1. Ön İşleme (Preprocessing)

```python
def preprocess_text(self, text):
    text = text.lower()                 # Küçük harfe çevir
    text = re.sub(r'\W+', ' ', text)    # Alfanumerik olmayan karakterleri temizle
    return text
```

**Örnek:**
```
Giriş:  "Hello, World! How are you?"
Çıkış:  "hello world how are you"
```

### 2. Tokenizasyon

```python
def tokenize(self, text):
    tokens = text.split()    # Boşluklara göre böl
    return tokens
```

**Örnek:**
```
Giriş:  "hello world how are you"
Çıkış:  ['hello', 'world', 'how', 'are', 'you']
```

### 3. Kelime Frekansı Hesaplama

```python
def word_frequencies(self, tokens):
    frequency_dict = Counter(tokens)    # collections.Counter kullanarak
    return frequency_dict
```

**Örnek:**
```python
{'the': 80030, 'and': 38850, 'i': 38050, 'to': 35520, ...}
```

### 4. Edit Distance Algoritması

#### Edit Distance 1 (Tek Düzenleme)

Bir kelime üzerinde yapılabilecek 4 farklı işlem:

| İşlem | Açıklama | Örnek |
|-------|----------|-------|
| **Silme (Delete)** | Bir karakter çıkarma | `hello` → `helo` |
| **Yer Değiştirme (Transpose)** | İki bitişik karakteri değiştirme | `hello` → `hlelo` |
| **Değiştirme (Replace)** | Bir karakteri başka biriyle değiştirme | `hello` → `hallo` |
| **Ekleme (Insert)** | Bir karakter ekleme | `hello` → `helllo` |

```python
def edits1(self, word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    
    deletes    = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces   = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts    = [L + c + R for L, R in splits for c in letters]
    
    return set(deletes + transposes + replaces + inserts)
```

#### Edit Distance 2 (İki Düzenleme)

Edit Distance 1'deki kelimelere tekrar Edit Distance 1 uygulanır:

```python
def edits2(self, word):
    return (e2 for e1 in self.edits1(word) for e2 in self.edits1(e1))
```

### 5. Aday Seçim Stratejisi

```python
def candidates(self, word, word_dict):
    # Öncelik sırası:
    # 1. Kelime zaten doğruysa → direkt döndür
    # 2. Edit distance 1 adayları → kontrol et
    # 3. Edit distance 2 adayları → kontrol et
    # 4. Hiçbiri bulunamazsa → kelimeyi olduğu gibi döndür
    
    direct_known = self.known([word], word_dict)
    edits1_known = self.known(self.edits1(word), word_dict)
    edits2_known = self.known(self.edits2(word), word_dict)

    if direct_known:
        return direct_known
    elif edits1_known:
        return edits1_known
    elif edits2_known:
        return edits2_known
    else:
        return [word]
```

### 6. Düzeltme Seçimi

En yüksek frekanslı kelime seçilir:

```python
def correction(self, word, word_dict):
    suggested_word = max(self.candidates(word, word_dict), key=word_dict.get)
    suggestions = self.suggestions(word, word_dict)
    return suggested_word, suggestions
```

---

## 🔧 Sınıf ve Metot Yapısı

### `MetinMadenciligi` Sınıfı

Ana uygulama sınıfı, tüm işlevselliği barındırır.

#### Özellikler (Attributes)

| Özellik | Tip | Açıklama |
|---------|-----|----------|
| `master` | `tk.Tk` | Ana pencere nesnesi |
| `entry_font` | `font.Font` | Giriş alanı yazı tipi (12pt) |
| `button_font` | `font.Font` | Buton yazı tipi (10pt, bold) |
| `label_font` | `font.Font` | Etiket yazı tipi (10pt) |
| `word_dict` | `Counter` | Kelime frekans sözlüğü |
| `typ_Entry` | `tk.Entry` | Kullanıcı metin giriş alanı |
| `run_btn` | `tk.Button` | "Düzelt" butonu |
| `text_output` | `tk.Text` | Sonuç çıktı alanı |
| `corrected_words` | `list` | Düzeltilmiş kelimeler listesi |

#### Metotlar

| Metot | Parametreler | Dönüş Tipi | Açıklama |
|-------|--------------|------------|----------|
| `__init__` | `master` | `None` | Sınıf başlatıcı, GUI oluşturur |
| `Spell_Check` | - | `None` | Ana düzeltme fonksiyonu |
| `show_suggestions` | `processed_text` | `None` | Alternatif önerileri gösterir |
| `preprocess_text` | `text` | `str` | Metin ön işleme |
| `tokenize` | `text` | `list` | Kelimelere ayırma |
| `word_frequencies` | `tokens` | `Counter` | Frekans hesaplama |
| `create_new_text` | `processed_text` | `str` | Düzeltilmiş metin oluşturma |
| `correction` | `word`, `word_dict` | `tuple` | Kelime düzeltme |
| `suggestions` | `word`, `word_dict` | `list` | Öneri listesi oluşturma |
| `candidates` | `word`, `word_dict` | `set` | Aday kelimeleri bulma |
| `known` | `words`, `word_dict` | `set` | Bilinen kelimeleri filtreleme |
| `edits1` | `word` | `set` | Tek düzenleme mesafesi |
| `edits2` | `word` | `generator` | İki düzenleme mesafesi |

---

## 📚 Korpus Bilgisi

### big.txt Dosyası

Uygulama, kelime sözlüğünü oluşturmak için `big.txt` dosyasını kullanır.

| Özellik | Değer |
|---------|-------|
| **Dosya Boyutu** | ~6.6 MB |
| **Toplam Satır** | 103,600+ |
| **İçerik** | Sir Arthur Conan Doyle - Sherlock Holmes Serisi |
| **Kaynak** | Project Gutenberg |
| **Dil** | İngilizce |

### Korpus İçeriği

```
THE ADVENTURES OF SHERLOCK HOLMES
├── I.   A Scandal in Bohemia
├── II.  The Red-Headed League
├── III. A Case of Identity
├── IV.  The Boscombe Valley Mystery
├── V.   The Five Orange Pips
├── VI.  The Man with the Twisted Lip
├── VII. The Adventure of the Blue Carbuncle
├── VIII.The Adventure of the Speckled Band
├── IX.  The Adventure of the Engineer's Thumb
├── X.   The Adventure of the Noble Bachelor
├── XI.  The Adventure of the Beryl Coronet
└── XII. The Adventure of the Copper Beeches
```

Bu korpus sayesinde uygulama:
- Yaygın İngilizce kelimeleri tanır
- Kelime frekanslarını doğru hesaplar
- Düzeltme önerilerinde doğru önceliklendirme yapar

---

## 🚀 Kurulum

### Sistem Gereksinimleri

| Gereksinim | Minimum |
|------------|---------|
| **Python** | 3.8 veya üzeri |
| **İşletim Sistemi** | Windows / macOS / Linux |
| **RAM** | 512 MB |
| **Disk Alanı** | 10 MB |

### Adım Adım Kurulum

#### 1. Projeyi İndirin

```bash
# Git ile klonlayın
git clone https://github.com/kadirbeskardes/Spell-Checking.git

# Proje dizinine gidin
cd Spell-Checking
```

#### 2. Sanal Ortam Oluşturun (Önerilen)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3. Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt.txt
```

#### 4. Uygulamayı Çalıştırın

```bash
python project2.py
```

---

## 📖 Kullanım

### Temel Kullanım

1. **Uygulamayı Başlatın**: `python project2.py` komutu ile
2. **Metin Girin**: Üst kısımdaki metin kutusuna İngilizce metninizi yazın
3. **Düzelt Butonuna Tıklayın**: "Düzelt" butonuna basın
4. **Sonuçları İnceleyin**: 
   - Düzeltilmiş metin görüntülenir
   - Alternatif öneriler listelenir

### Ekran Görünümü

```
┌─────────────────────────────────────────────────────────────────┐
│                    Yazım Denetleyici                             │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────┐  ┌──────────┐          │
│  │ [Metin giriş alanı]                 │  │  Düzelt  │          │
│  └─────────────────────────────────────┘  └──────────┘          │
│                                                                  │
│  Düzeltilmiş metin:                                             │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │                                                             ││
│  │  [Düzeltilmiş metin burada görünür]                        ││
│  │                                                             ││
│  │  Alternatif Öneriler:                                       ││
│  │  'helo' için öneriler: hello, help, held, hero              ││
│  │                                                             ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
```

### Örnek Kullanım

| Giriş | Çıkış |
|-------|-------|
| `helo wrld` | `hello world` |
| `ths is a tset` | `this is a test` |
| `speling eror` | `spelling error` |
| `programing languge` | `programming language` |

---

## 📁 Proje Dosya Yapısı

```
Spell-Checking/
│
├── 📄 project2.py          # Ana uygulama dosyası
│   └── MetinMadenciligi    # Ana sınıf
│       ├── __init__()      # GUI başlatma
│       ├── Spell_Check()   # Ana düzeltme fonksiyonu
│       ├── preprocess_text()
│       ├── tokenize()
│       ├── word_frequencies()
│       ├── create_new_text()
│       ├── correction()
│       ├── suggestions()
│       ├── candidates()
│       ├── known()
│       ├── edits1()
│       └── edits2()
│
├── 📄 big.txt              # Korpus dosyası (~6.6 MB)
│   └── Sherlock Holmes     # Project Gutenberg
│
├── 📄 requirements.txt.txt # Python bağımlılıkları
│   ├── tk                  # Tkinter
│   └── spellchecker        # PySpellChecker
│
└── 📄 README.md            # Bu dosya
```

---

## 📦 Bağımlılıklar

### Kullanılan Kütüphaneler

| Kütüphane | Versiyon | Kullanım Amacı |
|-----------|----------|----------------|
| `tkinter` | Built-in | GUI arayüzü oluşturma |
| `tkinter.font` | Built-in | Özel yazı tipi tanımlama |
| `re` | Built-in | Regex ile metin işleme |
| `collections.Counter` | Built-in | Kelime frekansı hesaplama |
| `time` | Built-in | Performans ölçümü |
| `spellchecker` | External | (İmport edilmiş, aktif kullanılmıyor) |

### requirements.txt.txt İçeriği

```
tk
spellchecker
```

---

## ⚡ Performans

### Zaman Ölçümü

Uygulama, her düzeltme işleminin süresini konsola yazdırır:

```python
start_time = time.time()
# ... işlemler ...
end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed Time:", elapsed_time, "seconds")
```

### Performans Optimizasyonları

1. **Öncelikli Arama**: Önce direkt eşleşme, sonra edits1, sonra edits2
2. **Set Kullanımı**: Tekrar eden adayları engelleme
3. **Generator (edits2)**: Bellek optimizasyonu için lazy evaluation
4. **Öneri Limiti**: Maksimum 5 öneri gösterme

### Beklenen Süreler

| İşlem | Ortalama Süre |
|-------|---------------|
| Tek kelime düzeltme | < 0.1 saniye |
| 10 kelimelik metin | < 0.5 saniye |
| Başlangıç yüklemesi | 1-2 saniye |

---

## 🔬 Algoritma Karmaşıklığı

| Fonksiyon | Zaman Karmaşıklığı | Alan Karmaşıklığı |
|-----------|-------------------|-------------------|
| `preprocess_text` | O(n) | O(n) |
| `tokenize` | O(n) | O(n) |
| `word_frequencies` | O(n) | O(k) |
| `edits1` | O(n) | O(n) |
| `edits2` | O(n²) | O(1)* |
| `known` | O(m) | O(m) |
| `candidates` | O(n²) | O(n) |

*Generator kullanımı sayesinde

---

## 📝 Lisans

Bu proje eğitim amaçlı geliştirilmiştir.

---

<p align="center">
  <b>🚀 İyi Kodlamalar! 🚀</b>
</p>

<p align="center">
  Geliştirici: Kadir Beşkardeş
</p>
