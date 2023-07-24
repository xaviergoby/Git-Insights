import urllib.request
from PyPDF2 import PdfReader

# Download the PDF file from the URL

# (pg1)
#  ~~~~~ Markets in crypto-assets (MiCA) ~~~~~
#  "BRIEFING - EU Legislation in Progress"
# ...
# (pg11)
# This document is prepared for, and addressed to, the Members and staff of the European Parliament as
# background material to assist them in their parliamentary work.
url = 'https://www.europarl.europa.eu/RegData/etudes/BRIE/2022/739221/EPRS_BRI(2022)739221_EN.pdf'


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
