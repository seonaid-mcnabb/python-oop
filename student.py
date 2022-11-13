"""
Practicing OOP concepts with Python
"""
#Initializes an otherwise empty object when you create it.
class Student:
    """
    Commenting
    """
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "HufflePuff","Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus
    
    def __str__(self):
        return f'{self.name} is from {self.house} and their patronus is {self.patronus}'
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "Horse"
            case "Otter":
                return "Otter"
            case "Jack Russell Terrier":
                return "Bar"
            case _:
                return "Wand with no magic"

def main():
    """
    Commenting
    """
    student = get_student()
    print("Expecto patronum!")
    print(student.charm())

def get_student():
    """
    Commenting
    """
    name = input("Name: ")
    house = input("House: ")
    patronus = input ("Patronus: ")
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()
