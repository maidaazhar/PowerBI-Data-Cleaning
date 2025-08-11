import re

# Clean text values
def clean_text(text: str) -> str:
    if not isinstance(text, str) or not text.strip():
        return ""

    # Remove emojis/unwanted chars (keep letters, numbers, commas, -)
    text = re.sub(r"[^\w\s,-]", "", text, flags=re.UNICODE)

    # Remove periods
    text = text.replace(".", " ")

    # Fix commas/spaces
    text = re.sub(r",+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    # Remove short words (<3) except whitelist
    whitelist = {"ali"}
    words = [w for w in text.split() if len(w) >= 3 or w.lower() in whitelist]

    # Rejoin and title case
    return " ".join(words).title()

# Apply cleaning on dataset
dataset["decoded_name"] = dataset["decoded_name"].apply(clean_text)
dataset["decoded_owner"] = dataset["decoded_owner"].apply(clean_text)
