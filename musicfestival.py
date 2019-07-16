import constant

# Stating all the variables 
numberOfChildren=0# this is one of the variables
numberOfStudents=0# this is one of the variables
numberOfAdults=0
numberOfOaps=0

costOfChild=13.50
costOfStudent=20
costOfAdult=30
costOfOap=20

totalForChild=0
totalForStudent=0
totalForAdult=0
totaleForOap=0


userEnteredAge=""
while(userEnteredAge != "done"):

    userEnteredAge=input("Type stuff: ")

    if userEnteredAge != "done":
      if int(userEnteredAge) > 0:
          totalChildCost=numberOfChildren * costOfChild
          print(str(totalChildCost))
      else:
          print("Not this time !")


 
while Turns<100:# this means that when the amount of turns that have happend is less than 100 you can replay the game 
    Turns=Turns+1 # this will add 1 to the Turns total so once it gts to 100 it will stop the game 
    Number1=int(input("Enter your first number"))# this will make it so you can entre a number and it will be used later on in the game 
    Number2=int(input("Enter your second number"))# this eill make it so you can entre another number and it will be used later on in the game 
    Symbol=input("What would you like to do with these numbers? +,-,/,*")# this is when the user types in a term 
 
    if Symbol == "+": #this tells the program that if the chosen symbol is a + then do the following but if not skip it out 
                 SumAnswer=Number1+Number2# this tells the program to add the numbers that the usre has enterd 
                 print(str(SumAnswer))# this tells the program to add the numbers that the usre has enterd 
                  
    elif Symbol=="-": # this tells the program that if the chosen symbol is a - then do the following but if not skip it out 
                 SumAnswer=Number1-Number2# this tells the program to take the seccond number away from the first number that the usre has enterd 
                 print(str(SumAnswer))# this tells the program to print the answer  
                  
    elif Symbol=="/":# this tells the program that if the chosen symbol is a / then do the following but if not skip it out 
                 SumAnswer=Number1/Number2 # this tells the program to divide the numbers by each other using the numbers the user enterd 
                 print(str(SumAnswer))# this tells the program to print the answer 
                  
    elif Symbol=="*": # this tells the program that if the chosen symbol is a * then do the following but if not skip it out 
                 SumAnswer=Number1*Number2# this tells the program to times the numbers that the usre has enterd 
                 print(str(SumAnswer))# this tells the program to print the answer 
                  
    else:# this tells the program that if the chosen symbol is no valid then tell the user to retry 
                 print("You must enter a +,-,/ or *.Please try again") # this will tell you that you need to retry as you have used an invalid term 
