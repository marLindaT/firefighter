
from bs4 import BeautifulSoup
import os

#soup = BeautifulSoup(open("Take the Chapter 4 Test.html"), "html.parser")


   
chapter = 4

soup = BeautifulSoup(open(f"ifsta html\\Take the Chapter {chapter} Test.html"), "html.parser")



    
questions = []
answers =[]
correct_ans =[]

def getInformation():
    
    for question in soup.find_all('div', {'class' : 'qtext'}):
        x = question.text.strip()
        questions.append(x)
        #print(x)
    
    for ans in soup.find_all('label', {'class' : 'm-l-1'}):
        x = ans.text.strip()
        answers.append(x)    
        #print(x)
        
    for correct in soup.find_all('div', {'class' : 'rightanswer'}):
        x = correct.text.strip()
        correct_ans.append(x)
        #print(x)
        
getInformation()  

def createAnsList(arr):
    
    n = 0
    result=[]
    for i in range(int(len(arr)/4)):
        result.append(arr[0+4*n:4+4*n])
        n+=1
    return result

answer_arr = createAnsList(answers)

def createQuestionDictionary(qlist, alist, answers):
    
    if not (len(questions)==len(answer_arr)==len(correct_ans)):
        print("escaped")
        return None
        ## exit if the lists aren't equal length
    result ={}
    questionNum = 1
    for i in range(len(qlist)):
        
        result[f"Chapter{chapter}_question{questionNum}"] = {"question":qlist[questionNum-1],
              "a":alist[questionNum-1][0],
            "b":alist[questionNum-1][1],
            "c":alist[questionNum-1][2],
            "d":alist[questionNum-1][3],
            "ans":answers[questionNum-1]}
        questionNum +=1
        
    return result
    
    
    
final = createQuestionDictionary(questions, answer_arr, correct_ans)


#file = open("deleteMe.txt", "a")

#file.write(str(final))

#file.close()
    
    










    
