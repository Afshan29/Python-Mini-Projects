# Initializing Dictionary 
student_grades = {}

# Function to add a student
def add_student(name, grade):
    student_grades[name] = grade
    print(f"Added {name} with a grade of {grade}")

# Function to update a student
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade  # updating the grade
        print(f"{name}'s grade has been updated to {grade}")
    else:
        print(f"{name} is not found!")

# Function to delete a student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully deleted")
    else:
        print(f"{name} is not found!")     

# Function to display all students
def display_all_students():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
    else:
        print("No student found/added")

# Main function
def main():
    while True:
        print('\nStudents Grades Management System')  
        print("1. Add Student")  
        print("2. Update Student")  
        print("3. Delete Student")  
        print("4. View Students")  
        print("5. Exit")  

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            name = input("Enter Student Name: ")    
            grade = int(input("Enter Student Grade: "))  
            add_student(name, grade)
            
        elif choice == 2:
            name = input("Enter Student Name: ")    
            grade = int(input("Enter Student Grade: "))  
            update_student(name, grade)        

        elif choice == 3:
            name = input("Enter Student Name: ")    
            delete_student(name)     

        elif choice == 4:
            display_all_students()        

        elif choice == 5:   
            print("Closing the program...")
            break

        else:
            print("Invalid Choice!")

# Calling main function
main()

        



