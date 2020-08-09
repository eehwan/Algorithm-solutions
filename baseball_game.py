import sys
import random

min_lev = 1
max_lev = 5

def set_level():
    try:
        level = int(input(f"Set level({min_lev}~{max_lev}) :\n"))
        if (level<=max_lev and level>=min_lev):
            return level
        else:
            print(f"--- Level must be {min_lev}~{max_lev} ---\n.")
            return set_level()
    except:
        print("Wrog input\n")
        return set_level()
def set_answer(lev:int):
    answer = ""
    while len(set(list(answer))) < lev:
        answer+=str(random.randint(1,9))
    return answer
def set_score(answ):
    print(f"\nGame started !!\nGuess {len(answ)} digits from 1 to 9(unredundant)\n")
    def score(ans):
        try :
            num = int(input("Input : "))
            input_nums = list(str(num))
            if len(input_nums)!=len(ans):
                print("--- wrong length of input ---\n")
                return score(ans)
            strike = 0
            ball = 0
            for index, value in enumerate(input_nums):
                if value == ans[index]:
                    strike+=1
                elif value in ans:
                    ball+=1
            print(f"{strike} strike\n{ball} ball\n")
            if strike==len(ans):
                print("\n < You W.I.N > \n")
            else:
                return score(ans)
        except:
            print(f"--- Input {len(ans)} digits ---\n")
            score(ans)
    try:
        score(answ)
    except:
        print("error")
        score(answ)
def play():
    level = set_level()
    answer = set_answer(level)
    # print(answer)
    set_score(answer)
    ask()
def ask():
    do = str(input("\ndo again? (y/n): ")).upper()
    if do == "Y":
        print("\n---------------------\n\n\n")
        play()

def init():
    play()
play()
