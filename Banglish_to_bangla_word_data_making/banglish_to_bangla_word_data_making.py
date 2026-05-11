import json
import os

def build_complete_english_dataset(): #English Letter, Bangla Phonetic, Pure Bangla
    master_list = {
        "level_1": [
            # Greetings & Basic Conversation
            ("hi", "হাই", "শুভেচ্ছা"), ("hello", "হ্যালো", "শুভেচ্ছা"), ("bye", "বিদায়", "বিদায়"),
            ("thanks", "থ্যাংকস", "ধন্যবাদ"), ("thank you", "থ্যাঙ্ক ইউ", "ধন্যবাদ"),
            ("sorry", "সরি", "দুঃখিত"), ("please", "প্লিজ", "দয়া করে"), ("plz", "প্লিজ", "দয়া করে"),
            ("ok", "ওকে", "ঠিক আছে"), ("okay", "ওকে", "ঠিক আছে"), ("yes", "ইয়েস", "হ্যাঁ"),
            
            # Daily Chat Words
            ("bro", "ব্রো", "ভাই"), ("brother", "ব্রাদার", "ভাই"), ("buddy", "বাডি", "বন্ধু"),
            ("friend", "ফ্রেন্ড", "বন্ধু"), ("cool", "কুল", "দারুণ"), ("awesome", "অসাম", "চমৎকার"),
            ("nice", "নাইস", "সুন্দর"), ("bad", "ব্যাড", "খারাপ"), ("happy", "হ্যাপি", "খুশি"),
            ("sad", "স্যাড", "মন খারাপ"), ("angry", "এংরি", "রাগান্বিত"), ("wait", "ওয়েট", "অপেক্ষা"),
            
            # Common Actions
            ("call", "কল", "আহ্বান"), ("check", "চেক", "যাচাই"), ("post", "পোস্ট", "প্রকাশ"),
            ("share", "শেয়ার", "ভাগ"), ("like", "লাইক", "পছন্দ"), ("comment", "কমেন্ট", "মন্তব্য"),
            ("message", "মেসেজ", "বার্তা"), ("text", "টেক্সট", "বার্তা")
        ],
        
        "level_2": [
            # Work & Study (Formal)
            ("office", "অফিস", "দপ্তর"), ("school", "স্কুল", "বিদ্যালয়"), ("college", "কলেজ", "মহাবিদ্যালয়"),
            ("university", "ইউনিভার্সিটি", "বিশ্ববিদ্যালয়"), ("job", "জব", "চাকরি"), ("work", "ওয়ার্ক", "কাজ"),
            ("meeting", "মিটিং", "সভা"), ("salary", "স্যালারি", "বেতন"), ("project", "প্রজেক্ট", "প্রকল্প"),
            ("exam", "এক্সাম", "পরীক্ষা"), ("result", "রেজাল্ট", "ফলাফল"), ("student", "স্টুডেন্ট", "শিক্ষার্থী"),
            ("teacher", "টিচার", "শিক্ষক"), ("class", "ক্লাস", "শ্রেণি")
        ],
        
        "level_3": [
            # Objects & Tech (Pure/Archaic)
            ("mobile", "মোবাইল", "মুঠোফোন"), ("phone", "ফোন", "দূরভাষ"), 
            ("computer", "কম্পিউটার", "গণনযন্ত্র"), ("laptop", "ল্যাপটপ", "বহনযোগ্য গণনযন্ত্র"),
            ("chair", "চেয়ার", "কেদারা"), ("table", "টেবিল", "মেজি"), ("bus", "বাস", "গণপরিবহন"),
            ("train", "ট্রেন", "রেলগাড়ি"), ("car", "কার", "গাড়ি"), ("room", "রুম", "কক্ষ"),
            ("bottle", "বোটল", "বোতল"), ("market", "মার্কেট", "বাজার"), ("shop", "শপ", "দোকান")
        ]
    }

    # process dictionary format
    final_dataset = {"level_1": [], "level_2": [], "level_3": []}

    for level, words in master_list.items():
        temp_list = []
        for eng, phn, target in words:
            #add English Latin script
            temp_list.append({"english": eng, "bangla": target})
            # add bangla phonetic
            temp_list.append({"english": phn, "bangla": target})
        
        # first process big word
        final_dataset[level] = sorted(temp_list, key=lambda x: len(x['english']), reverse=True)

    #save file
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'bangla_nlp\data', 'banglish_to_bangla_word_dataset.json')
    
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(final_dataset, f, ensure_ascii=False, indent=4)
    
    print(f"banglish to bangla Dataset Built Successfully!")
    print(f"Total Words Processed: {sum(len(v) for v in final_dataset.values())}")

if __name__ == "__main__":
    build_complete_english_dataset()