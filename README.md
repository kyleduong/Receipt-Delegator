# Receipt Delegator

Goal: Take a picture of your receipt and be able to delegate all of the receipt items purchased to the various people that ordered.

## How it works
The user will upload a picture of a receipt with a preferrable dark background. Then the image will undergo a transformation and reading. 

![Receipt Process](./Receipt%20Process.png)

Preprocesses the image -> Pytesseract extracts the words -> use spaCy for NER and filter the food words

## Installation
```bash
git clone https://github.com/kyleduong/Receipt-Delegator.git
```

## Set up Python environment

Install [pytesseract](https://tesseract-ocr.github.io/tessdoc/Installation.html)

```bash
# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # For Windows, use venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Running the code hosted locally
```bash
python Backend/app.py
npm run dev
```
[https://localhost:5173](https://localhost:5173) to see the the locally hosted website.

## Technologies Used

- **Frontend:** React.js
- **Backend:** Flask
- **Database:** PostgreSQL
- **Other:** Pytesseract, spaCy, OpenCV
  
## Retraining the model

```bash
python Backend/trainingNER.py
```

## License
This project is licensed under the terms of the MIT license
