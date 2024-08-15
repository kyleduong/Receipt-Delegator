# Receipt Delegator

Goal: Take a picture of your receipt and be able to delegate all of the receipt items purchased to the various people that ordered.

## How it works

![Receipt Process](./Receipt%20Process.png)

Preprocesses the image -> Pytesseract extracts the words -> use spaCy for NER and filter the food words

## Installation
```bash
git clone https://github.com/kyleduong/Receipt-Delegator.git
```

## Set up Python environment

Install [pytesseract]([https://example.com](https://tesseract-ocr.github.io/tessdoc/Installation.html))

```bash
# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # For Windows, use venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```
