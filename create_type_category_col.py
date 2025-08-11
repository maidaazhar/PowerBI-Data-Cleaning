import pandas as pd

# Category codes to text
category_map = {
    101: "Kirana/Grocery",
    102: "Textile/Fashion",
    103: "Medical",
    104: "Electronics",
    105: "Mobile",
    106: "Automobile",
    107: "Sports",
    108: "Kids",
    109: "Hardware/Tools",
    110: "Other"
}

# Type codes to text
type_map = {
    1: "Distributor",
    2: "Manufacturer",
    3: "Wholesaler",
    4: "Retailer/Shop",
    5: "Services",
    6: "Others"
}

# Map category → text
dataset["toCategory"] = dataset["category"].apply(
    lambda x: category_map.get(x, "") if pd.notnull(x) else ""
)

# Map type → text
dataset["toType"] = dataset["type"].apply(
    lambda x: type_map.get(x, "") if pd.notnull(x) else ""
)
