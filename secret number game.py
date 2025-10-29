# secret number game
import random
secret = random.randint(1, 10)
# print(secret)
k= int(input("enter the number: "))
tries=1
if k==secret:
      print(f"you got it in {tries} try the secret number was {secret}")
else:
  while k!=secret:
      if k<secret:
        print("too low")
      else:
        print("too high")
      k=int(input("try again: ")) 
      tries=tries+1 
      if tries>2 and k!=secret:
        print("you lost, the number was", secret)
        break  
      elif k==secret:
        print(f"you got it in {tries} tries the secret number was {secret}")