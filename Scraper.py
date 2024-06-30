[19:53] Jay Kerai
import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
import datetime
 
# URLs of the website to scrape
#TODO: Add Subdomain enumeration Capabiltiy
urlslist =['https://example.com','https://google.com']
# Number of most frequent words to return
num_words = 30
 
#Get Model for Association
def get_related_words(word, top_n=5): #adjust n for amount of words to return. #TODO, ARG Parse this.
    from gensim.models import KeyedVectors
    model = KeyedVectors.load_word2vec_format('./model/GoogleNews-vectors-negative300.bin', binary=True) # https://drive.usercontent.google.com/download?id=0B7XkCwpI5KDYNlNUTTlSS21pQmM&export=download&confirm=t&uuid=7b93067e-638f-45f2-9f6c-61db0e0f77b7
    try:
        related_words = model.most_similar(word, topn=top_n)
        return [word for word, similarity in related_words]
    except KeyError:
        return ["Word not in vocabulary"]
 
 
def scrape_and_count_words(url, num_words):
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
    common_words = word_counts.most_common(num_words)
    return common_words
 
 
def normalize_word(temp):
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
    return temp.lower()
 
# Scrape the website and get the most frequent words
stamp = datetime.datetime.now().strftime("%x").replace("/","-")
 
for url in urlslist:
    filename = "WordList " + url.replace('https://','').replace('http://','').replace('www.','') + " " + stamp + ".txt"
    most_frequent_words = scrape_and_count_words(url, num_words)
 
    print("list of top " + str(num_words) + " words from " + str(url))
    print('\n'.join('{}: {}'.format(*k) for k in enumerate(most_frequent_words)))
    print()
 
    for i in most_frequent_words:
        local_word_list = [] #build list for current word and associated word
        related_words = get_related_words(i[0].lower())
       
        for j in related_words:
            if (not '_' in j) and (j.lower() not in local_word_list) and (len(j) > 3) and j.lower() != "word not in vocabulary": #skip words less than 3 chars, already in the list and results with underscore
                local_word_list.append(normalize_word(j))
 
        local_word_list.append(normalize_word(i[0].lower())) #Finally add the word itself
 
        with open(filename, 'a',newline='') as file:
            try:
                for k in local_word_list:
                    file.write(k)
                    file.write("\n")
                    print("ADDED " + k +" to " + filename)
            except: #fallback
                print(" Error with adding to list ")
 
 
 
 
