# this is for testing out importing the hill file to save space
## UPDATE: it didnt work
## disregard this file until more import tests are necessary

def main():
    
    def print_menu():
        print("        MENU")
        print("---------------------")
        print("1) Landyachtz Dinghy")
        print("2) Sector9 Horizon")
        print("3) ThreeSix Dropthrough")
        print("4) Kryptonics Pintail")
        print("5) quit")
    
    print("you and some friends decide to go longboarding\n\nhere are your boards-")
    print_menu()
    board = int(input("which board do you want to take?:    "))
    
    if board == 1:
        print("\nyou chose to take the Dinghy! a great choice for cruising with your friends\n")
    elif board == 2:
        print("\nyou chose to take the Horizon! a great choice for cruising with your friends and maybe bombing some hills\n")
    elif board == 3:
        print("\nyou chose to take the ThreeSix! a great choice for high speeds and bombing hills\n")
    elif board == 4: 
        print("\nyou chose to take the Pintail! a good beginner board\n")
    elif board == 5:
        print("\nprogram will self destruct in 5 seconds...\n")
        print("5...")
        print("4...")
        print("3...")
        print("2...")
        print("1...")
        print("explosion.wav")
        quit()
    # error handling that doesnt work yay
    # elif board > 5:
    #     print("error 420: number too high")
        
    
    print("\nbefore you leave, you need to decide if you want to go left or right")
    direction = input("type ,left, or ,right,:    ")
    
    ### left = hill
    if direction == "left":
        print("you came across a big hill while you were riding! "\
                "would you like to bomb the hill or move on?\n")
        handle_hill()
                    
    elif direction == "right":
        print("havent gotten this far yet lol")
    
    
    
    
main()