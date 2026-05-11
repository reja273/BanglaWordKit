from BanglaWordKit import English_banglish_ToBangla
converter = English_banglish_ToBangla()

sample_text = "তোমার রেজাল্ট কেমন হয়েছে?"

print(f"মূল বাক্য: {sample_text}\n")

print(f"Level 1 (Casual): {converter.convert(sample_text, level=1)}")
print(f"Level 2 (Formal): {converter.convert(sample_text, level=2)}")
print(f"Level 3 (Archaic): {converter.convert(sample_text, level=3)}")