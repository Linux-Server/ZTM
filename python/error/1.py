# ERROR HANDLING
while True:
    try:
        age = int(input("Please enter your age ?"))
        
    except:
        print("Please entera valid number")
    else:
        print("Thank you")
        break
  