#guess a number and computer will find it
print('Please think of a number between 0 and 100!')
low = 0
high = 100
ans = (low + high)//2
print('Is your secret number ',ans,'?')
m = 0
while m < 100:
  
  x = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
  if x == 'h' or x == 'l' or x == 'c' :
   
        if x == 'c':
            print('Game over. Your secret number was: ',ans)
            break
        elif x == 'h':
            high = ans
            ans = (low + high)//2
            print('Is your secret number ',ans,'?')
        else:
            low = ans
            ans = (low + high)//2
            print('Is your secret number ',ans,'?')
  else:
      print('Sorry, I did not understand your input.')
      print('Is your secret number ',ans,'?')
  m = m+1
