from Game_data import data
import random


def name_pick(celeb):
    celeb_name = celeb["name"]
    celeb_job = celeb["description"]
    celeb_country = celeb["country"]
    return f"Compare A: {celeb_name}, a {celeb_job}, from {celeb_country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


score = 0
should_continue = False
celeb_2 = random.choice(data)
while not should_continue:
    celeb_1 = celeb_2
    celeb_2=random.choice(data)
    print(celeb_1)
    if celeb_1==celeb_2:
        celeb_2=random.choice(data)
    print(celeb_2)
    print(f"Compare A:{name_pick(celeb_1)}")
    print(f"Against B:{name_pick(celeb_2)}")
    user_guess = input("Who has more followers?.Type 'A' or 'B': ")
    celeb_follows_1 = celeb_1["follower_count"]
    celeb_follows_2 = celeb_2["follower_count"]
    is_correct = check_answer(user_guess, celeb_follows_1, celeb_follows_2)
    if is_correct:
        score += 1
        print(f"You're correct.Current score: {score}")
    else:
        should_continue = True
        print(f"Sorry that's wrong. Final score {score}")
