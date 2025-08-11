# Input data comes in 'dataset'
import pandas as pd
import numpy as np
import re
from difflib import SequenceMatcher   # for fuzzy match

# ---------------------------------------------------------
# CATEGORY CODES
# 101 = Grocery
# 102 = Textile
# 103 = Medical
# 104 = Electronics
# 105 = Mobile
# 106 = Automobile
# 107 = Sports
# 108 = Kids
# 109 = Hardware
# 110 = Other
#
# TYPE CODES
# 1 = Distributor
# 2 = Manufacturer
# 3 = Wholesaler
# 4 = Retailer
# 5 = Services
# 6 = Others
# ---------------------------------------------------------

# Category keywords
category_keywords = {
    "101": [  # Grocery
        "kirana", "grocery", "store", "mart", "dukan", "shop", "جنرل", "کریانہ",
        "سبزی", "فروٹ", "fruit", "meat", "bakery", "milk", "tea", "rice", "flour"
    ],
    "102": [  # Textile
        "cloth", "kapra", "textile", "fabrics", "fashion", "boutique", "suits", 
        "tailor", "کپڑے", "سوٹ", "dress", "shoe", "kurta", "wear"
    ],
    "103": [  # Medical
        "pharmacy", "medical", "clinic", "medicine", "chemist", "doctor", "pharma",
        "دوائی", "ہسپتال", "lab", "hospital"
    ],
    "104": [  # Electronics
        "electronics", "appliance", "tv", "fridge", "laptop", "computer", 
        "solar", "fan", "light", "cable", "charger"
    ],
    "105": [  # Mobile
        "mobile", "cell", "smartphone", "android", "iphone", "sim", "repair"
    ],
    "106": [  # Automobile
        "car", "bike", "motor", "auto", "tyre", "گاڑی", "oil", "mechanic", "tractor"
    ],
    "107": [  # Sports
        "sports", "gym", "cricket", "football", "bat", "ball", "exercise"
    ],
    "108": [  # Kids
        "kids", "toy", "baby", "child", "student", "بچوں", "school", "stationary"
    ],
    "109": [  # Hardware
        "hardware", "cement", "steel", "tools", "machinery", "marble", "tent", 
        "plumbing", "construction", "paint", "tiles", "glass"
    ],
    "110": [  # Other
        "misc", "others", "personal", "loan", "self", "online", "business", 
        "property", "real estate", "travel", "tourism"
    ]
}

# Type keywords
type_keywords = {
    "1": ["distributor", "dealer", "supply", "agency", "ڈسٹریبیوٹر"],
    "2": ["manufacturer", "factory", "mill", "industry", "builders", "company"],
    "3": ["wholesale", "mandi", "grain market", "bulk"],
    "4": ["retail", "shop", "store", "mart", "bazaar", "market", "trader"],
    "5": ["service", "solutions", "repair", "studio", "consultant", "travel", 
          "hospital", "clinic", "hotel", "transport"],
    "6": ["misc", "personal", "self", "student", "expenses", "online"]
}

# Clean text column
dataset['decoded_name'] = dataset['decoded_name'].astype(str).str.lower().fillna("")

# Fuzzy check
def is_fuzzy_match(word, text, threshold=0.85):
    return SequenceMatcher(None, word, text).ratio() >= threshold

# Keyword matcher
def match_keywords(text, keyword_dict, default_code):
    clean_text = re.sub(r'[^a-z0-9ا-ےآءئؤ]+', '', text)
    for code, keywords in keyword_dict.items():
        for word in keywords:
            if word in text or word.replace(" ", "") in clean_text:
                return code
            if is_fuzzy_match(word, text):
                return code
    return default_code

# Assign category
dataset['category'] = dataset.apply(
    lambda row: match_keywords(row['decoded_name'], category_keywords, "110"),
    axis=1
)

# Assign type
dataset['type'] = dataset.apply(
    lambda row: match_keywords(row['decoded_name'], type_keywords, "6"),
    axis=1
)

# Final dataset
dataset
