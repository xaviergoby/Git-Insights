import requests
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from gensim.corpora import Dictionary
from gensim.models import LdaModel

# Download the PDF document
# url = "https://www.europarl.europa.eu/RegData/etudes/BRIE/2022/739221/EPRS_BRI(2022)739221_EN.pdf"
url = "https://eur-lex.europa.eu/resource.html?uri=cellar:f69f89bb-fe54-11ea-b44f-01aa75ed71a1.0001.02/DOC_1&format=PDF"

response = requests.get(url)
open("MiCA.pdf", "wb").write(response.content)

# Convert PDF to text using Tika
from tika import parser
parsed_pdf = parser.from_file("MiCA.pdf")
text = parsed_pdf["content"]

# Tokenize and preprocess the text
def preprocess(text):
    result = []
    for token in simple_preprocess(text):
        if token not in STOPWORDS and len(token) > 3:
            result.append(token)
    return result

tokenized_text = [preprocess(text)]

# Create a Gensim dictionary and corpus
dictionary = Dictionary(tokenized_text)
corpus = [dictionary.doc2bow(doc) for doc in tokenized_text]

# Perform LDA topic modeling
lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=10, passes=10)

# Print the top 10 words for each topic
for idx, topic in lda_model.show_topics(formatted=False, num_topics=10, num_words=10):
    print("Topic: ", idx)
    print(", ".join([w[0] for w in topic]))
    print()
