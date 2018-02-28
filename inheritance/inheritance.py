'''
Created on Feb 28, 2018

@author: guan
'''
class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent constructor")
        self.last_name = last_name
        self.eye_color = eye_color
    def show_info(self):
        print(self.last_name + " " + self.eye_color)
        
class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child constructor")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys
        
    def show_info(self):
        print(self.last_name + " " + self.eye_color + " " + str(self.number_of_toys))
# billy_cyrus = Parent("Cyrus", "blue")
# print(billy_cyrus.last_name)
billy_cyrus = Child("Cyrus", "blue", 5)
# print(billy_cyrus.last_name)
# print(billy_cyrus.number_of_toys)
billy_cyrus.show_info()
