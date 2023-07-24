import pyLDAvis
import io
import requests
import PyPDF2
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from gensim import corpora
import pyLDAvis.gensim_models as gensimvis
import matplotlib.pyplot as plt

# download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# download necessary gensim data
nltk.download('wordnet')

# download pre-trained NER model
#nltk.download('averaged_perceptron_tagger')

# get the PDF file content
url = 'https://www.europarl.europa.eu/RegData/etudes/BRIE/2022/739221/EPRS_BRI(2022)739221_EN.pdf'
response = requests.get(url)
pdf_file = io.BytesIO(response.content)

# read the PDF file
pdf_reader = PyPDF2.PdfReader(pdf_file)

# get the text content from the PDF file
text = ""
for page in pdf_reader.pages:
    text += page.extract_text()

# preprocess the text
def preprocess(text):
    # remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in word_tokenize(text) if not word.lower() in stop_words]

    # lemmatize words
    lemmatizer = nltk.WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]

    # only keep words longer than 3 characters
    long_words = [word for word in lemmatized_words if len(word) > 3]

    return long_words

processed_text = preprocess(text)

# create a dictionary and corpus
dictionary = corpora.Dictionary([processed_text])
corpus = [dictionary.doc2bow(processed_text)]

# build the LDA model
lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=10, random_state=42)

# visualize the topics
vis = gensimvis.prepare(lda_model, corpus, dictionary)
# pyLDAvis.enable_notebook()
# pyLDAvis.display(vis)

pyLDAvis.save_html(vis, 'topic_modeling_visualization.html')

