import re
import pandas as pd

# Copy dataset
df = dataset.copy()

# Clean address text
def clean_address(text):
    if isinstance(text, str):
        # Remove question marks
        text = re.sub(r'[?]+', '', text)

        # Remove gibberish (?? etc.)
        text = re.sub(r'(?:\s*[?]{2,}\s*)+', ' ', text)

        # Fix spaces
        text = re.sub(r'\s+', ' ', text).strip()

        # Trim commas
        text = text.strip(", ")

        return text
    return text

# Apply cleaning on decoded_address_line
df['decoded_address_line'] = df['decoded_address_line'].apply(clean_address)

# Final dataframe
df
