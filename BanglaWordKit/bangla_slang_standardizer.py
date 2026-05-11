import json
import os
import re

class banglaSlangStandardizer:
    def __init__(self, dictionary_path=None):
        if dictionary_path is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            dictionary_path = os.path.join(base_dir, 'data', 'slang_words_dataset.json')
            
        self.dictionary_path = dictionary_path
        self.rules = self._load_data()

    def _load_data(self):
        try:
            if os.path.exists(self.dictionary_path):
                with open(self.dictionary_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                print(f"Slang dataset not found at {self.dictionary_path}")
                return []
        except Exception as e:
            print(f"Error loading slang data: {e}")
            return []

    def slang_standardize(self, text):
        if not text:
            return text
            
        cleaned_text = text
 
        sorted_rules = sorted(self.rules, key=lambda x: len(x['slang']), reverse=True)
        
        for item in sorted_rules:
            slang = item['slang']
            clean_word = item['clean']
            pattern = re.compile(r'(^|\W)' + re.escape(slang) + r'($|\W)', re.UNICODE)
            cleaned_text = pattern.sub(r'\g<1>' + clean_word + r'\g<2>', cleaned_text)
            
        return cleaned_text