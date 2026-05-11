
import json
import os

class ShadhuToCholito:
    def __init__(self, dictionary_path=None):
        if dictionary_path is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            dictionary_path = os.path.join(base_dir, '..', 'BanglaWordKit', 'data', 'shadhu_to_cholito_dataset.json')
            
        self.dictionary_path = dictionary_path
        self.conversion_rules = self._load_dictionary()

    def _load_dictionary(self):
        try:
            with open(self.dictionary_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                print(f"load total data: {len(data)}")
                return data
        except FileNotFoundError:
            print(f"not found data: {self.dictionary_path}")
            return []
        except Exception as e:
            print(f"error: {e}")
            return []

    def convert(self, text):
        if not text or not self.conversion_rules:
            return text

        converted_text = text

        for item in self.conversion_rules:
            sadhu_word = item['sadhu']
            cholito_word = item['cholito']
            converted_text = converted_text.replace(sadhu_word, cholito_word)

        return converted_text
