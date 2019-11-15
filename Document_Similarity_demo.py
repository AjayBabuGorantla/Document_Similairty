from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
# from nltk.corpus import stopwords
import math
# from Input_File import Input_File

# document_1="The game of a life. is a game, of? everlasting .learning"
# document_2="The unexamined/ life. is not worth? living"
# document_3="Never. stop/ learning"

tokenizer_regex = RegexpTokenizer(r'\w+')

def mod_value(dictionary):
    _sum = 0
    for key in dictionary:
        _sum = _sum + math.pow(dictionary[key], 2)
    return math.sqrt(_sum)

def dot_product(dictionary1, dictionary2):
    dot_product = 0
    for key in dictionary1:
        if key in dictionary2:
            dot_product = dot_product + dictionary1[key] * dictionary2[key]
    return dot_product

def cosine_similarity_value(dictionary1, dictionary2):
    return dot_product(dictionary1, dictionary2) / (mod_value(dictionary1) * mod_value(dictionary2))

def tokenizer(document):
    tokenized_document = tokenizer_regex.tokenize(document.lower())

    # TODO: Remove all the punctuation marks in the tokenized document . So use RegEx Tokenizer or PunKt Tokenizer
    # tokenized_document.remove(".") - Not happening

    return tokenized_document

def word_frequency(tokenized_list):

    vector_tokenized_list = dict()

    for word in tokenized_list:
        if word not in vector_tokenized_list:
            vector_tokenized_list[word] = 0
        vector_tokenized_list[word] += 1

    return vector_tokenized_list



def main(document_1,document_2):


    tokenized_document_1=tokenizer(document_1)
    tokenized_document_2=tokenizer(document_2)

    vector_document_1=word_frequency(tokenized_document_1)
    vector_document_2=word_frequency(tokenized_document_2)
    
    return cosine_similarity_value(vector_document_1, vector_document_2)



if __name__=='__main__':
    main()
