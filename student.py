"""
Practicing OOP concepts with Python
"""
#Initializes an otherwise empty object when you create it.
class Student:
    """
    Commenting
    """
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "HufflePuff","Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f'{student.name} is from {student.house}')

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()
