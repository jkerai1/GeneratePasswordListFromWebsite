import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
 
# Function to scrape website and return most frequent words
 
def scrape_and_count_words(url, num_words=20):
#Spoof user Agent to beat WAFs!
    request_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
    # Fetch the webpage content
    response = requests.get(url, headers=request_headers)
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return
 
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
 
    # Extract text from paragraphs and other relevant tags
 
    text = ' '.join([p.get_text() for p in soup.find_all('p')])
    # Clean and split the text into words
    words = re.findall(r'\b\w+\b', text.lower())
    print(type(words))
    words = filter(lambda item: len(item) > 4, words) #Can't use less than length of 4 for banned password list
    whitelist = {'their','right','through','customers'}
    words = filter(lambda item: item not in whitelist, words) #allow words to be removed
 
    # Count the frequency of each word
    word_counts = Counter(words)
    #print(type(word_counts))
    # Get the most common words
    common_words = word_counts.most_common(num_words)
 
    return common_words,words
 
# URL of the website to scrape
url = 'https://www.example.com'
#TODO: Add Subdomain enumeration Capabiltiy
 
# Number of most frequent words to return
num_words = 20
# Scrape the website and get the most frequent words
most_frequent_words,words = scrape_and_count_words(url, num_words)
 
# Print the result
print("list of top " + str(num_words) + " words from " + str(url))
print('\n'.join('{}: {}'.format(*k) for k in enumerate(most_frequent_words)))
for i in most_frequent_words:
    print(i[0])
