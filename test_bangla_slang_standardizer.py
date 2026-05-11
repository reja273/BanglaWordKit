from BanglaWordKit import banglaSlangStandardizer
standardizer = banglaSlangStandardizer()

text1 = "দেশের বাজেট নিয়ে বাজে কথা বলিস না, তুই একটা হারামি।"
print(standardizer.slang_standardize(text1))

text = "তুই একটা গাধা, বাজে কথা বলিস না!"
print(standardizer.slang_standardize(text))