#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

#Extras:

#Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)



#Ask age in int and name in string
name = input("What is your name? \n")
age =  int(input("How old are you?\n"))

#bonus add on
how_many_times = int(input("How many times would you like to be told the bad news?\n"))



#convert years left to str so it can be concatenated later 
years_left = str(100 - age)

#while loop to print multiple times

i=0
while i < how_many_times:

#Give out the bad news :(
    print ("Hi " + name + " I have a bad new for you ")
    print("You will turn 100 years old in " + years_left + " years, if you are lucky enough to make it till 100 \n" )
    i = i+1

