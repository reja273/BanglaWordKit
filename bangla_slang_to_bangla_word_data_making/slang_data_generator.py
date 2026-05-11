import json
import os

def build_pure_bangla_slang_dataset():
    slang_list = [
        # Anger/Rude
        ("রাগে আগুন", "খুব রাগান্বিত"), ("ঝাড় দিস", "বকা দাও"), ("ধুর", "উফ"),
        ("চুপ কর", "চুপ থাকো"), ("চুপ থাক", "একটু চুপ থাকো"), ("বাজে বকিস", "অপ্রয়োজনীয় কথা বলছ"),
        ("প্যাঁচাল পারিস", "অতিরিক্ত কথা বলছ"), ("ফালতু কথা", "অপ্রাসঙ্গিক কথা"), ("ফালতু", "অপ্রয়োজনীয়"),
        ("আজাইরা", "অপ্রয়োজনীয়"), ("ঢং করিস", "অভিনয় করছ"), ("নাটক করিস", "অতিরিক্ত নাটকীয় আচরণ করছ"),
        
        # Insult/Bad Sound
        ("গাধা", "বোকা"), ("বোকাচোদা", "খুব বোকা"), ("চোদনা", "অসভ্য ব্যক্তি"), 
        ("হারামি", "অসৎ ব্যক্তি"), ("বাটপার", "প্রতারক"), ("বেইমান", "বিশ্বাসঘাতক"), 
        ("লুচ্চা", "অসভ্য"), ("বাজে লোক", "খারাপ মানুষ"), ("নোংরা", "অপরিচ্ছন্ন"), 
        ("ঘেন্না লাগে", "অপছন্দ লাগে"),

        # Dismissive & Emotions
        ("দূর হ", "এখন যাও"), ("চলে যা", "এখন যাও"), ("দূর ভাগ", "সরে যাও"),
        ("ঝামেলা করিস না", "সমস্যা তৈরি কোরো না"), ("মুড অফ", "মন খারাপ"), 
        ("ভেঙে গেছি", "খুব কষ্ট পেয়েছি"), ("মরতে ইচ্ছা করে", "খুব হতাশ লাগছে"),
        ("জীবন শেষ", "খুব হতাশাজনক অবস্থা"), ("মাথা নষ্ট", "খুব বিরক্ত লাগছে"),
        ("পাগল হয়ে গেছি", "খুব বিভ্রান্ত লাগছে"), ("সহ্য হয় না", "খুব বিরক্তিকর লাগছে"),
        
        # Mocking & Relations
        ("বাহ কি বুদ্ধি!", "ভালো চেষ্টা"), ("বড় জ্ঞানী", "নিজেকে বেশি জ্ঞানী ভাবছ"),
        ("ওস্তাদ হয়ে গেছিস", "নিজেকে বেশি দক্ষ ভাবছ"), ("এই শোন", "শুনো"), 
        ("ওই", "এই যে"), ("তুই", "তুমি"), ("জঘন্য", "খুব খারাপ")
    ]

    # 1st priority to big size word
    slang_list = sorted(slang_list, key=lambda x: len(x[0]), reverse=True)
    
    formatted_data = [{"slang": s, "clean": c} for s, c in slang_list]

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'bangla_nlp\data', 'slang_words_dataset.json')
    
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(formatted_data, f, ensure_ascii=False, indent=4)
    
    print(f"successfully generate bangla slang word data: {file_path}")

if __name__ == "__main__":
    build_pure_bangla_slang_dataset()