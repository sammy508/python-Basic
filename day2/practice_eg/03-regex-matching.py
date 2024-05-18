

import re

text = "The quick brown fox"
pattern = r"quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")


# Here's the output will be : No match
#     Here's an explanation of why this is the case:

# The re.match() function only checks for a match at the beginning of the string. In your example, the pattern r"quick" does not match the beginning of the string "The quick brown fox" because the string starts with "The", not "quick".

# If you want to find "quick" anywhere in the string, you should use re.search() instead of re.match()