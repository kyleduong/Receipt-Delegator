import spacy, re
from spacy.training import Example
import random
from preprocessing import getReceipt
from train import train_data

def find_food_items():
    # Load the trained model
    nlp = spacy.load("food_ner_model")

    receipt_text = getReceipt()

    # Process the receipt text
    doc = nlp(receipt_text)

    food_items = []

    # Extract and print food items
    for ent in doc.ents:
        if ent.label_ == "FOOD":
            #print(f"Food Item: {ent.text}")
            food_items.append(ent.text)


    lines = receipt_text.splitlines()

    food_items_set = set(food_items)

    matching_lines = []
    for line in lines:
        if any(food_item in line for food_item in food_items_set):
            matching_lines.append(line)
    
    return matching_lines

test = find_food_items()
print(test)

def extractPrice(text):
    # Regular expression pattern to find prices
    pattern = r'\b\d+\.\d{2}\b'
    
    # Find all occurrences of the pattern
    prices = re.findall(pattern, text)
    
    # Convert the found prices to float and return
    prices = [float(price) for price in prices]

    # Calculate total price
    total_price = sum([prices])

    return total_price