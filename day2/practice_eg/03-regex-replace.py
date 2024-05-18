import re

text = "the quick brown fox jumps over lazy dog"
pattern = r"brown"

replacement = "red"

new_text = re.sub(pattern, replacement, text)
print(text)
print("text after modify:", new_text)