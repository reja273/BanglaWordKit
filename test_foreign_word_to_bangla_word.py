from BanglaWordKit import ForeignToBangla

converter = ForeignToBangla()

test_text = "আমি জলদি সাবান মেখে প্রস্তুত হলাম, কারণ আদালতে আমার একটি জরুরি মকদ্দমা আছে।"

print("মূল বাক্য       :", test_text)
print("Level 1 (Normal):", converter.convert(test_text, level=1))
print("Level 2 (Formal):", converter.convert(test_text, level=2))
print("Level 3 (Archaic):", converter.convert(test_text, level=3))