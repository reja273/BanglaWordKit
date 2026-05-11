import json
import os
import re

class banglaSlangStandardizer: 
    _cached_rules = None

    @staticmethod
    def _get_data_path():
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(current_dir, 'data', 'slang_words_dataset.json')

    @classmethod
    def _load_data(cls):
        
        if cls._cached_rules is not None:
            return cls._cached_rules

        dictionary_path = cls._get_data_path()
        try:
            if os.path.exists(dictionary_path):
                with open(dictionary_path, 'r', encoding='utf-8') as f:
                    rules = json.load(f) 
                    if isinstance(rules, list):
                        cls._cached_rules = sorted(rules, key=lambda x: len(x.get('slang', '')), reverse=True)
                    else:
                        cls._cached_rules = []
            else:
                print(f"Warning: Slang dataset not found at {dictionary_path}")
                cls._cached_rules = []
        except Exception as e:
            print(f"Error loading slang data: {e}")
            cls._cached_rules = []
            
        return cls._cached_rules

    @classmethod
    def slang_standardize(cls, text):
        if not text:
            return text
            
        rules = cls._load_data()
        cleaned_text = text
        
        for item in rules:
            slang = item.get('slang')
            clean_word = item.get('clean')
            if slang and clean_word:
               
                pattern = re.compile(r'(^|\W)' + re.escape(slang) + r'($|\W)', re.UNICODE)
                cleaned_text = pattern.sub(r'\g<1>' + clean_word + r'\g<2>', cleaned_text)
                
        return cleaned_text