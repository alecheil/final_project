board = 1

def hill():
    print("Before you leave, you need to decide of you want to go left or right.")
    direction_choice = input("type ,left, or ,right,:   ")
    def handle_direction_choice():
        if direction_choice == "left":
            print("you came across a hill while riding\ndo you want to bomb the hill " \
                    "or move on?")
            hill_choice = input("type ,bomb, or ,move on,:    ")
                
            # # this will be all of the outcomes for the dinghy (1):
            # def handle_hill_choice():
            #     if board == 1 and hill_choice == "bomb":
            #         print("\nyou crashed! Try a board that's better for hills\n")
            #         #print_menu()
            #     elif board == 1 and hill_choice == "move on":
            #         print("\nyou move down a few streets to avoid the getting hurt on the hill\n")
                        
hill()