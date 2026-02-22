class Virus:
    def __init__(self):
     print("Virus found")
    
    def __del__(self):
       print("Virus terminated")

obj=Virus()
del obj