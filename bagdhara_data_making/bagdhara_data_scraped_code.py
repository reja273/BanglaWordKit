import requests
from bs4 import BeautifulSoup
import json
import os
import re

urls = [
    "https://www.english-bangla.com/lessons/bagdhara/%E0%A6%AC%E0%A6%BE%E0%A6%97%E0%A6%A7%E0%A6%BE%E0%A6%B0%E0%A6%BE-%E0%A6%95%E0%A6%BE%E0%A6%95%E0%A7%87-%E0%A6%AC%E0%A6%B2%E0%A7%87",
    "https://www.english-bangla.com/lessons/bagdhara/%E0%A6%AC%E0%A6%BE%E0%A6%97%E0%A6%A7%E0%A6%BE%E0%A6%B0%E0%A6%BE-%E0%A6%AA%E0%A7%83%E0%A6%B7%E0%A7%8D%E0%A6%A0%E0%A6%BE-%E0%A7%A7",
    "https://www.english-bangla.com/lessons/bagdhara/%E0%A6%AC%E0%A6%BE%E0%A6%97%E0%A6%A7%E0%A6%BE%E0%A6%B0%E0%A6%BE-%E0%A6%AA%E0%A7%83%E0%A6%B7%E0%A7%8D%E0%A6%A0%E0%A6%BE-%E0%A7%A8",
    "https://www.english-bangla.com/lessons/bagdhara/%E0%A6%AC%E0%A6%BE%E0%A6%97%E0%A6%A7%E0%A6%BE%E0%A6%B0%E0%A6%BE-%E0%A6%AA%E0%A7%83%E0%A6%B7%E0%A7%8D%E0%A6%A0%E0%A6%BE-%E0%A7%A9",
    "https://www.english-bangla.com/lessons/bagdhara/%E0%A6%AC%E0%A6%BE%E0%A6%97%E0%A6%A7%E0%A6%BE%E0%A6%B0%E0%A6%BE-%E0%A6%AA%E0%A7%83%E0%A6%B7%E0%A7%8D%E0%A6%A0%E0%A6%BE-%E0%A7%AA"
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

bagdhara_list = []
counter = 1

for index, url in enumerate(urls, 1):
    print(f"data fetch from this {index} page")
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        #all text from website
        items = soup.find_all(['p', 'li', 'div'])
        
        for item in items:
            text = item.get_text(separator=' ').replace('\n', ' ').strip()
            
            # seperate complete sentence by |
            sentences = text.split('।')
            
            for sentence in sentences:
                sentence = sentence.strip()
                if not sentence:
                    continue
                
                # Regex: it will find bagdhara + brackeet + example if possible
                match = re.search(r'([^\(]+)\(([^)]+)\)\s*[-–—]*\s*(.*)', sentence)
                
                if match:
                    idiom_text = match.group(1).strip()
                    meaning_text = match.group(2).strip()
                    example_text = match.group(3).strip()
                    
                    # remove "যেমন:" from bagdhara
                    if "যেমন:" in idiom_text:
                        idiom_text = idiom_text.split("যেমন:")[-1].strip()
                        
                    # filter1: বাগধারার নাম সাধারণত ৬ শব্দের বেশি হয় না (অপ্রয়োজনীয় টেক্সট বাদ দেওয়ার জন্য)
                    if len(idiom_text.split()) > 6 or len(idiom_text) == 0:
                        continue
                        
                    # filter2: উদাহরণের বাক্য খুব ছোট হলে (যেমন ৫ অক্ষরের কম), সেটা হাবিজাবি টেক্স
                    if len(example_text) < 5:
                        continue
                        
                    # after each sentence add |
                    if not example_text.endswith('।'):
                        example_text += '।'
                        
                    #  generate array using (,) or (/)
                    if '/' in meaning_text:
                        meaning_final = [m.strip() for m in meaning_text.split('/')]
                    elif ',' in meaning_text:
                        meaning_final = [m.strip() for m in meaning_text.split(',')]
                    else:
                        meaning_final = meaning_text
                        
                    data = {
                        "id": f"B_{counter:04d}",
                        "idiom": idiom_text,
                        "meaning": meaning_final,
                        "example": example_text,
                        "category": "Idiom"
                    }
                    
                    #  check duplicate bangdhara
                    if not any(d['idiom'] == idiom_text for d in bagdhara_list):
                        bagdhara_list.append(data)
                        counter += 1
                
    except Exception as e:
        print(f"found a problem with this page {index} error: {e}")

#save JSON file
current_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(current_dir, 'scraped_bagdhara_data.json')

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(bagdhara_list, f, ensure_ascii=False, indent=4)

print(f"\ntotal data collect: {len(bagdhara_list)}")
print(f"Data save : {output_file}")