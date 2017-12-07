def main():
    
    def print_board_menu():
        print("        MENU")
        print("---------------------")
        print("1) Landyachtz Dinghy")
        print("2) Sector9 Horizon")
        print("3) ThreeSix Dropthrough")
        print("4) Kryptonics Pintail")
        print("5) quit")
        
    def print_store_menu():
        print("       STORE")
        print("--------------------")
        print("1) Gatorade")
        print("2) Pepsi")
        print("3) Coffee")
        print("3) Leave")
        
    
    print("you and some friends decide to go longboarding\n\nhere are your boards-")
    print_board_menu()
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
        print("5...\n4...\n3...\n2...\n1...")
        print("explosion.wav")
        quit()

    
    print("\nbefore you leave, you need to decide if you want to go left or right")
    direction = input("type ,left, or ,right,:    ")
    
    ### left = hill
    if direction == "left":
        print("\nyou came across a big hill while you were riding! "\
                "would you like to bomb the hill or move on?\n")
        hill = input("type ,bomb, or ,move on,:    ")
        
        # outcomes for dinghy
        if hill == "bomb" and board == 1:
            print("\nGAME OVER: you crashed. try a board that is better for downhill next time\n")
                    
        # outcomes for horizon
        elif hill == "bomb" and board == 2:
            print("\nyou made it down the hill but you had to go slow to avoid speed wobble "\
                    "so you were the last one to the bottom. \n")

        # outcomes for threesix
        elif hill == "bomb" and board == 3:
            print("\nthe ThreeSix is great for downhill racing, you made it to the bottom before"\
                    "all of your friends\n")

        # outcomes for pintail
        elif hill == "bomb" and board == 4:
            print("\nGAME OVER: you crashed. pick a better board next time\n")

        elif hill == "move on":
            print("you decided not to bomb the hill. you and your friends keep cruising")
            if board == 4:
                print("\nGAME OVER: your board is slow and all of your friends left you, "\
                        "now you are all alone")
            else:
                print("eventually you all get tired and thirsty\n")
                print("would you like to buy something to drink at the store?")
                store = input("type ,go in, or  ,move on,:  ")
                
                if store == "go in":
                    print_store_menu()
                    drink = int(input("what would you like to drink?:   "))
                    
                    if drink == 1:
                        print("good choice! the gatorade gives you the electrolytes to keep riding\n")
                        print("Congratulations! you and your friends made it back to the car without crashing!")
                        
                    elif drink == 2: 
                        print("pepsi was a bad idea. you ride for a few minutes and start to not feel to good.")
                        print("you throw up in the street and call a friend to pick you up")
                        
                    elif drink == 3:
                        print("wow! you have a lot of energy. It wont last long though,"\
                                "that coffee was not a good idea.")
                        print("you experience a caffiene crash and are unable to go on")
                        
                    elif drink == 4:
                        print("leaving store...")
                        print("you decide to keep riding but dont have enough energy to go very long")
                        print("you and your friends decide to head back to the car")
                        print("\ncongratulations! you and your friends made it back to the car without crashing!")
                        
                elif store == "move on":
                    print("you decide to keep riding but dont have enough energy to go very long")
                    print("you and your friends decide to head back to the car")
                    print("\ncongratulations! you and your friends made it back to the car without crashing!")
                    
                    
    elif direction == "right":
        print("\nthis way is flat\nyou and your friends ride for a while")
        if board == 4:
                print("\nGAME OVER: your board is slow and all of your friends left you, "\
                        "now you are all alone")
        else:
            print("eventually you all get tired and thirsty\n")
            print("would you like to buy something to drink at the store?")
            store = input("type ,go in, or  ,move on,:  ")
            
            if store == "go in":
                print_store_menu()
                drink = int(input("what would you like to drink?:   "))
                
                if drink == 1:
                    print("good choice! the gatorade gives you the electrolytes to keep riding\n")
                    print("Congratulations! you and your friends made it back to the car without crashing!")
                    
                elif drink == 2: 
                    print("pepsi was a bad idea. you ride for a few minutes and start to not feel to good.")
                    print("GAME OVER: you throw up in the street and call a friend to pick you up")
                    
                elif drink == 3:
                    print("wow! you have a lot of energy. It wont last long though,"\
                            "that coffee was not a good idea.")
                    print("GAME OVER: you experience a caffiene crash and are unable to go on")
                    
            elif store == "move on":
                print("you decide to keep riding but dont have enough energy to go very long")
                print("you and your friends decide to head back to the car")
                print("\ncongratulations! you and your friends made it back to the car without crashing!")
                
            
        
        
    
    
    
    
main()