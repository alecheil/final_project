
### IMPORTS ###
# import random
# import stats


def main():
    
    def print_menu():
        print("        MENU")
        print("---------------------")
        print("1) Landyachtz Dinghy")
        print("2) Sector9 Horizon")
        print("3) ThreeSix Dropthrough")
        print("4) Kryptonics Pintail")
        print("5) quit")
    
    def board():
        print("you and some friends are going longboarding.\n")
        print_menu()
        board_choice = int(input("\nWhich board will you take?:  "))
    
        def handle_board_choice():
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
                
        handle_board_choice()    
    
        
    def hill():
        print("Before you leave, you need to decide of you want to go left or right.")
        direction_choice = input("type ,left, or ,right,:   ")
        
        # if left go handle hill stuff
        # def handle_direction_choice():
        if direction_choice == "left":
            print("you came across a hill while riding\ndo you want to bomb the hill " \
                    "or move on?")
            hill_choice = input("type ,bomb, or ,move on,:    ")
            
            # this will be all of the outcomes for the dinghy (1):
            #def handle_hill_choice():
            if board == 1 and hill_choice == "bomb":
                print("\nyou crashed! Try a board that's better for hills\n")
                print_menu()
            elif board == 1 and hill_choice == "move on":
                print("\nyou move down a few streets to avoid the getting hurt on the hill\n")

            #handle_hill_choice()
        # handle whatever i think of next    
        elif direction_choice == "right":
            print("i havent gotten that far yet lol")
            
        # handle_direction_choice()

                

    board()
    hill()

    
main()