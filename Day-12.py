class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores=None):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
#   Class Constructor
#
#   Parameters:
#   firstName - A string denoting the Person's first name.
#   lastName - A string denoting the Person's last name.
#   id - An integer denoting the Person's ID number.
#   scores - An array of integers denoting the Person's test scores.
#
# Write your constructor here
    def calculate(self):
        total = sum(scores)
        average = total // len(scores)

        if 90 <= average <= 100:
            return 'O'
        elif 80 <= average < 90:
            return 'E'
        elif 70 <= average < 80:
            return 'A'
        elif 55 <= average < 70:
            return 'P'
        elif 40 <= average < 55:
            return 'D'
        else:
            return 'T'

#   Function Name: calculate
#   Return: A character denoting the grade.
#
# Write your function here


line = input().split()
