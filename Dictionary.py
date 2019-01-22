import json
import difflib
from difflib import get_close_matches

data=json.load(open("data.json"))

def retrieve_meaning(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper()in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys(),1,0.8)) > 0:
        action= input("Did you mean %s instead? [y or n]" % get_close_matches(word,data.keys(),1,0.8)[0]).lower()
        if (action=="y"):
            return data[get_close_matches(word,data.keys(),1,0.8)[0]]
        elif (action=="n"):
            return("The word doesn't exist, yet.")
        else:
            return("Wrong input.")
    else:
        return("Word does not exist!")

word=input("Enter the word: ").lower()

output=retrieve_meaning(word)

if(type(output)==list):
    for i in output:
        print("-",i)
else:
    print("-",output)
