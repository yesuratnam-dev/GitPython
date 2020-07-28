import random

secret_number=random.randint(1,20)

guess_count=0
guess_limit=5
while guess_count<guess_limit:
    guess=int(input('guess: '))
    guess_count+=1
    if guess == secret_number:
        print('you won')
        break
    elif guess < secret_number:
      print('your guess is too low')
      guess_count+=1
    elif guess>secret_number:
        print('tour guess is too high')
    elif guess_count==guess_limit:
        print('you lost')
    else:
        print(''' 'you lost' better luck next time ''')

print(secret_number)