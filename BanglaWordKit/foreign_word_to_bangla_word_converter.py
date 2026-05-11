import json
import os

class ForeignToBangla:
    def __init__(self, dictionary_path=None):
        if dictionary_path is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            dictionary_path = os.path.join(base_dir, 'BanglaWordKit\data', 'foreign_word_to_bangla_word_dataset.json')
            
        self.dictionary_path = dictionary_path
        self.data = self._load_data()

    def _load_data(self):
        try:
            with open(self.dictionary_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                print(f"data load complete: {self.dictionary_path})")
                return data
        except FileNotFoundError:
            print(f"not found data: {self.dictionary_path})")
            return {"level_1": [], "level_2": [], "level_3": []}
        except Exception as e:
            print(f"error: {e}")
            return {"level_1": [], "level_2": [], "level_3": []}

    def convert(self, text, level=1):
        """
        level=1: শুধু দৈনন্দিন প্রমিত শব্দ পরিবর্তন হবে।
        level=2: প্রমিত + দাপ্তরিক শব্দ পরিবর্তন হবে।
        level=3: প্রমিত + দাপ্তরিক + অতি-বিশুদ্ধ শব্দ পরিবর্তন হবে।
        """
        if not text: 
            return text
     
        rules = self.data.get('level_1', [])
        if level >= 2:
            rules += self.data.get('level_2', [])
        if level == 3:
            rules += self.data.get('level_3', [])
       
        rules = sorted(rules, key=lambda x: len(x['foreign']), reverse=True)

        converted_text = text
        for item in rules:
            converted_text = converted_text.replace(item['foreign'], item['bangla'])
        
        return converted_text