import re 

# Provinces and countries
provinces = [
    "Punjab", "Sindh", "Balochistan", "Khyber Pakhtunkhwa",
    "Gilgit-Baltistan", "Azad Kashmir", "FATA"
]
countries = ["Pakistan", "Afghanistan", "India"]

# Extract city from address
def extract_city(address: str) -> str:
    if not isinstance(address, str) or not address.strip():
        return ""
    
    # Normalize separators
    address = re.sub(r",+", ",", address).strip(", ")
    parts = re.split(r"[,-]", address)
    parts = [p.strip() for p in parts if p.strip()]
    
    if not parts:
        return ""
    
    # If only one part
    if len(parts) == 1:
        return parts[0].title()
    
    # Word before province/country
    for i, part in enumerate(parts):
        if part in provinces or part in countries:
            if i > 0:
                return parts[i-1].title()
    
    # Last valid part
    for part in reversed(parts):
        if part not in provinces and part not in countries:
            return part.title()
    
    return ""

# Extract city from decoded_address
dataset["decoded_city"] = dataset["decoded_address"].apply(extract_city)

# Optionally from decoded_address_line aswell
# dataset["decoded_city_line"] = dataset["decoded_address_line"].apply(extract_city)
