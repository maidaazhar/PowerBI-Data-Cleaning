# 'dataset' comes from Power BI
import pandas as pd
import re

# Provinces list for cleaning/reordering
provinces = [
    "Punjab", "Sindh", "Balochistan", "Khyber Pakhtunkhwa",
    "Gilgit-Baltistan", "Azad Kashmir", "FATA"
]

# Clean and standardize address strings
def clean_address(text):
    # Handle None or NaN
    if text is None or (isinstance(text, float) and pd.isna(text)):
        return None
    # Convert non-string to string
    if not isinstance(text, str):
        return str(text)

    # Remove "Unnamed Road"
    text = re.sub(r"\bUnnamed Road\b", "", text, flags=re.IGNORECASE)

    # Remove Google Plus Codes
    text = re.sub(r"\b[A-Z0-9]{3,5}[ +]?[A-Z0-9]{2,4}\b", "", text)

    # Replace underscores
    text = text.replace("_", " ")

    # Clean punctuation and spaces
    text = re.sub(r"[;,]{2,}", ",", text)
    text = re.sub(r",\s*,+", ",", text)
    text = re.sub(r"\s{2,}", " ", text).strip(" ,;")

    # Drop junk values (random numbers/words)
    if re.fullmatch(r"[0-9]+", text) or re.fullmatch(r"[a-zA-Z]+", text):
        return None
    if len(text.split()) <= 2 and not any(p in text for p in provinces):
        return None

    # Remove leading numbers
    text = re.sub(r"^\d+\s*,?\s*", "", text)

    # Split into parts
    parts = [p.strip() for p in text.split(",") if p.strip()]

    # Fix province stuck with city
    split_parts = []
    for p in parts:
        matched = False
        for prov in provinces:
            if prov in p and p != prov:
                city = p.replace(prov, "").strip()
                if city:
                    split_parts.append(city)
                split_parts.append(prov)
                matched = True
                break
        if not matched:
            split_parts.append(p)

    # Remove duplicates, keep order
    seen = set()
    unique_parts = []
    for p in split_parts:
        if p not in seen:
            seen.add(p)
            unique_parts.append(p)

    # Reorder → [city, province, Pakistan]
    provs_found = [p for p in unique_parts if p in provinces]
    others = [p for p in unique_parts if p not in provinces and p.lower() != "pakistan"]
    has_pakistan = any(p.lower() == "pakistan" for p in unique_parts)

    final_parts = others
    if provs_found:
        final_parts += provs_found
    if has_pakistan:
        final_parts.append("Pakistan")

    # Fix text case (title, keep acronyms)
    final_parts = [p if p.isupper() else p.title() for p in final_parts]

    # Join back
    final = ", ".join(final_parts).strip(" ,;")
    return final if final else None


# Apply cleaning to dataset copy
df = dataset.copy()

# Clean decoded_address if present
if "decoded_address" in df.columns:
    df["decoded_address"] = df["decoded_address"].apply(clean_address)

# Clean decoded_address_line if present
if "decoded_address_line" in df.columns:
    df["decoded_address_line"] = df["decoded_address_line"].apply(clean_address)

# Final cleaned dataset
df
