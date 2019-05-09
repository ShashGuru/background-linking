import json
import collections
with open('data.json', 'r') as fp:
    data = json.load(fp)
doc_dict =collections.OrderedDict()
for k, v in data.items():
    v = v.replace("\xad","-")
    v = v.replace("\xa0"," ")
    v = v.replace("\u2009"," ")   
    doc_dict[k] = v

query_id = "9171debc316e5e2782e0d2404ca7d09d"
query_file = open("query.txt", "r")
query_str = query_file.read()
import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer

stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]  


for k, v in doc_dict.items():   
    print(cosine_sim(query_str,v))    