
### IMPORTS ###
# import random
# import info
###
# look at 'from info import *' #

# INITIAL IDEAS
## choose board
## come up to a big hill
## choose to go down or not
## have different outcomes depending on board
### like if you have a dinghy and do down the hill you crash
### or if you have the three six you make it down before all of your friends

# THINGS I NEED TO ADD/WORK ON
## also need to add error handling at some point

## read comments about hill/flat choice ~ line 49ish

## think about creating functions for each board choice ~ line 66ish

## ask about adding random thing for the hill outcome
### like a 50/50 chance of crashing or making it ~ line 87ish
### adding onto this, maybe add a chance for all of the board outcomes.
#### like a 90/10 chnace of crashing on the dinghy or a 25/75 for the horzion

## move onto 'what happens next' ~ line 100ish



def main():
    
    def print_menu():
        print("        MENU")
        print("---------------------")
        print("1) Landyachtz Dinghy")
        print("2) Sector9 Horizon")
        print("3) ThreeSix Dropthrough")
        print("4) Kryptonics Pintail")
        print("5) quit")
    
    print("you and some friends are going longboarding.\n")
    print_menu()
    board_choice = int(input("\nWhich board will you take?:  "))
    
    # def handleboard_choice():
    # tab everything in if function is needed
    if board_choice == 1:
        print("\nyou chose to take the Landyachtz Dinghy!")
        # print(dinghy_info)
    elif board_choice == 2:
        print("\nyou chose to take the Sector9 Horizon!")
    elif board_choice == 3:
        print("\nyou chose to take the ThreeSix Dropthrough!")
    elif board_choice == 4:
        print("\nyou chose to take the Kryptonics Pintail!")
    elif board_choice == 5:
        print("\n quitting program")
        quit()
    # else:
    #     print("error 420: number too high")
    #     print_menu() 
    
    # handle_board_choice()
    
    
    ### maybe add an option to go right or left,
    ### one being a hill and the other being flat
    #### this would suck tho because i already wrote a bunch of crap
    #### for the hill thing that i would need to change if i did the choice.
    print("\nwhile you were riding, you come up to a hill\nwould you like to bomb the hill or move on?")
    hill_choice = input("type: ,bomb, or ,move on,:    ")
    
    # def handle_hill_choice():
    ### maybe make all of choices into a funtion to make it easier? like a different function for each board ###
    # again, tab everything over if needed
    # this will be all of the outcomes for the dinghy (1):
    if board_choice == 1 and hill_choice == "bomb":
        print("\nyou crashed! Try a board that's better for hills\n")
        print_menu()
    elif board_choice == 1 and hill_choice == "move on":
        print("\nyou move down a few streets to avoid the getting hurt on the hill\n")

    # outcomes for horizon (1):
    elif board_choice == 2 and hill_choice == "bomb":
        print("\nyou made it down the hill, but you had to go slow to avoid speed wobbles " \
                "so you were the last one to the bottom of the hill\n")
    elif board_choice == 2 and hill_choice == "move on":
        print("\nyou move on to find a street that is better for cruising\n")
        
    # outcomes for threesix (3):
    elif board_choice == 3 and hill_choice == "bomb":
        print("'nthe ThreeSix is great for downhill racing, you made it to the bottom " \
                "before all of your friends!\n")
    elif board_choice == 3 and hill_choice == "move on":
        print("\nif you don't want to bomb hills yet, it's ok. Go find a street to cruise on\n")
        
    # outcomes for kryptonics (4):
    elif board_choice == 4 and hill_choice == "bomb":
        print("\nyou crahsed because kryptonics boards are trash lol\n")
        # try to make a 50/50 chance of making it down the hill
        # random.choice([0, 1])
        # if random.choice == 0:
        #     print("you crashed")
        # elif random.choice == 1:
        #     print("you made it")
    elif board_choice == 4 and hill_choice == "move on":
        print("\nyou moved on, but all of your friends are mad at you because your board is trash\n")
    
    
    # this will be after the hill or whatever i make the other option
    # print("whoo, that was fun! do you want to keep riding or go home?")
    # choice_2 = input("type ,keep riding, or ,go home,:    ")
    
    # if choice_2 == "keep riding":
    #     print("would you like to change boards or stick with yours?")
    #     keep_going_choice = input("type ,change, or ,keep,")
        
    #     if keep_going_choice == "change":
    #         print_menu()
    #     elif keep_going_choice == "keep":
            
    
    
    
    
    
main()


