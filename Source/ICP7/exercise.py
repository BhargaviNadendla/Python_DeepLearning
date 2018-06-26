from bs4 import BeautifulSoup
import urllib.request
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.util import trigrams
from nltk import ne_chunk
'''Get the text from the python programming language url'''
# Read the web url into a variable
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
# use urllib to open the url
res = urllib.request.urlopen(url)    #opening the defined url
plain_text = res
# Use beautiful soup to get the content of webpage
soup = BeautifulSoup(plain_text, "html.parser") #using beautiful soap to get the text

data = soup.get_text("\n") #Extracting text using soup.get_text
#print(data)
with open("out.txt",'w') as f:  #writig the data to a text file
    f.write(str(data.encode("utf-8"))) 
tokenize_words = nltk.word_tokenize(data) #tokenizing words from the text
print("Tokenized words")
print("----------------------------------------------------------------------------------------------------------------")
print(tokenize_words)  #printing tokenized words
print("-----------------------------------------------------------------------------------------------------------------")
print("POS Tagging")   
print("----------------------------------------------------------------------------------------------------------------")
parts_of_speech=nltk.pos_tag(tokenize_words) #getting the parts of speech of each tokenize_word
print(parts_of_speech)
print("-----------------------------------------------------------------------------------------------------------------")
print("Trigrams")
print("------------------------------------------------------------------------------------------------------------------")
print(list(trigrams(tokenize_words)))  #listing all the trigrams from the words
print("------------------------------------------------------------------------------------------------------------------")
print("Named entity recognition")
print("------------------------------------------------------------------------------------------------------------------")
print(ne_chunk(parts_of_speech))   #recognizing the entity parts of speech for each word
print("-------------------------------------------------------------------------------------------------------------------")

with open("out.txt",'r') as f:
    lines=f.read().splitlines() #splitting the data into lines
    for l in lines:
        words=l.split()   # for each line of the data, splititng into words
        pstem=PorterStemmer()  
        word_lemmatizer=WordNetLemmatizer() 
        for i in words:
            print("Stemmed words")
            print("-------------")
            print(pstem.stem(i)) # applying stemmer to get the stem of the word
            print("-------------")
            print("Lemmatized words")
            print("--------------")
            print(word_lemmatizer.lemmatize(i)) # applying lemmatization to each word to check the difference
            print("--------------")






