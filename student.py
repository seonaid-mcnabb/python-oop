"""
Practicing OOP concepts with Python
"""
#Initializes an otherwise empty object when you create it.
class Student:
    """
    Commenting
    """
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    def __str__(self):
        return f'{self.name} is from {self.house}'

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

def main():
    """
    Commenting
    """
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()
