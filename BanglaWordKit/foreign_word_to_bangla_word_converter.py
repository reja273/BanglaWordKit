import json
import os

class ForeignToBangla:
     
    _cached_data = None

    @staticmethod
    def _get_data_path():
        current_dir = os.path.dirname(os.path.abspath(__file__)) 
        return os.path.join(current_dir, 'data', 'foreign_word_to_bangla_word_dataset.json')

    @classmethod
    def _load_data(cls):
       
        if cls._cached_data is not None:
            return cls._cached_data

        dictionary_path = cls._get_data_path()
        try:
            if os.path.exists(dictionary_path):
                with open(dictionary_path, 'r', encoding='utf-8') as f:
                    cls._cached_data = json.load(f)
            else:
                print(f"Warning: Dataset not found at {dictionary_path}")
                cls._cached_data = {"level_1": [], "level_2": [], "level_3": []}
        except Exception as e:
            print(f"Error loading data: {e}")
            cls._cached_data = {"level_1": [], "level_2": [], "level_3": []}
            
        return cls._cached_data

    @classmethod
    def convert(cls, text, level=1):
        """
        level=1: শুধু দৈনন্দিন প্রমিত শব্দ পরিবর্তন হবে।
        level=2: প্রমিত + দাপ্তরিক শব্দ পরিবর্তন হবে।
        level=3: প্রমিত + দাপ্তরিক + অতি-বিশুদ্ধ শব্দ পরিবর্তন হবে।
        """
        if not text: 
            return text
        
        data = cls._load_data()
     
      
        rules = data.get('level_1', [])
        if level >= 2:
            rules += data.get('level_2', [])
        if level == 3:
            rules += data.get('level_3', [])
        
       
        rules = sorted(rules, key=lambda x: len(x.get('foreign', '')), reverse=True)

        converted_text = text
        for item in rules:
            foreign_word = item.get('foreign')
            bangla_word = item.get('bangla')
            
            if foreign_word and bangla_word:
                converted_text = converted_text.replace(foreign_word, bangla_word)
        
        return converted_text