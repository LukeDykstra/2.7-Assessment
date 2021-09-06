students= ["Tom", "Dick", "Harry"]
outF = open("students.txt", "a") #Opens the bookings text file
outF.write("\n\n***Students***\n") #Opening statement in text file
for student in students: #For every ticket order
    outF.write("{}\n".format(student)) #Prints out the students on a new line
    print(student) #test print in pyscripter
outF.write("***End of list***\n\n")
outF.close() #Closes the bookings text file
print("Printed to text file") #test print statement

from datetime import date

today = date.today()
print("Today's date:", today)