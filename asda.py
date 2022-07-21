import random
import os 
user_credits = 100

deck = [2,3,4,5,6,7,8,9,10,'j','q','k','A',
        2,3,4,5,6,7,8,9,10,'j','q','k','A',
        2,3,4,5,6,7,8,9,10,'j','q','k','A'
        ,2,3,4,5,6,7,8,9,10,'j','q','k','A']

def menu():
    menu_choice = input('hello would you like to 1 sign in 2 register ')
    return menu_choice


def sign_in():
    x = True
    while x:
        username= input('enter ur username: ')
        password = input('enter your password: ')
        try:
            with open('%s/password.txt' % username, 'r') as f:
                line = f.readline()
                login_info = line.split('-')
                if login_info[1] == password:
                    print('hello ' ,username, ' you have ', login_info[2], ' credits in your account.')
                    return login_info
                else:
                    print('wrong pass')
        except FileNotFoundError:
            print('Username Not found')
                
            


def register():
    username_choice = input('Please enter a username: ')
    password_choice = input('Please enter a password: ')
    os.mkdir(username_choice)
    with open ('%s/password.txt' % username_choice, 'w') as f:
        f.write(username_choice)
        f.write('-')
        f.write(password_choice)
        f.write('-')
        f.write('100')
        f.close()

def save_score(login_info, user_credits):
    username = login_info[0]
    password= login_info[1]
    strcreds = str(user_credits)
    with open ('%s/password.txt' %username, 'w') as f:
        f.write(username)
        f.write('-')
        f.write(password)
        f.write('-')
        f.write(strcreds)
    print('your credits have been updated')




def user_bet(user_credits):
    x = True
    while x:
        user_wager = int(input('please input your bet: '))
        if user_wager > user_credits:
            print('bet cannot be more than balance')
        elif user_wager == str:
            print('Numbers only')
        else:
            return user_wager
        

def shuffle_deck():
    new_deck = deck.copy()
    random.shuffle(new_deck)
    return new_deck

def give_cards(player_hand, dealer_hand):
    player_hand.append(new_deck.pop())
    dealer_hand.append(new_deck.pop())
    player_hand.append(new_deck.pop())
    dealer_hand.append(new_deck.pop())

def hits(turn):
    turn.append(new_deck.pop())
    print(turn[-1])
    return turn

def hand_value(turn):
    if 'A' in turn:
        turn.append(turn.pop(turn.index('A')))

    total = 0
    face = ['j','q','k']
    for x in turn:
        if x in range(1,11):
            total += x
        elif x in face:
            total += 10
        else:
            if total  >= 11:
                total += 1
            else:
                total += 11
    if total>21:
        print('you went bust')
        return 1
    return total


def comparison(total_user, total_dealer, user_credits, user_wager, dealer_hand):
    if total_user > 21:
        print('bust')
        user_credits -= user_wager
        score['draws'] += 1
    elif total_dealer > 21:
        print('dealer bust')
        score['wins'] += 1
        user_credits += user_wager
    elif total_dealer == 21:
        print('dealer blackjack u lose')
        score['losses'] += 1
        user_credits -= user_wager
    elif total_dealer == total_user:
        print('draw')
        score['draws'] += 1
    elif total_dealer > total_user:
        print('dealer win')
        score['losses'] += 1
        user_credits -= user_wager
    else:
        print('win!')
        score['wins'] += 1
        user_credits += user_wager
    print(dealer_hand, total_dealer)
    return user_credits



score = {'wins':0,'draws':0,'losses':0}
new_deck = shuffle_deck()
print(user_credits)

def play(new_deck,user_credits):
    a = True
    while a:
        menus = menu()
        if menus == '1':
            login_info = sign_in()
            user_credits = int(login_info[2])
            a = False
            y = True
            while y:
                if (len(new_deck)/52)*100<25:
                    new_deck = shuffle_deck()
                user_wager = user_bet(user_credits)
                player_hand = []
                dealer_hand = []
                give_cards(player_hand, dealer_hand)
                print('hand of: {}, {}.'.format(player_hand[0],player_hand[1]))
                player_hand_value = hand_value(player_hand)
                print('hand value: ' , player_hand_value)
                total_dealer = hand_value(dealer_hand)
                print('dealer_shows: ', dealer_hand[0])

                x = True
                while x:
                    decide = input('1 hit, 2 stick:        ')
                    if decide == '1':
                        hits(player_hand)
                        total_user = hand_value(player_hand)
                        print(total_user)
                        if total_user == 1:
                            user_credits -= user_wager
                            print(user_credits)
                            x = False
                    elif decide == 's':
                        print(score)
                    else:
                        while total_dealer < 14:
                            hits(dealer_hand)
                            total_dealer = hand_value(dealer_hand)
                        total_user = hand_value(player_hand)
                        user_credits = comparison(total_user, total_dealer, user_credits, user_wager, dealer_hand)
                        print(user_credits)
                        x= False
                user_play = input('continue playing? y/n:    ')
                print('\n\n*************************\n\n')
                if user_play == 'n':
                    save_score(login_info, user_credits)
                    y = False

        else:
            register()
    
play(new_deck,user_credits)







