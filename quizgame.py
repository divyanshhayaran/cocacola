print("welcome to my quiz")

playing=input("do you want to play the game ")

if playing.lower() !="yes":
   quit()

print("okay lets play the game ")
score=0

answer=input("what does cpu stands for ")
if answer.lower()=="central processing unit":
   print("correct ")
   score+=1
else:
   print("wrong answer")


answer=input("who invented computer ")
if answer.lower()=="charles babbage":
   print("correct ")
   score+=1
else:
   print("wrong answer")


answer=input("what does ram stands for ")
if answer.lower()=="random access memory":
   print("correct ")
   score+=1
else:
   print("wrong answer")   


answer=input("is mouse a input device ")
if answer.lower()=="yes":
   print("correct ")
   score+=1
else:
   print("wrong answer")

print("you have got "+str(score)+" correct questions")
