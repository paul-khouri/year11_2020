class Store:

    def __init__(self):
        self.colour = "rgb(0,0,0,0)"





class Shark:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        """ constructor """
        store.colour = "rgb(255,255,255,1)"
        print("This is the constructor")
        
    def swim(self):
        """ what the shark is doing"""
        print(self.name+" is swimming")
        
    def be_awesome(self):
        """ what the shark is being"""
        print(self.name+" is being awesome")

    def _age(self):
        """ how old is it """
        print(self.name +" is "+str(self.age)+" years old")

store = Store()
shark = Shark("sam", 10)
print(store.colour)
