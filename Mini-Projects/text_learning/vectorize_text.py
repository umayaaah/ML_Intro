#!/usr/bin/python

import os
import pickle
import re
import sys

# sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText

"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.
"""


from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

### temp_counter limits the number of emails to iterate over
### remove this limit to run over full dataset
temp_counter = 0


for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        temp_counter += 1
        if temp_counter < 200:
            path = os.path.join('../../ud120-projects/', path[:-1])
            # print(path)
            email = open(path, "r")

            ### use parseOutText to extract the text from the opened email
            stemmed_email = parseOutText(email)

            ### use str.replace() to remove any instances of the words
            ignore_words = ["sara", "shackleton", "chris", "germani"]
            reg = re.compile(r"\b%s\b|"%r"\b|\b".join(map(re.escape, ignore_words)))
            stemmed_email = reg.sub("", stemmed_email)
            
            ### append the preprocessed text to word_data
            word_data.append(stemmed_email)

            ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
            from_data.append(name)

            email.close()

def test():
    print(word_data[152])
    print(from_data[152])

test()
print("emails processed")
from_sara.close()
from_chris.close()

pickle.dump( word_data, open("your_word_data.pkl", "wb") )
pickle.dump( from_data, open("your_email_authors.pkl", "wb") )


### in Part 4, do TfIdf vectorization here


