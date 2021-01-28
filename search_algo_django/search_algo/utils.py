import string
import nltk
from nltk.stem import WordNetLemmatizer 


def clean_str(str):
    str = str.lower()
    str = str.translate(str.maketrans('', '', string.punctuation))

    lemmatizer = WordNetLemmatizer()

    word_list = nltk.word_tokenize(str)
    str = ' '.join([lemmatizer.lemmatize(w) for w in word_list])

    return str

