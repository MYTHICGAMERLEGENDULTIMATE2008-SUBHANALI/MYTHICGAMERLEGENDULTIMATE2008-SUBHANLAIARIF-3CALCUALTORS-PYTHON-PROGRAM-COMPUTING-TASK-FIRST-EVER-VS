
# PROGRAMMING A SINGLE/SIMPLE CALCUALTOR FOR ADDITION,SUBTRACTION,MULTIPLICATION AND DIVISION

print("HELLO EVERYONE THIS IS A BASIC ADDING/MINUSING/MULTIPLYING/DIVIDING CALCUALTOR MADE BY LEGENDGAMER5208. SINCE THIS IS THE 1ST MODEL I WILL TRY TO MAKE A MORE ADVANCED FINAL PRODUNCT IN THE FUTURE WITH SCIENTIFIC NOTATION AND OTHER COOL DOING STUFF. HOPE YOU ALL ARE SAFE AND NOW GRANTING PERMISSION TO GO AHEAD AND HAVE UNLIMITED FUN")


# THIS PART OF THE FUNCTION ADDS TWO INPUTED NUMBERS A AND B 
def add_2(a, b,):
    return a + b
    
# THIS PART OF THE FUNCTION ADDS THREE INPUTED NUMBERS A AND B AND C 
def add_3(a, b, c):
    return a + b + c
    
# THIS PART OF THE FUNCTION ADDS FOUR INPUTED NUMBERS A AND B AND C AND D 
def add_4(a, b, c, d):
    return a + b + c + d
    
# THIS PART OF THE FUNCTION ADDS FIVE INPUTED NUMBERS A AND B AND C AND D AND E 
def add_5(a, b, c, d, e):
    return a + b + c + d + e
    
# THIS PART OF THE FUNCTION ADDS SIX INPUTED NUMBERS A AND B AND C AND D AND E AND F 
def add_6(a, b, c, d, e, f):
    return a + b + c + d + e + f 
    
# THIS PART OF THE FUNCTION ADDS SEVEN INPUTED NUMBERS A AND B AND C AND D AND E AND F AND G 
def add_7(a, b, c, d, e, f, g):
    return a + b + c + d + e + f + g

# THIS FUNCTION SUBTRACTS TWO INPUTED NUMBERS A AND B
def subtract_2(a, b):
    return a - b
    
# THIS FUNCTION SUBTRACTS THREE INPUTED NUMBERS A AND B AND C
def subtract_3(a, b, c):
    return a - b - c
    
# THIS FUNCTION SUBTRACTS FOUR INPUTED NUMBERS A AND B AND C AND D
def subtract_4(a, b, c, d):
    return a - b - c - d 
    
# THIS FUNCTION SUBTRACTS FIVE INPUTED NUMBERS A AND B AND C AND D AND E
def subtract_5(a, b, c, d, e):
    return a - b - c - d - e
    
# THIS FUNCTION SUBTRACTS SIX INPUTED NUMBERS A AND B AND C AND D AND E AND F
def subtract_6(a, b, c, d, e, f):
    return a - b - c - d - e - f

# THIS FUNCTION SUBTRACTS SEVEN INPUTED NUMBERS A AND B AND C AND D AND E AND F AND G
def subtract_7(a, b, c, d, e, f, g):
    return a - b - c - d - e - f- g
    
# THIS FUNCTION MULTIPLYS TWO INPUTED NUMBERS TOGETHER A AND B
def multiply_2(a, b):
    return a * b

# THIS FUNCTION MULTIPLYS TWO INPUTED NUMBERS TOGETHER A AND B AND C
def multiply_3(a, b, c):
    return a * b * c 

# THIS FUNCTION MULTIPLYS TWO INPUTED NUMBERS TOGETHER A AND B AND C AND D
def multiply_4(a, b, c, d):
    return a * b * c * d

# THIS FUNCTION MULTIPLYS TWO INPUTED NUMBERS TOGETHER A AND B AND C AND D AND E
def multiply_5(a, b, c, d, e ):
    return a * b * c * d * e 

# THIS FUNCTION MULTIPLYS TWO INPUTED NUMBERS TOGETHER A AND B AND C AND D AND E AND F
def multiply_6(a, b, c, d, e, f):
    return a * b * c * d * e * f

# THIS FUNCTION MULTIPLYS TWO INPUTED NUMBERS TOGETHER A AND B AND C AND D AND E AND F AND G
def multiply_7(a, b, c, d, e, f, g):
    return a * b * c * d * e * f * g
    
# THIS FUNCTION DIVIDED TWO NUMBERS TOGTEHER AND THEY ARE A AND B
def divide_2(a, b):
    return a / b

# THIS FUNCTION DIVIDED THREE NUMBERS TOGTEHER AND THEY ARE A AND B AND C
def divide_3(a, b, c):
    return a / b / c
    
# THIS FUNCTION DIVIDED FOUR NUMBERS TOGTEHER AND THEY ARE A AND B AND C AND D
def divide_4(a, b, c, d):
    return a / b / c / d
    
# THIS FUNCTION DIVIDED FIVE NUMBERS TOGTEHER AND THEY ARE A AND B AND C AND D AND E
def divide_5(a, b, c, d, e):
    return a / b / c / d / e
    
# THIS FUNCTION DIVIDED SIX NUMBERS TOGTEHER AND THEY ARE A AND B AND C AND D AND E AND F
def divide_6(a, b, c, d, e, f):
    return a / b /  c / d / e / f
    
# THIS FUNCTION DIVIDED SEVEN NUMBERS TOGTEHER AND THEY ARE A AND B AND C AND D AND E AND F AND G
def divide_7(a, b, c, d, e, f, g):
    return a / b / c / d / e / f / g


print("Select operation.")
print("1.add_2/n")
print("2.add_3/n")
print("3.add_4/n")
print("4.add_5/n")
print("5.add_6/n")
print("6.add_7/n")
print("7.subtract_2/n")
print("8.subtract_3/n")
print("9.subtract_4/n")
print("10.subtract_5/n")
print("11.subtract_6/n")
print("12.subtract_7/n")
print("13.multiply_2/n")
print("14.multiply_3/n")
print("15.multiply_4/n")
print("16.multiply_5/n")
print("17.multiply_6/n")
print("18.multiply_7/n")
print("19.divide_2/n")
print("20.divide_3/n")
print("21.divide_4/n")
print("22.divide_5/n")
print("23.divide_6/n")
print("24.divide_7/n")

for i in range(24):
    # NOW WE WILL TAKE INPUT FOR THE NUMBERS FROMTHE USER ANY NUMBER CAN BE ENETERED
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/21/23/24): ")

    # THIS WILL CHECK IF THE CHOICE IS FROM ONE OF THE LISTED OPTIONS
    if choice in ('1', '7', '13', '19'):
        NUMBER1 = float(input("ENTER THE FIRST REQUIRED NUMBER: "))
        NUMBER2 = float(input("ENTER THE SECOND REQUIRED NUMBER: "))

        if choice == '1':
            print(NUMBER1, "+", NUMBER2, "=", add_2(NUMBER1, NUMBER2))

    # check if user wants another calculation
    # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            
            
         break

        if next_calculation == "yes":
            
            
         continue            

        elif choice == '7':
            print(NUMBER1, "-", NUMBER2, "=", subtract_2(NUMBER1, NUMBER2))

    # check if user wants another calculation
    # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            
            
         break

        if next_calculation == "yes":
            
            
         continue 

        elif choice == '13':
            print(NUMBER1, "*", NUMBER2, "=", multiply_2(NUMBER1, NUMBER2))

    # check if user wants another calculation
    # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            
            
         break

        if next_calculation == "yes":
            
            
         continue            

        elif choice == '19':
            print(NUMBER1, "/", NUMBER2, "=", divide_2(NUMBER1, NUMBER2))

    # check if user wants another calculation
    # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            
            
         break

        if next_calculation == "yes":
            
            
         continue         

    # THIS WILL CHECK IF THE CHOICE IS FROM ONE OF THE LISTED OPTIONS
    if choice in ('2', '8', '14', '20'):
        NUMBER1 = float(input("ENTER THE FIRST REQUIRED NUMBER: "))
        NUMBER2 = float(input("ENTER THE SECOND REQUIRED NUMBER: "))
        NUMBER3 = float(input("ENTER THE THIRD REQUIRED NUMBER: "))
        
        if choice == '2':
            print(NUMBER1, "+", NUMBER2, "+", NUMBER3, "=", add_3(NUMBER1, NUMBER2, NUMBER3))

    # check if user wants another calculation
    # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            
            
         break

        if next_calculation == "yes":
            
            
         continue            

        elif choice == '8':
            print(NUMBER1, "-", NUMBER2, "-", NUMBER3, "=", subtract_3(NUMBER1, NUMBER2, NUMBER3))

    # check if user wants another calculation
    # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            
            
         break

        if next_calculation == "yes":
            
            
         continue             

        elif choice == '14':
            print(NUMBER1, "*", NUMBER2, "*", NUMBER3, "=", multiply_3(NUMBER1, NUMBER2, NUMBER3))

    # check if user wants another calculation
    # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            
            
         break

        if next_calculation == "yes":
            
            
         continue            

        elif choice == '20':
            print(NUMBER1, "/", NUMBER2, "/", NUMBER3, "=", divide_3(NUMBER1, NUMBER2, NUMBER3))

    # check if user wants another calculation
    # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            
            
         break

        if next_calculation == "yes":
            
            
         continue            
        
            
    # THIS WILL CHECK IF THE CHOICE IS FROM ONE OF THE LISTED OPTIONS
    if choice in ('3', '9', '15', '21'):
        NUMBER1 = float(input("ENTER THE FIRST REQUIRED NUMBER: "))
        NUMBER2 = float(input("ENTER THE SECOND REQUIRED NUMBER: "))
        NUMBER3 = float(input("ENTER THE THIRD REQUIRED NUMBER: "))
        NUMBER4 = float(input("ENETR THE FOURTH REQUIRED NUMBER: "))
        
        if choice == '3':
            print(NUMBER1, "+", NUMBER2, "+", NUMBER3, "+", NUMBER4, "=", add_4(NUMBER1, NUMBER2, NUMBER3, NUMBER4))

    # check if user wants another calculation
    # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            
            
         break

        if next_calculation == "yes":
            
            
         continue            

        elif choice == '9':
            print(NUMBER1, "-", NUMBER2, "-", NUMBER3, "-", NUMBER4, "=", subtract_4(NUMBER1, NUMBER2, NUMBER3, NUMBER4))

    # check if user wants another calculation
    # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            
            
         break

        if next_calculation == "yes":
            
            
         continue            

        elif choice == '15':
            print(NUMBER1, "*", NUMBER2, "*", NUMBER3, "*", NUMBER4, "=", multiply_4(NUMBER1, NUMBER2, NUMBER3, NUMBER4))

    # check if user wants another calculation
    # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            
            
         break

        if next_calculation == "yes":
            
            
         continue            

        elif choice == '21':
            print(NUMBER1, "/", NUMBER2, "/", NUMBER3, "/", NUMBER4, "=", divide_4(NUMBER1, NUMBER2, NUMBER3, NUMBER4))

    # check if user wants another calculation
    # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            
            
         break

        if next_calculation == "yes":
            
            
         continue            
        
    # THIS WILL CHECK IF THE CHOICE IS FROM ONE OF THE LISTED OPTIONS
    if choice in ('4', '10', '16', '22'):
        NUMBER1 = float(input("ENTER THE FIRST REQUIRED NUMBER: "))
        NUMBER2 = float(input("ENTER THE SECOND REQUIRED NUMBER: "))
        NUMBER3 = float(input("ENTER THE THIRD REQUIRED NUMBER: "))
        NUMBER4 = float(input("ENTER THE FOURTH REQUIRED NUMBER: "))
        NUMBER5 = float(input("ENTER THE FIFTH REQUIRED NUMBER: "))
        
        if choice == '4':
            print(NUMBER1, "+", NUMBER2, "+", NUMBER3, "+", NUMBER4, "+", NUMBER5, "=", add_5(NUMBER1, NUMBER2, NUMBER3, NUMBER4, NUMBER5))

    # check if user wants another calculation
    # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            
            
         break

        if next_calculation == "yes":
            
            
         continue            

        elif choice == '10':
            print(NUMBER1, "-", NUMBER2, "-", NUMBER3, "-", NUMBER4, "-", NUMBER5, "=", subtract_5(NUMBER1, NUMBER2, NUMBER3, NUMBER4, NUMBER5))

    # check if user wants another calculation
    # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            
            
         break

        if next_calculation == "yes":
            
            
         continue            

        elif choice == '16':
            print(NUMBER1, "*", NUMBER2, "*", NUMBER3, "*", NUMBER4, "*", NUMBER5, "=", multiply_5(NUMBER1, NUMBER2, NUMBER3, NUMBER4, NUMBER5))

    # check if user wants another calculation
    # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            
            
         break

        if next_calculation == "yes":
            
            
         continue            

        elif choice == '22':
            print(NUMBER1, "/", NUMBER2, "/", NUMBER3, "/", NUMBER4, "/", NUMBER5, "=", divide_5(NUMBER1, NUMBER2, NUMBER3, NUMBER4, NUMBER5))

    # check if user wants another calculation
    # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            
            
         break

        if next_calculation == "yes":
            
            
         continue            
        
    # THIS WILL CHECK IF THE CHOICE IS FROM ONE OF THE LISTED OPTIONS
    if choice in ('5', '11', '17', '23'):
        NUMBER1 = float(input("ENTER THE FIRST REQUIRED NUMBER: "))
        NUMBER2 = float(input("ENTER THE SECOND REQUIRED NUMBER: "))
        NUMBER3 = float(input("ENTER THE THIRD REQUIRED NUMBER: "))
        NUMBER4 = float(input("ENTER THE FOURTH REQUIRED NUMBER: "))
        NUMBER5 = float(input("ENTER THE FIFTH REQUIRED NUMBER: "))
        NUMBER6 = float(input("ENTER THE SIXTH REQUIRED NUMBER: "))
        
        if choice == '5':
            print(NUMBER1, "+", NUMBER2, "+", NUMBER3, "+", NUMBER4, "+", NUMBER5, "+", NUMBER6, "=", add_6(NUMBER1, NUMBER2, NUMBER3, NUMBER4, NUMBER5, NUMBER6))

    # check if user wants another calculation
    # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            
            
         break

        if next_calculation == "yes":
            
            
         continue            

        elif choice == '11':
            print(NUMBER1, "-", NUMBER2, "-", NUMBER3, "-", NUMBER4, "-", NUMBER5, "-", NUMBER6, "=", subtract_6(NUMBER1, NUMBER2, NUMBER3, NUMBER4, NUMBER5, NUMBER6))

    # check if user wants another calculation
    # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            
            
         break

        if next_calculation == "yes":
            
            
         continue            

        elif choice == '17':
            print(NUMBER1, "*", NUMBER2, "*", NUMBER3, "*", NUMBER4, "*", NUMBER5, "*", NUMBER6, "=", multiply_6(NUMBER1, NUMBER2, NUMBER3, NUMBER4, NUMBER5, NUMBER6))

    # check if user wants another calculation
    # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            
            
         break

        if next_calculation == "yes":
            
            
         continue            

        elif choice == '23':
            print(NUMBER1, "/", NUMBER2, "/", NUMBER3, "/", NUMBER4, "/", NUMBER5, "/", NUMBER6, "=", divide_7(NUMBER1, NUMBER2, NUMBER3, NUMBER4, NUMBER5, NUMBER6))

    # check if user wants another calculation
    # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            
            
         break

        if next_calculation == "yes":
            
            
         continue            
        
    # THIS WILL CHECK IF THE CHOICE IS FROM ONE OF THE LISTED OPTIONS
    if choice in ('6', '12', '18', '24'):
        NUMBER1 = float(input("ENTER THE FIRST REQUIRED NUMBER: "))
        NUMBER2 = float(input("ENTER THE SECOND REQUIRED NUMBER: "))
        NUMBER3 = float(input("ENTER THE THIRD REQUIRED NUMBER: "))
        NUMBER4 = float(input("ENTER THE FOURTH REQUIRED NUMBER: "))
        NUMBER5 = float(input("ENTER THE FIFTH REQUIRED NUMBER: "))
        NUMBER6 = float(input("ENTER THE SIXTH REQUIRED NUMBER: "))
        NUMBER7 = float(input("ENTER THE SEVENTH REQUIRED NUMBER: "))
        
        if choice == '6':
            print(NUMBER1, "+", NUMBER2, "+", NUMBER3, "+", NUMBER4, "+", NUMBER5, "+", NUMBER6,  "+", NUMBER7, "=", add_7(NUMBER1, NUMBER2, NUMBER3, NUMBER4, NUMBER5, NUMBER6, NUMBER7))

    # check if user wants another calculation
    # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            
            
         break

        if next_calculation == "yes":
            
            
         continue

        elif choice == '12':
            print(NUMBER1, "-", NUMBER2, "-", NUMBER3, "-", NUMBER4, "-", NUMBER5, "-", NUMBER6, "-", NUMBER7, "=", subtract_7(NUMBER1, NUMBER2, NUMBER3, NUMBER4, NUMBER5, NUMBER6, NUMBER7))

    # check if user wants another calculation
    # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            
            
         break

        if next_calculation == "yes":
            
            
         continue            

        elif choice == '18':
            print(NUMBER1, "*", NUMBER2, "*", NUMBER3, "*", NUMBER4, "*", NUMBER5, "*", NUMBER6, "*", NUMBER7, "=", multiply_7(NUMBER1, NUMBER2, NUMBER3, NUMBER4, NUMBER5, NUMBER6, NUMBER7))

    # check if user wants another calculation
    # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            
            
         break

        if next_calculation == "yes":
            
            
         continue            

        elif choice == '24':
            print(NUMBER1, "/", NUMBER2, "/", NUMBER3, "/", NUMBER4, "/", NUMBER5, "/", NUMBER6, "/", NUMBER7, "=", divide_7(NUMBER1, NUMBER2, NUMBER3, NUMBER4, NUMBER5, NUMBER6, NUMBER7))

    # check if user wants another calculation
    # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            
            
         break

        if next_calculation == "yes":
            
            
         continue