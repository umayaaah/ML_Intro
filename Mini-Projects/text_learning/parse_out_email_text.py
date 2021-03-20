#!/usr/bin/python

from nltk.stem.snowball import SnowballStemmer
import string

def parseOutText(f):
    """ given an opened email file f, parse out all text below the
        metadata block at the top
        (in Part 2, you will also add stemming capabilities)
        and return a string that contains all the words
        in the email (space-separated) 
        
        example use case:
        f = open("email_file_name.txt", "r")
        text = parseOutText(f)
        
        """


    f.seek(0)  ### go back to beginning of file
    all_text = f.read()

    ### split off metadata
    content = all_text.split("X-FileName:")
    words = ""
    if len(content) > 1:
        ### remove punctuation
        text_string = content[1].translate(str.maketrans({key: None for key in string.punctuation}))

        # print("Email body before stemming: ")
        # print(text_string)

        # words = text_string
        stemmer = SnowballStemmer("english")

        # convert string into a list of words and stripping new line tokens 
        words = text_string.split(" ")
        # stem each word in the list (ignoring whitespace and new lines) and return new list of stemmed words
        words = [stemmer.stem(w.replace("\n", " ")) for w in words if w != ""]
        # join the list on a space to create a sentence of newly stemmed words
        words = " ".join(words)

        words = " ".join(words.split())
        
    return words

    
def main():
    ff = open("test_email.txt", "r")
    text = parseOutText(ff)
    print("Email body after stemming:\n")
    print(text + "\n")



if __name__ == '__main__':
    main()
