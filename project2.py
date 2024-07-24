import re
import tkinter as tk
from tkinter import font  # font modülünü ekledik
from collections import Counter
from spellchecker import SpellChecker
import time

class MetinMadenciligi:
    def __init__(self, master):
        self.master = master
        self.master.title("Yazım Denetleyici")
        self.master.geometry("600x400")  
        self.master.configure(bg='#f0f0f0')  

        self.entry_font = font.Font(size=12)  # font sınıfını doğrudan çağırmak yerine tkinter.font modülünü kullanıyoruz
        self.button_font = font.Font(size=10, weight="bold")
        self.label_font = font.Font(size=10)

        # Büyük bir metin dosyasını okuyun ve işleyin
        text_set = open("big.txt", "r").read()
        text = self.preprocess_text(text_set)
        tokens = self.tokenize(text)
        self.word_dict = self.word_frequencies(tokens)

        self.typ_Entry = tk.Entry(master, font=self.entry_font, width=40)
        self.typ_Entry.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.run_btn = tk.Button(master, text="Düzelt", command=self.Spell_Check, font=self.button_font)
        self.run_btn.grid(row=0, column=1, padx=10)

        self.text_label = tk.Label(master, text="Düzeltilmiş metin:", font=self.label_font, bg='#f0f0f0')
        self.text_label.grid(row=1, column=0, padx=10, sticky="w")

        self.text_output = tk.Text(master, height=15, width=70, font=self.entry_font)
        self.text_output.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def Spell_Check(self):
        start_time = time.time()  # Başlangıç zamanını kaydet

        text_2 = self.typ_Entry.get()

        processed_text = self.preprocess_text(text_2)
        self.corrected_words = []

        corrected_text = self.create_new_text(processed_text)

        self.text_output.delete('1.0', tk.END)
        self.text_output.insert(tk.END, corrected_text)

        self.show_suggestions(processed_text)

        end_time = time.time()  # Bitiş zamanını kaydet
        elapsed_time = end_time - start_time  # Geçen süreyi hesapla
        print("Elapsed Time:", elapsed_time, "seconds")

    def show_suggestions(self, processed_text):
        self.text_output.insert(tk.END, "\n\nAlternatif Öneriler:\n")
        for word in processed_text.split():
            suggested_word, suggestions = self.correction(word, self.word_dict)
            if suggestions and suggested_word != word and word not in self.corrected_words:  
                if len(suggestions) <= 5:
                    self.text_output.insert(tk.END, f"\n'{word}' için öneriler: {', '.join(suggestions)}")
                else:
                    sorted_suggestions = sorted(suggestions, key=lambda x: self.word_dict[x], reverse=True)[:5]
                    self.text_output.insert(tk.END, f"\n'{word}' için önerilenler: {', '.join(sorted_suggestions)}")

    def preprocess_text(self, text):
        text = text.lower()
        text = re.sub(r'\W+', ' ', text)
        return text

    def tokenize(self, text):
        tokens = text.split()
        return tokens

    def word_frequencies(self, tokens):
        frequency_dict = Counter(tokens)
        return frequency_dict

    def create_new_text(self, processed_text):
        for word in processed_text.split():
            corrected_word, _ = self.correction(word, self.word_dict)
            self.corrected_words.append(corrected_word)
        corrected_text = ' '.join(self.corrected_words)
        return corrected_text

    def correction(self, word, word_dict):
        suggested_word = max(self.candidates(word, word_dict), key=word_dict.get)
        suggestions = self.suggestions(word, word_dict)
        return suggested_word, suggestions

    def suggestions(self, word, word_dict):
        suggested_words = []
        candidates = self.candidates(word, word_dict)
        for candidate in candidates:
            if candidate != word:
                suggested_words.append(candidate)
        return suggested_words

    def candidates(self, word, word_dict):
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

    def known(self, words, word_dict):
        known_words = set()
        for word in words:
            if word in word_dict:
                known_words.add(word)
        return known_words

    def edits1(self, word):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        splits = []
        deletes = []
        transposes = []
        replaces = []
        inserts = []

        for i in range(len(word) + 1):
            splits.append((word[:i], word[i:]))

        for Left, Right in splits:
            if Right:
                deletes.append(Left + Right[1:])

            if len(Right) > 1:
                transposes.append(Left + Right[1] + Right[0] + Right[2:])

            for c in letters:
                if Right:
                    replaces.append(Left + c + Right[1:])
                inserts.append(Left + c + Right)

        return set(deletes + transposes + replaces + inserts)

    def edits2(self, word):
        return (e2 for e1 in self.edits1(word) for e2 in self.edits1(e1))

def main():
    root = tk.Tk()
    app = MetinMadenciligi(root)
    root.mainloop()

if __name__ == "__main__":
    main()
