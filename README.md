# POWERBI_DATA_CLEANING

Python scripts for cleaning and preparing data for Power BI dashboards, created specifically for the needs of the DigiKhata database.  
These scripts help standardize, transform, and prepare raw datasets for accurate reporting and visualization.

## 📂 Folder Structure
POWERBI_DATA_CLEANING
- **assign_type_category.py** – Assigns type categories to dataset entries  
- **change_type_category.py** – Updates or modifies existing type categories  
- **clean_address.py** – Cleans and formats address fields  
- **clean_name.py** – Standardizes and cleans name fields  
- **clean_text.py** – Removes unwanted characters and extra spaces from text  
- **clean_urdu.py** – Cleans Urdu text fields  
- **create_type_category_col.py** – Creates a new type category column  
- **decode_urdu.py** – Decodes Urdu text from encoded formats  
- **detect_lang.py** – Detects the language of text entries  
- **extract_city.py** – Extracts city names from address data  


## 🚀 Features
- **Text cleaning**: Remove unwanted characters, spaces, and symbols  
- **Language detection**: Identify Urdu or English text  
- **Address parsing**: Extract city names and standardize address formatting  
- **Categorization**: Assign or update type categories for business data  
- **Encoding fixes**: Decode Urdu text from non-UTF formats  

## 🛠 Technologies Used
- **Python 3.13.5**
- `pandas` for data manipulation
- `re` for regex-based text cleaning

## 📌 Notes
These scripts were built around the specific structure of the DigiKhata database but can be adapted for other datasets with similar requirements.
---

**Author**: Maida Azhar  
**Organization**: DigiKhata SMC PVT LTD.  

## Running in Power BI

These scripts are designed to work directly inside Power BI's "Run Python Script" transform step.

### Setup
1. **Install Python**
   - Download from [python.org](https://www.python.org/downloads/) (version 3.10 or later)
   - Add Python to PATH during installation

2. **Install required packages**
   ```bash
   pip install -r requirements.txt

