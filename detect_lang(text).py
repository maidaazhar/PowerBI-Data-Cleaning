import pandas as pd
import urllib.parse
import re

# Detect Urdu or English
# Treat null as null
def detect_lang(text):
    if not text or pd.isna(text):
        return ""
    if isinstance(text, str):
        if re.search(r'[\u0600-\u06FF]', text):
            return "Urdu"
        else:
            return "Eng"
    return ""

# Apply detection on col decoded_name
dataset["Lang"] = dataset["decoded_name"].apply(detect_lang)

output = dataset
