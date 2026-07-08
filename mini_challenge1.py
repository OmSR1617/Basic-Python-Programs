marks = ()

while True:
    print("1. Add Marks")
    print("2. Total and Percentage of Marks")
    print("3. Check Grade and Status")
    print("4. Eligible for Scholarship?")
    print("5. Exit")
    
    choice = input("Enter Your Choice: ")
    
    if choice == "1":
        sub1 = int(input("Enter English Marks: "))
        sub2 = int(input("Enter Maths Marks: "))
        sub3 = int(input("Enter Hindi Marks: "))
        sub4 = int(input("Enter Marathi Marks: "))
        sub5 = int(input("Enter Science Marks: "))
        marks = sub1, sub2, sub3, sub4, sub5
        print("Marks Added Sucessfully!")
        
    elif choice == "2":
        if not marks:
            print("Please add marks first")
            continue
        else:
            total = sub1 + sub2 + sub3 + sub4 + sub5
            percentage = (total/ 500) * 100
            print(f"Your Total Marks is : {total} ")
            print(f"Your Percentage Marks is : {percentage}% ")
        
    elif choice == "3":
        if not marks:
            print("Please add marks first")
            continue
        else:
            total = sub1 + sub2 + sub3 + sub4 + sub5
            percentage = (total/ 500) * 100
        
            if percentage >= 90:
                print("You are passed with grade A")
            elif percentage >= 80:
                print("You are passed with grade B")
            elif percentage >= 60:
                print("You are passed with grade C")
            elif percentage >= 40:
                print("You are passed with grade D")
            elif percentage < 40:
                print("You are failed!")
            
    elif choice == "4":
        if not marks:
            print("Please add marks first")
            continue
        else:
            total = sub1 + sub2 + sub3 + sub4 + sub5
            percentage = (total/ 500) * 100
            
            if percentage >= 85:
                print("Congrats, You are eligible for Scholarship")
            else:
                print("Sorry, You are not eligible for Scholarship")
            
    elif choice == "5":
        print("Exiting...")
        break
    
    else:
        print("Please Enter Valid Input")