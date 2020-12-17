#default arguments
def display(name, course = "Btech"):
    print("Name : " + name)
    print("Course : ", course)

display(course = "BCA", name= "Arav")

display(name="Reyansh")

def display(name,marks,course = "BTech"):
    print("Name : " + name)
    print("Course : ", course)
    print("Marks :", marks)

display(name="Reyansh", marks=90)
