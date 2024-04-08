import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Garden path sentences list
gardenpathSentences = [
    "The old man the boat.",
    "The complex houses married and single soldiers and their families.",
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."]


# Tokenize each sentence and perform named entity recognition
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print(f"\nSentence = {sentence}\n") # print out of each garden path sentence from list
    for token in doc:
        print(f"Token = {token.text : <12} POS = {token.pos_ : ^10} Entity = {token.ent_type_ : >5}") # use of < ^ > for text alignment

print()
print(spacy.explain("PERSON"))
print(spacy.explain("GPE"))
print()

# Entities lookup comment:
# 1. In the sentence "Mary gave the child a Band-Aid." & "That Jill is never here hurts.", the entity is "PERSON", 
#    classified as 'people, including fictional'.
#    The name "Mary" & "Jill" does match the typical usage of people, so the entity label makes sense.
# 2. In the sentence "The cotton clothing is made of grows in Mississippi.",
#    the entity is "GPE", classified as 'countries, cities & states'. The word "Mississippi" does match the typical usage of a 
#    geopolitical location, so the entity label does make sense.