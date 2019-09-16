#Sign your name: Catherine_Clifford_______________


# 1.) Write a program that asks someone for their name and then prints their name to the screen?
name=input("what is your first name?")
print("Hello",name)
# 2. Write a a program where a user enters a base and height and you print the area of a triangle.

length=int(input("what is the length of the triangle"))
width=int(input("what is the width of the triangle"))
area=(length*width)/2
print("The area of the triangle is",area)


# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
radius=int(input("What is the radius of the circle?"))
circumference=(radius*2*3.14)
print("The circumference of the circle is", circumference)


# 4. Ask a user for an integer and then print the square root.
integer=int(input("Type in an integer"))
squareroot=integer**2
print("The squareroot of the integer is", squareroot)

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
mass=int(input("Type in mass"))
acceleration=int(input("Type in acceleration"))
force=mass*acceleration
print("The force is", force)
print("Get it?")


