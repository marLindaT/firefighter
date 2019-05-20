

from bs4 import BeautifulSoup
import os

#soup = BeautifulSoup(open("Take the Chapter 4 Test.html"), "html.parser")


   


soup = BeautifulSoup(open("firefighter1FinalTest_flashcards_sourceCode_html.html"), "html.parser")



    
questions = []
answers =[]
correct_ans =[]



for question in soup.find_all('span', {'class' : 'TermText notranslate lang-en'}):
    x = question.text.strip()
    questions.append(x)
    print(x)

##for ans in soup.find_all('label', {'class' : 'm-l-1'}):
##    x = ans.text.strip()
##    answers.append(x)    
##    #print(x)
##    
##for correct in soup.find_all('div', {'class' : 'rightanswer'}):
##    x = correct.text.strip()
##    correct_ans.append(x)
##    #print(x)
        
