class Shark:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        """ constructor """
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


def main():
    sammy = Shark("Sammy", 5)
    stevie = Shark("Stevie", 3)
    sammy.swim()
    stevie.be_awesome()
    sammy._age()

if __name__ =="__main__":
    main()


