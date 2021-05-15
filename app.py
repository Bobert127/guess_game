from random import randint


def get_user_range():
    user_digit_min = int(input("Provide digit for min range:\n"))
    user_digit_max = int(input("Provide digit for max range:\n"))

    return user_digit_min, user_digit_max


def draw_digit(min_digit, max_digit):
    return randint(min_digit, max_digit)


def guess_digit(drawn_digit, min_d, max_d):
    print(f"Guess number from: {min_d} - {max_d}")
    counter = 0
    while True:
        counter += 1
        user_guess = int(input())

        if drawn_digit > user_guess:
            print("Too low")
        elif drawn_digit < user_guess:
            print("Too high")
        else:
            print(f"Yuo win {counter} times")
            return


def play():
    min_digit, max_digit = get_user_range()
    shuffled = draw_digit(min_digit, max_digit)
    guess_digit(shuffled, min_digit, max_digit)


play()

# guess_digit(42, 10, 20)
