class student: 
    grade= 8
    name= "Aryan"

    def indtrodution(self):
        print("I am a student")

    def details(self):
        print("Hi my name is", self.name)
        print("I go in", self.grade, "grade")

ob = student()
ob.indtrodution()
ob.details()
