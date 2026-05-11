import json
import os
import requests
from bs4 import BeautifulSoup

class UltimateSadhuCholitoGenerator:
    def __init__(self):
        self.dataset = [] #Pure Consonant bangla verb Roots
        self.consonant_roots = [
            # Basic Actions 
            "কর", "বল", "দেখ", "শুন", "বস", "উঠ", "চল", "লিখ", "পড়", "হাস", "কাঁদ", 
            "রাখ", "শিখ", "বুঝ", "ভাব", "মার", "ধর", "কাট", "ছাড়", "ডাক", "খেল", 
            "ঘুর", "নাচ", "আঁক", "খুঁজ", "কিন", "বেচ", "টান", "ফেল", "বাঁচ", "মর", 
            "জাগ", "হাঁট", "উড়", "ভাস", "ডুব", "জ্বল", "নিভ", "খুল", "ঢুক", "নাম", 
            "হার", "জিত", "ভাঙ", "গড়", "বাঁধ", "পাক", "গল", "জম", "সাজ", "মান", 
            "জান", "চিন", "কাঁপ", "ফুট", "হট", "সর", "নড়", "বাড়", "কম", "থাম", 
            "টিক", "ঝুল", "দুল", "চড়", "ভুল", "রাঁধ", "হাঁক", "ঢাল", "মাখ", "ছাঁট", 
            "খাট", "বাঁক", "বাজ", "লাগ", "মাগ", "হাঁপ", "ঠক", "জপ", "বক", "ছুট", 
            "লড়", "খস", "পচ", "মাজ", "লুকা", 

            # Movement & Communication
            "ফির", "দৌড়", "কাঁপ", "গর্জ", "ধমক", "হাঁক", "গিল", "কাট",

            # Physical Actions
            "মুছ", "ঘষ", "তোল", "ছোঁড়", "চাপ", "ঠেল", "চির", "পিষ", "মাড়", "ছিঁড়", 
            "নাড়", "ভিজ", "শুঁক", "তুল", "ধুঁক",

            # Social & Emotion
            "মেল", "মিশ", "মিট", "রাগ", "হাস", "কাঁদ", "ভজ",

            # Auxiliary
            "পার", "থাক", "ঘট", "রট"
        ]
        # ২. স্বরবর্ণান্ত ধাতু (Pure Vowel Roots with Shifts) যেমন: খা -> খে)
        self.vowel_roots = {
            "খা": "খে",    # খাইয়া -> খেয়ে
            "যা": "গে",    # যাইয়া -> গিয়ে/গেয়ে
            "পা": "পে",    # পাইয়া -> পেয়ে
            "দি": "দি",    # দিয়া -> দিয়ে
            "নি": "নি",    # নিয়া -> নিয়ে
            "হ": "হ",      # হইয়া -> হয়ে
            "শো": "শু",    # শুইয়া -> শুয়ে
            "ধো": "ধু",    # ধুইয়া -> ধুয়ে
            "রো": "রু",    # রুইয়া -> রুয়ে
            "গা": "গে",    # গাইয়া -> গেয়ে
            "চা": "চে",    # চাইয়া -> চেয়ে
            "বা": "বে",    # বাইয়া -> বেয়ে
            "উড়া": "উড়ি"   # উড়াইয়া -> উড়িয়ে
        }

    def scrape_online_roots(self): #bangla verb root scrapping function
        url = "https://bn.wiktionary.org/wiki/বিষয়শ্রেণী:বাংলা_ক্রিয়া"
        print("searching new verb root from internet")
        
        try:
            response = requests.get(url, timeout=15)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            new_roots = []
            for li in soup.select('#mw-pages li'):
                word = li.text.strip()
                if word.endswith('ানো'):
                    root = word[:-3]
                elif word.endswith('া'):
                    root = word[:-1]
                else:
                    root = word
                    
                if len(root) >= 1 and root not in self.consonant_roots and root not in self.vowel_roots.keys():
                    new_roots.append(root)
            
            if new_roots:
                print(f"total scraped verb root from Wikipedia: {len(new_roots)}")
                self.consonant_roots.extend(new_roots)
            else:
                print("bangla verb root not found.")
                
        except Exception as e:
            print(f"error: {e}")

    def generate_verbs(self): #কাল, পুরুষ এবং রুট নিয়ে ক্রিয়াপদ জেনারেট  
        verb_rules = [
            ("িয়া", "ে"), ("িতে", "তে"), ("িলে", "লে"), ("িয়াও", "েও"),
            ("িলাম", "লাম"), ("িলে", "লে"), ("িল", "ল"), ("িলেন", "লেন"),
            ("িব", "ব"), ("িবে", "বে"), ("িবেন", "বেন"),
            ("িতেছি", "ছি"), ("িতেছ", "ছ"), ("িতেছে", "ছে"), ("িতেছেন", "ছেন"),
            ("িতেছিলাম", "ছিলাম"), ("িতেছিলে", "ছিলে"), ("িতেছিল", "ছিল"), ("িতেছিলেন", "ছিলেন"),
            ("িয়াছি", "েছি"), ("িয়াছ", "েছ"), ("িয়াছে", "েছে"), ("িয়াছেন", "েছেন"),
            ("িয়াছিলাম", "েছিলাম"), ("িয়াছিলে", "েছিলে"), ("িয়াছিল", "েছিল"), ("িয়াছিলেন", "েছিলেন"),
            ("িতাম", "তাম"), ("িতে", "তে"), ("িত", "ত"), ("িতেন", "তেন")
        ]

        #Consonant Roots
        for root in self.consonant_roots:
            for sadhu_sfx, cholito_sfx in verb_rules:
                self.dataset.append({"sadhu": root + sadhu_sfx, "cholito": root + cholito_sfx})

        #Vowel Roots 
        for sadhu_root, cholito_root in self.vowel_roots.items():
            for sadhu_sfx, cholito_sfx in verb_rules:
                
                #shadhu
                sadhu_sfx_mod = sadhu_sfx
                if sadhu_sfx.startswith("ি"): # যদি বিভক্তি ি-কার দিয়ে শুরু হয়
                    if sadhu_root.endswith("া") or sadhu_root.endswith("ো"):
                        # 'খা' + 'িলাম' = 'খাইলাম' (ি-কার 'ই' হয়ে যাবে)
                        sadhu_sfx_mod = "ই" + sadhu_sfx[1:]
                    elif sadhu_root.endswith("ি"):
                        # 'দি' + 'িলাম' = 'দিলাম' (অতিরিক্ত ি-কার বাদ যাবে)
                        sadhu_sfx_mod = sadhu_sfx[1:]
                
                sadhu_verb = sadhu_root + sadhu_sfx_mod
                
                # চলিত রূপের  
                if cholito_sfx.startswith("ে"):
                    cholito_verb = cholito_root + "য়" + cholito_sfx
                elif sadhu_sfx == "িয়া":
                    cholito_verb = cholito_root + "য়ে"
                else:
                    base = cholito_root if sadhu_sfx.startswith("িয়") or sadhu_sfx.startswith("িত") else sadhu_root
                    cholito_verb = base + cholito_sfx
                
                #manual cleanup
                sadhu_verb = sadhu_verb.replace("খািয়া", "খাইয়া").replace("যািয়া", "যাইয়া")
                
                self.dataset.append({"sadhu": sadhu_verb, "cholito": cholito_verb})

    def add_static_words(self): 
        
        #bangla pronouns   
        pronouns = [
            ("তাঁহারা", "তাঁরা"), ("উহারা", "ওরা"), ("তাহারা", "তারা"), 
            ("আমাকে", "আমায়"), ("তোমাদিগকে", "তোমাদের"), ("তাহাদিগকে", "তাদের"),
            ("যাহারা", "যারা"), ("ইহারা", "এরা"), ("উহাদিগকে", "ওদের"), ("তাহার", "তার"),
            ("তাহাদের", "তাদের"), ("তাহাদিগের", "তাদের"), ("ইহাদের", "এদের"), ("ইহাদিগের", "এদের"),
            ("উহাদের", "ওদের"), ("যাহা", "যা"), ("তাহা", "তা"), ("উহাকে", "ওকে"),
            ("যাহাদের", "যাদের"), ("যাহাদিগের", "যাদের"), ("কাহাদের", "কাদের"), 
            ("কাহাদিগের", "কাদের"), ("কেহ", "কেউ")
        ]
        # bangla nouns 
         
        nouns = [
            ("মৎস্য", "মাছ"), ("হস্ত", "হাত"), ("মস্তক", "মাথা"), 
            ("গাত্র", "গা"), ("অক্ষি", "চোখ"), ("কর্ণ", "কান"),
            ("নাসিকা", "নাক"), ("ওষ্ঠ", "ঠোঁট"), ("কফোণি", "কনুই"), ("‌মণিবন্ধ", "কবজি"),
            ("ঘৃত", "ঘি"), ("ব্যাঘ্র", "বাঘ"), ("অজ", "ছাগল"), ("গৃহ", "বাড়ি"), 
            ("শৃগাল", "শেয়াল"), ("বদন", "মুখ"), ("বালিকা", "মেয়ে"), ("হস্তী", "হাতি"), 
            ("পক্ষী", "পাখি"), ("অগ্নি", "আগুন"), ("পুস্তক", "বই")
        ]
 
        indeclinables = [
            ("সহিত", "সাথে"), ("নচেৎ", "নাহলে"), ("অদ্যাবধি", "আজ পর্যন্ত"), 
            ("তথাপি", "তবুও"), ("যদবধি", "যে পর্যন্ত"), ("এবংবিধ", "এমন"),
            ("নতুবা", "নইলে"), ("কিংবা", "অথবা"), ("তজ্জন্য", "সে কারণে"),
            ("অদ্যাপি", "আজও"), ("প্রায়শ", "প্রায়ই"), ("প্রায়শঃ", "প্রায়ই"),
            ("তদ্বিষয়ে", "সে বিষয়ে"), ("তৎপর", "তারপর"), ("যদ্যপি", "যদিও"), 
            ("কুত্রাপি", "কোথাও"), ("ইত্যবসরে", "এই সুযোগে"), ("ইত্যবকাশে", "এই সুযোগে"), 
            ("যদর্থে", "যে কারণে"), ("অদ্য", "আজ"), ("কল্য", "কাল"), ("পরশ্ব", "পরশু")
        ]

        # ৪.Adjectives / Adverbs 
        adjectives = [
            ("ততধিক", "তার চেয়ে বেশি"), 
            ("সর্বদা", "সবসময়"), 
            ("কিঞ্চিৎ", "কিছুটা")
        ]

        # combine all catagories word
        all_static_words = pronouns + nouns + indeclinables + adjectives
        
        #use .strip() function to remove space  
        for sadhu, cholito in all_static_words:
            self.dataset.append({
                "sadhu": sadhu.strip(), 
                "cholito": cholito.strip()
            })

    def export_dataset(self, filename='shadhu_to_cholito_dataset.json'):
        #remove duplicate
        unique_data = {v['sadhu']: v['cholito'] for v in self.dataset}

        final_list = [{"sadhu": s, "cholito": c} for s, c in unique_data.items()]
        #short big word
        final_list = sorted(final_list, key=lambda x: len(x['sadhu']), reverse=True)
        
    #add id to data
        formatted_list = []
        for index, item in enumerate(final_list):
            formatted_list.append({
                "id_number": index + 1,
                "sadhu": item['sadhu'],
                "cholito": item['cholito']
            })
        
        output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'bangla_nlp', 'data')
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, filename)

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(formatted_list, f, ensure_ascii=False, indent=4)
            
        print(f"total scraped {len(formatted_list)} with 'id_number' save to this path: {output_path}")

if __name__ == "__main__":
    generator = UltimateSadhuCholitoGenerator()
    
    #scrape from Wikipedia
    generator.scrape_online_roots()
    
    print("generate bangla verb root")
    generator.generate_verbs()
    
    print("add noun, pronoun, adverb term")
    generator.add_static_words()
    
    #save
    generator.export_dataset()