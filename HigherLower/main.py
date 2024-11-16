import random
from art import logo,vs
from game_data import data

def select_influencer():
     random_influencer_data= data[(random.randint(0,len(data)))]
     info=random_influencer_data['name']+", a "+random_influencer_data['description']+" from " + random_influencer_data['country']
     followers=random_influencer_data['follower_count']
     return info,followers

def compare(user_option,inf1,inf2):
    score=0
    if user_option=="A" and (inf1[1]>inf2[1]) or (inf1[1]==inf2[1]):
            score+=1

    elif user_option=="B" and (inf2[1] > inf1[1]) or (inf2[1] == inf1[1]):
            score += 1
    else:
        score=0
    return score

def game():
    print(logo)
    final_score=0
    current_score = 0
    is_game_over=False
    influencer_1 = select_influencer()
    while not is_game_over:
        print("Compare A: "+influencer_1[0])
        print(vs)
        influencer_2=select_influencer()
        print("Against B: " + influencer_2[0])
        user_answer=input("Who has more followers? Type 'A' or 'B': ").upper()
        current_score =compare(user_answer,influencer_1,influencer_2)
        final_score+=current_score
        if current_score!=0:
            influencer_1=influencer_2
            print("\n"*20)
            print(f"You are right!! Current Score {final_score}")
        else:
            print(f"Sorry, that's wrong. Final score: {final_score}")
            is_game_over=True
game()

