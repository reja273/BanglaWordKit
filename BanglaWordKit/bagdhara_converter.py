import json
import re
import unicodedata
import os

class BanglaBagdharaConverter:
    def __init__(self, dataset_path=None):
        if dataset_path is None:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            dataset_path = os.path.join(current_dir, 'data', 'bagdhara_dataset.json')

        try:
            with open(dataset_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
           
            cleaned_data = []
            for item in data:
           
                raw_idiom = str(item['idiom']).strip()
                clean_idiom = unicodedata.normalize('NFC', raw_idiom).replace('\u200c', '').replace('\u200d', '')
                
       
                raw_meaning = item['meaning'][0] if isinstance(item['meaning'], list) else item['meaning']
                clean_meaning = unicodedata.normalize('NFC', str(raw_meaning).strip())
                
          
                if clean_idiom and clean_meaning:
                    cleaned_data.append({
                        'idiom': clean_idiom,
                        'meaning': clean_meaning
                    })

            self.bagdharas = sorted(cleaned_data, key=lambda x: len(x['idiom']), reverse=True)
                
        except Exception as e:
            print(f"problem with module: {e}")
            self.bagdharas = []

    def transform(self, text):
        if not self.bagdharas:
            return text
        
        normalized_text = unicodedata.normalize('NFC', text).replace('\u200c', '').replace('\u200d', '')
        transformed_text = re.sub(r'\s+', ' ', normalized_text).strip()

        for item in self.bagdharas:
            idiom = item['idiom']
            meaning = item['meaning']
            
            # Word Boundary (\b) এর বদলে স্পেস বা বিভক্তি চেক করা
            pattern = re.escape(idiom) + r'(ে|র|ের|কে|তে|য়|টি|টা)?'
            replacement = lambda match: meaning + (match.group(1) if match.group(1) else "")
            
            transformed_text = re.sub(pattern, replacement, transformed_text)

        return transformed_text