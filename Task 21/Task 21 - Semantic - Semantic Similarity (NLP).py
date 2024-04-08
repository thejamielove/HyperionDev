import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# cat & monkey have the highest similarity as they are categorised as mammals (warm blooded with fur)
# banana & monkey have the second highest similarity due to pop culture & tropical habitat association
# banana & cat have the least similarity as these words are not commonly linked

print()

word1 = nlp("dog")
word2 = nlp("pizza")
word3 = nlp("ice cream")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

print()

# dog & pizza, as well as, ice cream & dog have the least similarity as one word is associated with food & the other an animal
# ice cream & pizza have the highest similarity due to the association with food

#-----------------------------------------------------------------------------------------------------

''' Running the example.py in 'en_core_web_sm', I noticed that the similarities were a lot lower due to 
    no word vectors in the model, known as word & phrase mapping numbers to calculate similarity & association.
    Running the same file in 'en_core_web_md', the similarities are a lot higher due to word vectors available in the model '''

#-----------------------------------------------------------------------------------------------------

tokens = nlp('cat apple monkey banana ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

#-----------------------------------------------------------------------------------------------------

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)