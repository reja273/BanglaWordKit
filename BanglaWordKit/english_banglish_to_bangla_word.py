import json
import os
import re

class English_banglish_ToBangla:
    def __init__(self, dictionary_path=None):
        if dictionary_path is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            dictionary_path = os.path.join(base_dir, 'BanglaWordKit\data', 'banglish_to_bangla_word_dataset.json')
            
        self.dictionary_path = dictionary_path
        self.data = self._load_data()

    def _load_data(self):
        try:
            if os.path.exists(self.dictionary_path):
                with open(self.dictionary_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                print(f"not found dataset: {self.dictionary_path}")
                return {"level_1": [], "level_2": [], "level_3": []}
        except Exception as e:
            print(f"problem to load data: {e}")
            return {"level_1": [], "level_2": [], "level_3": []}

    def convert(self, text, level=1):
        """
        level=1: সাধারণ চ্যাটিং শব্দ (Hi -> শুভেচ্ছা)
        level=2: দাপ্তরিক শব্দ (Office -> দপ্তর)
        level=3: অতি-বিশুদ্ধ/প্রযুক্তিগত শব্দ (Mobile -> মুঠোফোন)
        """
        if not text:
            return text

        # level wise (Cumulative selection)
        rules = self.data.get('level_1', [])
        if level >= 2:
            rules += self.data.get('level_2', [])
        if level == 3:
            rules += self.data.get('level_3', [])
 
        rules = sorted(rules, key=lambda x: len(x['english']), reverse=True)

        converted_text = text

        for item in rules:
            eng_word = item['english']
            bn_word = item['bangla']

            if re.match(r'^[a-zA-Z0-9]+$', eng_word):
                pattern = re.compile(r'\b' + re.escape(eng_word) + r'\b', re.IGNORECASE)
                converted_text = pattern.sub(bn_word, converted_text)
            else:
                converted_text = converted_text.replace(eng_word, bn_word)

        return converted_text