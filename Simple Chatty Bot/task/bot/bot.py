def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    monarchs = ["Queen Elizabeth II", "King Jason", "Queen Madison", "Her Grace, Macie", "Mackenzie the Great"]
    print("Let's test your programming knowledge.")
    print("Who is the current British Monarch?")
    print("1. " + monarchs[3])
    print("2. " + monarchs[4])
    print("3. " + monarchs[0])
    print("4. " + monarchs[2])
    print("5. " + monarchs[1])
    user_answer = int(input())
    while user_answer != 3:
        print("Please, try again.")
        user_answer = int(input())
    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Aid', '2020')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
