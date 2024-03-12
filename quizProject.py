#PYTHON QUIZ
marks=0
def result(answer,question,marks):
    ans1="B"
    ans2="A"
    ans3="B"
    ans4="C"
    if question==1:
        if answer==ans1:
            marks+=1
            print('Correct answer')
        else:
            print("wrong answer")
            print("correct answer is B ")   
    elif question==2:
        if answer==ans2:
            marks+=1
            print('Correct answer')
        else:
            print("wrong answer")
            print("correct answer is A ")
            
    elif question==3:
        if answer==ans3:
            marks+=1
            print('Correct answer')
        else:
            print("wrong answer")
            print("correct answer is B ")
    elif question==4:
        if answer==ans4:
            marks+=1
            print('Correct answer')
        else:
            print("wrong answer")
            print("correct answer is C ")
    return marks        
question1=("Who is the first prime minister of INDIA?","A.GANDHI","B.NEHRU","C.AMBEDKAR","D.MODI")
question2=("Who is the richest man in INDIA?","A.AMBANI","B.GAUTAM ADANI","C.KUMAR BIRLA","D.DILIP") 
question3=("Whatis the capital of ASSAM?","A.HYDERBAD","B.DISPUR","C.AGRA","D.KERALA")
question4=("What is the red planet?","A.SUN","B.PLUTO","C.MARS","D.EARTH")

quiz=(question1,question2,question3,question4)
question=0
for i in quiz:
    for j in i:
        print(j)
    question+=1
    answer=input("enter ur choice (A,B,C,D):")
    marks=result(answer,question,marks)
    print()

print(marks)
