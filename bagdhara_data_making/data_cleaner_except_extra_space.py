import json
import os
 
current_dir = os.path.dirname(os.path.abspath(__file__))
input_filename = 'scraped_bagdhara_data1.json' 
output_filename = 'bagdhra_data_with_extra_space.json'

 
input_file = os.path.join(current_dir, input_filename)
output_file = os.path.join(current_dir, output_filename)

try:
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # remove 1st 6 english garbage data
    cleaned_data = data[6:]

    #  add new serial
    for index, item in enumerate(cleaned_data, start=1):
        item['id'] = f"B_{index:04d}"

    # save new JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=4)

    print("data cleaning complete")
    print(f"1st 6 data removed then total data: {len(cleaned_data)}")
    print(f"save file: {output_file}")

except FileNotFoundError:
    print(f"\nfile not found")
except Exception as e:
    print(f"error: {e}")