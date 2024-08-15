import spacy
from spacy.training import Example
import random
from preprocessing import getReceipt
from train import train_data

nlp = spacy.blank("en")

# Create a new NER component
ner = nlp.add_pipe("ner")

# Add the 'FOOD' label to the NER component
ner.add_label("FOOD")

# Convert the training data to spaCy's Example format
def convert_examples(train_data):
    examples = []
    for text, annot in train_data:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annot)
        examples.append(example)
    return examples

train_examples = convert_examples(train_data)

# Train the model
nlp.begin_training()
for epoch in range(16):  # Number of training epochs
    random.shuffle(train_examples)
    losses = {}
    for batch in spacy.util.minibatch(train_examples, size=2):
        for example in batch:
            nlp.update([example], drop=0.5, losses=losses)
    print(f"Epoch {epoch} - Losses: {losses}")

# Save the trained model
nlp.to_disk("food_ner_model")