# 🇧🇩 BanglaWordKit (v0.1.0)
**A Comprehensive NLP Toolkit for Bangla Text Normalization, Standardization, and Conversion.**

`BanglaWordKit` is a robust Python library designed to simplify Bangla Natural Language Processing (NLP) tasks. It provides ready-to-use tools for text normalization, slang removal, dialect conversion, and seamless integration between English and Bangla characters.

---

## 🚀 Key Features

- **🚫 Slang & Abuse Standardizer:** Detects and replaces offensive or rude Bangla words with polite alternatives while maintaining semantic meaning.
- **🔄 English/Banglish to Bangla:** Converts English or Banglish words within a Bangla sentence into proper Bangla script (e.g., "office" ➔ "অফিস").
- **📖 Bagdhara Converter:** Translates complex Bangla idioms (Bagdhara) into simple, understandable Bangla.
- **🏛️ Sadhu to Cholito:** Converts archaic Sadhu Bhasha into modern standard Cholito Bhasha.
- **🌍 Foreign Word Handler:** Standardizes foreign words into their common Bangla phonetic representations.
- **🧹 Advanced Normalization:** Cleans redundant spaces, punctuation, and handles multi-modal text structures.

---

## 📂 Project Structure

Based on the library Structure:

```text
BNAGLA_NLP_LIBRARY/
├── BanglaWordKit/                          # Core Package
│   ├── data/                            # JSON Datasets (Dictionaries)
│   │   ├── bagdhara_dataset.json
│   │   ├── banglish_to_bangla_word_dataset.json
│   │   ├── foreign_word_to_bangla_word_dataset.json
│   │   ├── sadhu_to_cholito_dataset.json
│   │   └── slang_words_dataset.json
│   ├── __init__.py                      # Package Entry Point
│   ├── bagdhara_converter.py            # Module 1
│   ├── bangla_slang_standardizer.py     # Module 2
│   ├── english_banglish_to_bangla_word.py # Module 3
│   ├── foreign_word_to_bangla_word_converter.py # Module 4
│   └── sadhu_to_cholito_converter.py    # Module 5
├── bangdhara_data_making/               # Data Scraping & Preprocessing Tools
├── bangla_slang_to_bangla_word_data_making/
├── ...                                  # Other Data Making Modules
├── tests/                               # Unit Testing Suite
│   ├── test_bagdhara_converter.py
│   ├── test_bangla_slang_standardizer.py
│   └── ...
├── setup.py                             # Package Configuration
└── README.md                            # Documentation


🛠 Installation
You can install the library directly from PyPI (once published):
 pip install BanglaWordKit

💻 Quick Start
1. Slang Standardization
Clean up rude text while keeping the sentiment intact:

from BanglaWordKit import banglaSlangStandardizer

std = banglaSlangStandardizer()
text = "তুই একটা গাধা, একদম বাজে বকিস না।"
result = std.slang_standardize(text)

print(result) 
Output: তুমি একটা বোকা, একদম অপ্রয়োজনীয় কথা বলছ না।

2. Engliah/Banglish to Bangla Conversion
Automatically fix English words used in Bangla sentences:

from BanglaWordKit import English_banglish_ToBangla
converter = English_banglish_ToBangla()

sample_text = "তোমার রেজাল্ট কেমন হয়েছে?"

print(f"মূল বাক্য: {sample_text}\n")

print(f"Level 1 (Casual): {converter.convert(sample_text, level=1)}")
print(f"Level 2 (Formal): {converter.convert(sample_text, level=2)}")
print(f"Level 3 (Archaic): {converter.convert(sample_text, level=3)}")

Output:
Level 1 (Casual): তোমার রেজাল্ট কেমন হয়েছে?
Level 2 (Formal): তোমার ফলাফল কেমন হয়েছে?
Level 3 (Archaic): তোমার ফলাফল কেমন হয়েছে?

3. Sadhu to Cholito Conversion

from BanglaWordKit import ShadhuToCholito
 
ShadhuToCholito_converter = ShadhuToCholito()
    
test_sentences = [
        # ১. সর্বনাম ও সাধারণ ক্রিয়াপদ টেস্ট
        "তাহারা অদ্য মাঠে খেলিতেছিল এবং আমি তাহা দেখিতেছিলাম।",
        
        # ২. বিশেষ্য, অব্যয় এবং স্বরবর্ণান্ত ধাতু (করিয়া -> করে) টেস্ট
        "বালিকাটি নিজ হস্তে গৃহ পরিষ্কার করিয়া বিশ্রাম নিতেছিল।",
        
        # ৩. অব্যয় (অদ্যাবধি, সহিত) এবং সর্বনাম টেস্ট
        "অদ্যাবধি আমি তাহাদের সহিত কোনো বিবাদে জড়াই নাই।",
        
        # ৪. ডাবল ি-কার (দিলাম) এবং ভাওয়েল শিফট (খাইল -> খেল) টেস্ট
        "আমি উহাকে একটি মৎস্য দিলাম এবং সে তাহা আনন্দে খাইল।",
        
        # ৫. একাধিক ক্রিয়াপদ এবং বিশেষ্য (ব্যাঘ্র -> বাঘ) টেস্ট
        "ব্যাঘ্র দেখিয়া সে ভয়ে কাঁপিতে কাঁপিতে দৌড়াইয়া পলাইল।"
]

for i, sentence in enumerate(test_sentences, 1):
        cholito_sentence = ShadhuToCholito_converter.convert(sentence)
        print(f"সাধু : {sentence}")
        print(f"চলিত : {cholito_sentence}")

Output:
সাধু : তাহারা অদ্য মাঠে খেলিতেছিল এবং আমি তাহা দেখিতেছিলাম।
চলিত : তারা আজ মাঠে খেলছিল এবং আমি তা দেখছিলাম।
সাধু : বালিকাটি নিজ হস্তে গৃহ পরিষ্কার করিয়া বিশ্রাম নিতেছিল।
চলিত : মেয়েটি নিজ হাতে বাড়ি পরিষ্কার করে বিশ্রাম নিছিল।
সাধু : অদ্যাবধি আমি তাহাদের সহিত কোনো বিবাদে জড়াই নাই।
চলিত : আজ পর্যন্ত আমি তাদের সাথে কোনো বিবাদে জড়াই নাই।
সাধু : আমি উহাকে একটি মৎস্য দিলাম এবং সে তাহা আনন্দে খাইল।
চলিত : আমি ওকে একটি মাছ দিলাম এবং সে তা আনন্দে খাল।
সাধু : ব্যাঘ্র দেখিয়া সে ভয়ে কাঁপিতে কাঁপিতে দৌড়াইয়া পলাইল।
চলিত : বাঘ দেখে সে ভয়ে কাঁপতে কাঁপতে দৌড়াইয়া পলাইল।

4. Foreign (not english) word to Bangla standard word
from BanglaWordKit import ForeignToBangla

converter = ForeignToBangla()

test_text = "আমি জলদি সাবান মেখে প্রস্তুত হলাম, কারণ আদালতে আমার একটি জরুরি মকদ্দমা আছে।"

print("মূল বাক্য:", test_text)
print("Level 1 (Normal):", converter.convert(test_text, level=1))
print("Level 2 (Formal):", converter.convert(test_text, level=2))
print("Level 3 (Archaic):", converter.convert(test_text, level=3))

Output:
মূল বাক্য: আমি জলদি সাবান মেখে প্রস্তুত হলাম, কারণ আদালতে আমার একটি জরুরি মকদ্দমা আছে।
Level 1 (Normal): আমি দ্রুত সাবান মেখে প্রস্তুত হলাম, কারণ আদালতে আমার একটি আবশ্যক মকদ্দমা আছে।
Level 2 (Formal): আমি দ্রুত সাবান মেখে প্রস্তুত হলাম, কারণ বিচারালয়ে আমার একটি আবশ্যক মামলা আছে।
Level 3 (Archaic): আমি দ্রুত মলিনানাশক মেখে প্রস্তুত হলাম, কারণ বিচারালয়ে আমার একটি আবশ্যক মামলা আছে।

5. Conversion of Baghara (idioms) word to standard Bangla word:
from BanglaWordKit import BanglaBagdharaConverter

bagdhara_transformar = BanglaBagdharaConverter()
text = "এইটুকু ছেলের কথা শুনে আমার তো আক্কেল গুড়ুম।"
result = bagdhara_transformar.transform(text)
print("ফলাফল:", result)

Output:
ফলাফল: এইটুকু ছেলের কথা শুনে আমার তো স্তম্ভিত।



🧪 Running Tests
To ensure everything is working correctly, run the test suite:
python -m unittest discover tests

🤝 Contributing
Contributions are welcome! If you want to add new words to the dataset or improve the logic:

1. Fork the Project.

2. Create your Feature Branch (git checkout -b feature/NewModule).

3. Commit your changes (git commit -m 'Add some NewModule').

4. Push to the Branch (git push origin feature/NewModule).

5. Open a Pull Request.

📄 License
Distributed under the MIT License. See LICENSE for more information.

✉️ Contact
Your Name - GitHub :reja273

Author(Just creator)
~Rejaul Karim


