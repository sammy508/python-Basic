import re

text = "apple, banana, orange, grapes"
pattern = r","
split_result = re.split(pattern, text)

print(text)
print("result after split", split_result)