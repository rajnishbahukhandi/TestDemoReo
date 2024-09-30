# Class representing a simple student record system
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    # Method to display student details
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

# Function to save student records to a file
def save_to_file(student_list, filename="students.txt"):
    try:
        with open(filename, 'w') as file:
            for student in student_list:
                file.write(student.display_info() + '\n')
        print("Student data saved successfully.")
    except Exception as e:
        print(f"Error occurred while saving: {e}")

# Function to read student records from a file
def read_from_file(filename="students.txt"):
    try:
        with open(filename, 'r') as file:
            print("Reading student data from file:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main execution block
if __name__ == "__main__":
    # Creating a list of students
    students = [
        Student("Alice", 20, "A"),
        Student("Bob", 19, "B+"),
        Student("Charlie", 21, "A-")
    ]

    # Display each student's info
    for student in students:
        print(student.display_info())

    # Save student data to a file
    save_to_file(students)

    # Read student data from the file
    read_from_file()
