# from game_final import *
import game_final
import game_03

def handle_hill():
    hill = input("type ,bomb, or ,move on,:    ")
        
    # outcomes for dinghy
    if hill == "bomb" and board == 1:
        print("you crashed! try a better board for downhill\n")
        print_menu()
    elif hill == "move on" and board == 1:
        print("you decided to not bomb the hill. that was a good idea "\
                "because you would have crashed on the dinghy\n")
                
    # outcomes for horizon
    elif hill == "bomb" and board == 2:
        print("you made it down the hill but you had to go slow to avoid speed wobble "\
                "so you were the last one to the bottom. \n")
        print_menu()
    elif hill == "move on" and board == 2:
        print("you decided to not bomb the hill. you and your friends keep cruising\n")
        
    # outcomes for threesix
    if hill == "bomb" and board == 3:
        print("the ThreeSix is great for downhill racing, you made it to the bottom before"\
                "all of your friends\n")
        print_menu()
    elif hill == "move on" and board == 3:
        print("you decided to not bomb the hill. you and your friends keep cruising\n")
        
    # outcomes for pintail
    if hill == "bomb" and board == 1:
        print("you crashed because kryptonics boards are trash lol\n")
        print_menu()
    elif hill == "move on" and board == 1:
        print("you decided to not bomb the hill which was a good idea because you" \
                "could have crashed on that cheap board\n")