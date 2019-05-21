"""
this is a WIP to get answers from quizlet page and make an iterable for JS on html app
questions are provided in the same span with answer options from the raw html but are labelled with either A. to D.
the correct answers are provided in separate spans(same class) but can be removed using basic modulus operator on list items

trying to use regex to screen question_with_answer list by selecting options between A....D.

final output should be a list of dicts (JS objects) for use in JS


"""
import re
from bs4 import BeautifulSoup
import os

#soup = BeautifulSoup(open("Take the Chapter 4 Test.html"), "html.parser")


   


soup = BeautifulSoup(open("firefighter1FinalTest_flashcards_sourceCode_html.html"), "html.parser")

    
raw_source = []


for question in soup.find_all('span', {'class' : 'TermText notranslate lang-en'}):
    x = question.text.strip()
    raw_source.append(x)
    #print(x)
print(f"raw_source is {len(raw_source)} long")

question_with_answers =[]

for num in range(len(raw_source)):
    if num%2==0:
        question_with_answers.append(raw_source[num])

answer_options =[]

for item in question_with_answers:
    m = re.search("?<=^[A-D]\.).+(?=[A-D]\.$", item)
        

answers = []

for num in range(len(raw_source)):
    if num%2>0:
        answers.append(raw_source[num])


        


