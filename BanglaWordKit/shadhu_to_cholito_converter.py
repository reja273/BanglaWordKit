import json
import os

class ShadhuToCholito:
    _cached_rules = None

    @staticmethod
    def _get_data_path():
        base_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base_dir, 'data', 'shadhu_to_cholito_dataset.json')

    @classmethod
    def _load_dictionary(cls):
        if cls._cached_rules is not None:
            return cls._cached_rules

        dictionary_path = cls._get_data_path()
        try:
            if os.path.exists(dictionary_path):
                with open(dictionary_path, 'r', encoding='utf-8') as file:
                    rules = json.load(file)
                    if isinstance(rules, list):
                        cls._cached_rules = sorted(rules, key=lambda x: len(x.get('sadhu', '')), reverse=True)
                    else:
                        cls._cached_rules = []
            else:
                print(f"Warning: Dataset not found at {dictionary_path}")
                cls._cached_rules = []
        except Exception as e:
            print(f"Error: {e}")
            cls._cached_rules = []
            
        return cls._cached_rules

    @classmethod
    def convert(cls, text):
        if not text:
            return text

        rules = cls._load_dictionary()
        if not rules:
            return text

        converted_text = text
        
        for item in rules:
            sadhu_word = item.get('sadhu')
            cholito_word = item.get('cholito')
            if sadhu_word and cholito_word:
                converted_text = converted_text.replace(sadhu_word, cholito_word)

        return converted_text