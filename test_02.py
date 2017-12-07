

def main():
    

    def print_menu():
        print("        MENU")
        print("---------------------")
        print("1) Landyachtz Dinghy")
        print("2) Sector9 Horizon")
        print("3) ThreeSix Dropthrough")
        print("4) Kryptonics Pintail")
        print("5) quit")
    
    print_menu()
    board = int(input("pick a longboard:    "))
    
    if board == 1:
        print("chose dinghy")
    elif board == 2:
        print("chose horizon")
    
    
    direction = input("type left or right:  ")
    
    if direction == "left":
        hill = input("type bomb or move on:    ")
        if hill == "bomb" and board == 1:
            print("you crashed lol")
        elif hill == "move on" and board == 2:
            print("you moved on")
        
    elif direction == "right":
        print("right works")
    

    
    
main()