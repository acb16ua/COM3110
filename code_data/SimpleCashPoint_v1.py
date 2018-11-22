
def cashpoint(truepin,balance):
    truepin1 = input("Enter your PIN: ")
    
    if truepin1 == truepin :
        print("What service would you like to use?")
        print("(1) Check Balance")
        print("(2) Withdraw Cash")
        print("(3) Mobile Phone Top-up")
        
        choice = input("Please select an option: ")
        
        if choice == "1" :
            return balance
        elif choice == "2" :
            drawAmount = input("How much money would you like to withdraw?: ")
            
            if float(drawAmount) > balance:
                print("INSUFFICIENT FUNDS!")
            else:
                balance = (balance-float(drawAmount))
                print("Money withdrawn: ", drawAmount)
                print("New Balance: ", balance)
                
        elif choice == "3" :
            print("Apologies, but the selected service is currently not avaialable")
            
        else :
            print("Wrong input!")
        
    else :
        print("WRONG PASSWORD!")
        

