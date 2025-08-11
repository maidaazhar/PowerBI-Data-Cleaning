# 'dataset' comes from Power BI
import re
import pandas as pd

# Copy dataset
df = dataset.copy()

# Clean decoded_name text
def clean_name(text):
    if not isinstance(text, str):
        return text
    
    # Remove emojis
    text = re.sub(r'[\U00010000-\U0010ffff]', '', text)

    # Remove emails
    text = re.sub(r'\S+@\S+', '', text)

    # Remove numbers and dates
    text = re.sub(r'\b\d{1,4}([/-]\d{1,2}([/-]\d{2,4})?)?\b', '', text)

    # Remove question marks and random symbols
    text = re.sub(r'[?]+', '', text)
    text = re.sub(r'[_*#><:;~^=+|\\\[\]{}]+', ' ', text)

    # Remove extra punctuation (keep English & Urdu/Arabic)
    text = re.sub(r'[^\w\s\u0600-\u06FF]+', ' ', text)

    # Fix multiple spaces
    text = re.sub(r'\s+', ' ', text).strip()

    # Trim commas or dashes
    text = text.strip(",.- ")

    return text

# Apply cleaning on decoded_name
df['decoded_name'] = df['decoded_name'].apply(clean_name)

# Final dataframe
df
