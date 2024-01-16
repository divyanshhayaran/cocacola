import random
top_range=input("input a number")

if top_range.isdigit():
   top_range=int(top_range)
   if top_range<=0:
      print("please type a number larger than 0")
      quit()
else:
   print("please type a number next time")
   quit()
random_number=random.randint(0,top_range)
guesses=0

while True:
   guesses+=1
   user_guess=input("guess any number")
   if user_guess.isdigit():
      user_guess=int(user_guess)
   else:
      print("please type a number")
      continue 

   if user_guess==random_number:
      print("you got it ")
      break
   else:
      print("you got it wrong")

print("you got it in",str(guesses),"guesses")



