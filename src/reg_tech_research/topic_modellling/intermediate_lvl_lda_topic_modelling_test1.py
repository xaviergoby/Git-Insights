import tika
from tika import parser
import re
from gensim import corpora, models
from pprint import pprint
import urllib.request

# # Parse PDF document using Tika
# tika.initVM()
# parsed_pdf = parser.from_file('MiCA-Markets-in-Crypto-Assets-regulation-memo.pdf')
# pdf_text = parsed_pdf['content']
#
# # Clean text
# clean_text = re.sub(r'\s+', ' ', pdf_text)



# Download the PDF file from the URL
# url = 'https://www.europarl.europa.eu/RegData/etudes/BRIE/2022/739221/EPRS_BRI(2022)739221_EN.pdf'
url = "https://eur-lex.europa.eu/resource.html?uri=cellar:f69f89bb-fe54-11ea-b44f-01aa75ed71a1.0001.02/DOC_1&format=PDF"

filename = '../mica_regulation_memo.pdf'
urllib.request.urlretrieve(url, filename)

# Convert the PDF file to a list of sentences
# from tika import parser
pdf_file = open(filename, 'rb')
raw_content = parser.from_buffer(pdf_file)['content']


# Split text into individual sentences
# sentences = re.split(r'[.!?]+', clean_text)
sentences = re.split(r'[.!?]+', raw_content)

# Tokenize sentences and remove stopwords
stop_words = ['a', 'an', 'the', 'in', 'on', 'at', 'of', 'and', 'or', 'to', 'for', 'is', 'are', 'be', 'will', 'may', 'can', 'should', 'must', 'would', 'could', 'have', 'has', 'had', 'been', 'that', 'this', 'these', 'those', 'with', 'by', 'from']
tokenized_sentences = [[word.lower() for word in sentence.split() if word.lower() not in stop_words] for sentence in sentences]

# Create a dictionary representation of the documents.
dictionary = corpora.Dictionary(tokenized_sentences)

# Convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in tokenized_sentences]

# Define number of topics
num_topics = 5

# Build LDA model
lda_model = models.ldamodel.LdaModel(corpus, num_topics=num_topics, id2word=dictionary)

# Print the topics
pprint(lda_model.show_topics(num_topics=num_topics, formatted=False))
