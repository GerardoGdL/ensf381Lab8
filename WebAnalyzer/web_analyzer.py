import requests
from bs4 import BeautifulSoup
from collections import Counter
import string

url = "https://en.wikipedia.org/wiki/University_of_Calgary"

try:
    response = requests.get(url)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url}")
except Exception as e:
    print(f"Error fetching content: {e}")

print(soup.prettify())

#Headers
headers = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
for header in headers:
    occurances = soup.find_all(header)
    print(f"There are {len(occurances)} occurance(s) of {header} in this text")
    print("---------------------------")

#Links
links = soup.find_all('a')
print(f"There are {len(links)} links in this text")

#Paragraphs
paragraphs = soup.find_all('p')
print(f"There are {len(paragraphs)} paragraphs in this text")

print("------------------------------------------------------------------------------------")

#Search for a keyword
keyword = input("Please enter a keyword you'd like to search for: ")
text_soup = soup.get_text()
keyword_occurances = text_soup.count(keyword)
print(f"There are {keyword_occurances} occurances of \"{keyword}\" in this text")

print("------------------------------------------------------------------------------------")

#Word Frequency
text_soup_lower = soup.get_text().lower()
text_soup_lower = text_soup_lower.translate(str.maketrans("", "", string.punctuation)) #This is to remove punctuation
words = text_soup.split()

counts = Counter(words)

word_and_count = {word: count for word, count in counts.items()}
top_words = Counter(word_and_count).most_common(5)
print("Top 5 most frequent words:")
for word, freq in top_words:
    print(f"{word}: {freq}")

print("------------------------------------------------------------------------------------")

#Longest Paragraph
paragraphs = soup.find_all('p')

longest_paragraph = ""
max_word_count = 0

for para in paragraphs:
    text = para.get_text().strip()
    words = text.split()
    
    if len(words) >= 5 and len(words) > max_word_count:  # Ignore empty or paragraphs shorter than 5 words
        longest_paragraph = text
        max_word_count = len(words)

print(f"The longest paragraph is: \n{longest_paragraph} \nThis paragraph has {max_word_count} words")

#Visualization
import matplotlib.pyplot as plt
labels = ['Headings', 'Links', 'Paragraphs']
values = [sum(len(soup.find_all(header)) for header in headers), len(links), len(paragraphs)]
plt.bar(labels, values)
plt.title('Group 28 - Gerardo and Kiersten')
plt.ylabel('Count')
plt.show()