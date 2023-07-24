# Tika is a Python library that allows for parsing and extracting text and metadata from various file formats, including PDFs
import tika
from tika import parser
import urllib.request
import gensim
from gensim.utils import simple_preprocess
from gensim.models import LdaModel
from gensim.corpora import Dictionary

# Download the PDF file from the URL
# url = 'https://www.europarl.europa.eu/RegData/etudes/BRIE/2022/739221/EPRS_BRI(2022)739221_EN.pdf'
url = "https://eur-lex.europa.eu/resource.html?uri=cellar:f69f89bb-fe54-11ea-b44f-01aa75ed71a1.0001.02/DOC_1&format=PDF"

filename = '../mica_regulation_memo.pdf'
urllib.request.urlretrieve(url, filename)

# Convert the PDF file to a list of sentences
# from tika import parser
pdf_file = open(filename, 'rb')
raw_content = parser.from_buffer(pdf_file)['content']
sentences = raw_content.split('\n\n')

# Tokenize the sentences using Gensim's simple_preprocess function
tokens = [simple_preprocess(sentence, deacc=True) for sentence in sentences]

# Create a Gensim dictionary from the tokens
dictionary = Dictionary(tokens)

# Create a bag-of-words representation of the tokens
bow_corpus = [dictionary.doc2bow(token) for token in tokens]

# Training an LDA topic model on the bag-of-words corpus
# num_topics => the num of topics I want to extract from the corpus
# passes => the num iterations that the LDA algo should run for to converge to a stable sol.
num_topics = 10
lda_model = LdaModel(bow_corpus, num_topics=num_topics, id2word=dictionary, passes=10)

# Print the topics and their corresponding words
for topic in lda_model.print_topics(num_words=10):
    print(topic)
