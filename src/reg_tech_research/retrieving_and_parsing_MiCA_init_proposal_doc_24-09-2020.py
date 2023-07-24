import urllib.request
from PyPDF2 import PdfReader

# Download the PDF file from the URL

# Brussels, 24.9.2020
# COM(2020) 593 final
# 2020/0265 (COD)
#
# Proposal for a
# REGULATION OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL
# on Markets in Crypto-assets, and amending Directive (EU) 2019/1937
url = "https://eur-lex.europa.eu/resource.html?uri=cellar:f69f89bb-fe54-11ea-b44f-01aa75ed71a1.0001.02/DOC_1&format=PDF"


filename = '../mica_regulation_memo.pdf'
urllib.request.urlretrieve(url, filename)

# Read the content of the PDF file
pdf_file = open(filename, 'rb')
pdf_reader = PdfReader(filename)
text = ''

# Loop over all the pages in the PDF file and extract the text
for page in pdf_reader.pages:
    page_text = page.extract_text()
    text += page_text

# Close the PDF file
pdf_file.close()

# Print the extracted text
print(text)
