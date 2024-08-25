#Calculator script 
#Written by Evannoshy :P on DD/MM/YY - 24/08/24
#Calculator includes addition, subtraction, division, multiplication

#create a prompt to input first number
while True:
 while True: #creates loop
    try:
        first_num = float(input('What is your first number? ')) 
        break #breaks loop
    except ValueError: #this forces user to input a number if not prompt will loop
        print("Please input a number!")
        continue
#create a prompt to indicate operator that user wants
 while True:
    operator = input('A: + , B: - , C: *, D: / ').upper() #.upper() allows user to indicate choice regardless of capitalization as it auto caps it
    if operator in ['A', 'B', 'C', 'D']: #if input is in array of choices, continue
        break
    else:
        print("Please input a valid option!") 
        continue
#create a prompt to input second number
 while True:
    try:
        second_num = float(input('What is your second number? '))
        break
    except ValueError:
        print("Please input a number!")
        continue
#conditions to be met for operator to take effect
 if operator == 'A':
    print(first_num + second_num)
 elif operator == 'B':
    print(first_num - second_num)
 elif operator == 'C':
    print(first_num * second_num)
 elif operator == 'D':
    print(first_num / second_num)

 # Ask if the user wants to perform another calculation

 again = input("Do you want to perform another calculation? (yes/no): ").strip().lower() #strips extra white spcaes and specifed characters from the start and end
 if again != 'yes': #if input is not yes, end loop, else user is able to continously use code
    print("Thank you for using the calculator!")
    break