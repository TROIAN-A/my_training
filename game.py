import random
random.seed() #system time

compliance = {'1' : 'scissors','2' : 'paper','3' : 'rock','4' : 'lizard','5' : 'Spock', '6' : 'stop'}
win = {'scissors' : ('paper' , 'lizard'), 'paper' : ('rock', 'Spock'), 'rock' : ('scissors', 'lizard'),
       'lizard' : ('Spock', 'paper'), 'Spock' : ('scissors', 'rock')}

user_input = str()

while user_input != 'stop' or user_input == '6':
    option = ['scissors', 'paper', 'rock', 'lizard', 'Spock']
    random.shuffle(option) #shuiffle
    computer_choise = random.choice(option) #choise

    user_input = input('Make your choice 1 if your choise scissors, 2 if papper, '
                       '3 if rock, 4 if lizard and 5 if Spock. Stop enter 6!\n')
    user_input = compliance.get(user_input)
    print('You chose is', user_input+"!")

    win_combination = win.get(user_input) #dict.get(key[, default])

    if computer_choise == user_input: #logic
        print('There is a draw', computer_choise)
    elif user_input == '6' or user_input == 'stop':
        break
    elif computer_choise in win_combination:
        print('Well done. Computer chose '+computer_choise, 'and failed! :)')
    else:
        print('Sorry, but computer chose '+computer_choise, 'and win! :(')
print('I liked it, come again, bye!')
