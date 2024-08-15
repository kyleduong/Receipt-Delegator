import re

# Example block of text
text = """
Good Restaurant
89 Greenwich Ave.
212-691-8080

Guest Check Party of 2
Table 102 Ticket 4003

1 BISCUITS $3.00
1 COMBO 16.50
1 FRITTATA 11.75
Price: $31.25
Total: 33.87 USD
"""

# Define the regex pattern for matching prices
price_pattern = re.compile(r'\b(?:\$?\d+(?:\.\d{2})?|\d+\.\d{2} ?(?:USD|€|£)?)\b')

# Split text into lines
lines = text.split('\n')

# Filter lines that contain prices
price_lines = [line for line in lines if price_pattern.search(line)]

# Print filtered lines
for line in price_lines:
    print(line)
