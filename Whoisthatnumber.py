from random import randrange
n = randrange(1000)
while True:
  v = int(input())
  if n == v:
    print('bravo! you have defeated me.')
    break
  print('nice try! too bad the number is too low.' if (n > v) else 'nice try! to bad the number is too big.')



##NOTE:You can change the stuff it prints if you guess a number too big or guessed the number too low or even the message it shows when you 
# guess it right to your liking. Most of you would already know but i'am telling this just in case someone isn't don't mess with anything 
# else and the number guessing game should run on the default replit console also don't worry if it shows an error if you wrote something 
# except a number it should run smoothly even though it might show an error if you write anything excpet a number which should be obvious 
# to most of you.   
# Enjoy guessing numbers :)