import pandas as pd
import urllib.parse

df = dataset.copy()

def decode_urdu(text):
    if isinstance(text, str):
        return urllib.parse.unquote(text).replace('+', ' ')
    return text

# Apply the function to the 'name' column - Change the column names here
df['decoded_name'] = df['name'].apply(decode_urdu)

df

#simply paste the code on Transform - Python Script to run on Data 