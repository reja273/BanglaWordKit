import json
import os
import re

class English_banglish_ToBangla:
    # ডাটা মেমোরিতে ক্যাশ করে রাখার জন্য
    _cached_data = None

    @staticmethod
    def _get_data_path():
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(current_dir, 'data', 'banglish_to_bangla_word_dataset.json')

    @classmethod
    def _load_data(cls):
        # যদি আগে থেকেই ডাটা লোড করা থাকে, তবে সরাসরি সেটা রিটার্ন করবে
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
            print(f"Problem to load data: {e}")
            cls._cached_data = {"level_1": [], "level_2": [], "level_3": []}
            
        return cls._cached_data

    @classmethod
    def convert(cls, text, level=1):
        """
        level=1: সাধারণ চ্যাটিং শব্দ (Hi -> শুভেচ্ছা)
        level=2: দাপ্তরিক শব্দ (Office -> দপ্তর)
        level=3: অতি-বিশুদ্ধ/প্রযুক্তিগত শব্দ (Mobile -> মুঠোফোন)
        """
        if not text:
            return text

        data = cls._load_data()

        # level wise (Cumulative selection)
        rules = data.get('level_1', [])
        if level >= 2:
            rules += data.get('level_2', [])
        if level == 3:
            rules += data.get('level_3', [])
 
        rules = sorted(rules, key=lambda x: len(x.get('english', '')), reverse=True)

        converted_text = text

        for item in rules:
            eng_word = item.get('english')
            bn_word = item.get('bangla')
            
            if not eng_word or not bn_word:
                continue
            
            # Word boundary দিয়ে রিপ্লেস করা
            if re.match(r'^[a-zA-Z0-9]+$', eng_word):
                pattern = re.compile(r'\b' + re.escape(eng_word) + r'\b', re.IGNORECASE)
                converted_text = pattern.sub(bn_word, converted_text)
            else:
                converted_text = converted_text.replace(eng_word, bn_word)

        return converted_text