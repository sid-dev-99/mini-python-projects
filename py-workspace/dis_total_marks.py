class Student:

    def __init__(self, name, usn):
        self.name = name 
        self.usn = usn
        self.marks = []
        self.total = 0

    def getthemarks(self):

        for i in range(3):
            mark = float(input(f"enter marks in {i+1} subject: "))
            self.marks.append(mark)
            self.total += mark

    def display(self):
        print(f"name: {self.name}")
        print(f"usn: {self.usn}")
        for i, mark in enumerate(self.marks):
                print(f"subject {i+1} marks: {mark}")
        print(f"total mar: {self.total}")

name = input("enter your name: ")
usn = input("usn: ")
s = Student(name,usn)
s.getthemarks()
s.display()