
import datefinder
import country_converter as coco
import re

def normalize_text(corpus):
    normalized_corpus = {}
    for doc_id, text in corpus.items():
        # Normalize country names first
        text = normalize_country(text)
        # Then normalize dates
        text = normalize_date(text)
        # Update the text in the dictionary
        normalized_corpus[doc_id] = text
    return normalized_corpus

def normalize_country(text):
    # Create a dictionary to map country names to ISO codes
    cc = coco.CountryConverter()
    country_mapping = {country: cc.convert(names=country, to='ISO2', not_found=None) for country in cc.data['name_short'].tolist()}
    
    # Find country names in the text
    for country_name, iso_code in country_mapping.items():
        if country_name.lower() in text.lower():
            # Replace country name with ISO code
            text = re.sub(r'\b' + re.escape(country_name) + r'\b', iso_code, text, flags=re.IGNORECASE)
    return text

def normalize_date(text):
    matches = datefinder.find_dates(text)
    for match in matches:
        # Replace the original date with the ISO 8601 formatted date
        text = text.replace(str(match.date()), match.strftime("%Y-%m-%d"))
    return text

