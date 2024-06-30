import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
import datetime
 
# Function to scrape website and return most frequent words
words = []
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
    words = (re.findall(r'\b\w+\b', text.lower())) #alphanumeric
    words = filter(lambda item: len(item) > 4, words) #Can't use less than length of 4 for banned password list
    whitelist = {'their','right','through','customers','your','with'}
    words = filter(lambda item: item not in whitelist, words) #allow words to be removed
 
    # Count the frequency of each word
    word_counts = Counter(words)
    #print(type(word_counts))
    # Get the most common words
    common_words = word_counts.most_common(num_words)
    return common_words
 
# URLs of the website to scrape
urlslist =['https://example.com','https://scc.com']
 
#TODO: Add Subdomain enumeration Capabiltiy
# Number of most frequent words to return
num_words = 50
# Scrape the website and get the most frequent words
stamp = datetime.datetime.now().strftime("%x").replace("/","-")
 
for url in urlslist:
    filename = "WordList " + url.replace('https://','').replace('http://','').replace('www.','') + " " + stamp + ".txt"
    most_frequent_words = scrape_and_count_words(url, num_words)
    # Print the result
    print("list of top " + str(num_words) + " words from " + str(url))
    print('\n'.join('{}: {}'.format(*k) for k in enumerate(most_frequent_words)))
#print raw list
    print()
    print("Raw Normalized list \n")
    for i in most_frequent_words:
        temp = i[0].lower()
        temp = temp.replace("0", "o")
        temp = temp.replace("1","l")
        temp = temp.replace("$","s")
        temp = temp.replace("@","a")
    #Provided by synacktiv.com https://www.synacktiv.com/publications/entra-id-banned-password-lists-password-spraying-optimizations-and-defenses
        temp = temp.replace("5", "s")
        temp = temp.replace("|","l")
    #temp = temp.replace("i","l")
        temp = temp.replace("2","z")
        temp = temp.replace("3","e")
        temp = temp.replace("!","l")
        print(temp)
 
        with open(filename, 'a',newline='') as file:
            try:
                file.write(temp)
                file.write("\n")
            except: #fallback
                print(" Error with adding " + temp + " to list ")
 
