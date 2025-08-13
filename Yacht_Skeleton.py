'''
AAAA111
'''

import random #Do not alter
import time

def main():
    available_categories = [1, 2, 3, 4, 5, 6] #Do not alter
    category_names = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes"] #Do not alter
    filename = "High_Scores.txt" #Do not alter
    username = "AAAA111"
    print_banner(username)
    new_score = play_game(available_categories, category_names)
    handle_high_scores(filename, username, new_score)
        
#Do not alter
def roll_dice():
    dice_roll = []
    for i in range(5):
        dice_roll.append(random.randrange(1,7))
    return dice_roll

def print_banner(username):
    text = f"*  Yacht by {username}  *"
    print("*" * len(text))
    print(text)
    print("*" * len(text))
    print()
    pass

def calculate_roll_score(category, dice_roll):
    turn_score = 0
    for item in dice_roll:
        if item == category:
            turn_score += item
    
    return turn_score        
    pass

def get_category(available_categories):
    print(f"The available categories are: {available_categories}")
    selection = True

    while selection:
        category_input = input("Please select your scoring category: ")
        if category_input.isnumeric() == False or int(category_input) not in available_categories:
            print("\nInvalid selection. Please select again.\n")
        else:
            category_selection = int(category_input)
            target_number = category_selection
            place = available_categories.index(target_number)
            available_categories.pop(place)
            selection = False
    return target_number
    pass

def play_game(available_categories, category_names):
    total_score = 0
    rounds = 5
    counter = 0

    for number in range(rounds + 1):
        if counter >= rounds:
            print(f"\nCongratulations! Final Score = {total_score}")
            return total_score
            
        else:
            counter += 1
            results = roll_dice()
            results.sort()
            print(f"Dice results = {results}")
            target = get_category(available_categories)
            print(f"Scoring category is: {category_names[target-1]}")
            calculate_score = calculate_roll_score(target, results)
            total_score += calculate_score
            print(f"Round {counter} Score = {calculate_score}")
            if counter < rounds:
                print(f"Current Total Score = {total_score}\n")
    pass

def read_high_scores(filename):
    file = open(filename, 'r')
    scores = file.read().split('\n')
    file.close()
    values = []
    for item in scores[1:]:
        splice = item.split('.')
        for element in splice[1::2]:
                values.append(element[1:])
    return values
    pass

def update_high_scores(filename, username, high_scores, new_score):
    counter = 0
    track_score = new_score
    file = open(filename, 'w')
    high_scores = list(map(int, high_scores))
    for item in high_scores:
        if track_score > item:
            high_scores.pop(counter)
            high_scores.append(track_score)
            high_scores.sort(reverse = True)
            track_score = item
        counter += 1
    counter = 0
    file.write(f"High Scores for {username}\n")
    for item in range(5):
        file.write(f"{counter + 1}. {high_scores[counter]}\n")
        counter += 1
    file.close()
    pass

def handle_high_scores(filename, username, new_score):
    high_scores = read_high_scores(filename)
    update_high_scores(filename, username, high_scores, new_score)
    pass

main() #Do not alter

