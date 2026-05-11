import json
import re
import os

input_file = r'bagdhara_data_making\bagdhra_data_with_extra_space.json'

# Output path (bangla_nlp/data/)
output_file = os.path.join('bangla_nlp', 'data', 'bagdhara_dataset.json')

try:
    # read input file
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # text space clean function
    def clean_text_spacing(text):
        if text and isinstance(text, str):
            # one or more space -> one space
            return re.sub(r'\s+', ' ', text).strip()
        return text

    # elean every item
    for item in data:
        if 'example' in item:
            item['example'] = clean_text_spacing(item['example'])

    #if folder not exist, create folder
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    #save new file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("finally, remove space from text")
    print(f"save new file: {output_file}")

except FileNotFoundError:
    print(f"'{input_file}' file not found")
except Exception as e:
    print(f"error: {e}")