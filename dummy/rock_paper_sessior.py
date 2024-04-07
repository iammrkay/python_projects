import random
def display():
    print("Rock Payer Sissor \n")
    print("Select \n r for rock \n s for sissor \n p for paper \n")
    
def enter():
    user = input()
    if ((user == "r") or (user == "s") or (user == "p")):
        if (user == "r"):
            ch = "Rock"
        elif(user == "s"):
            ch = "Sissor"
        elif(user == "p"):
            ch = "Paper"
        print("you have selected ",ch)
        opponent = random.choice(["Rock","Sissor","Ppaper"])
        print("Opponent selected ",opponent)
        play(ch,opponent)        
    else:
        print("invalid selection select again")
        quit()

def play( ch , opponent):
    if (ch == opponent):
        print("its a Tie")
    elif(ch == "Rock" and opponent == "Sissor") or (ch == "Sissor" and opponent == "Ppaper") or (ch == "Ppaper" and opponent == "Rock"):
        print("You win")
    else:
        print("You lose")

display()
enter()
