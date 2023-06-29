from string import ascii_letters   
 
 
class Helper:
    def __set_name__(self, owner, name):
        return self.name
    
    

    
class Stud:
    
    RUS = "абвгдеёжзийклмнопрстуфхцчшщьыэюя-"
    RUS_UPPER = RUS.upper()
    
    def __init__(self, fn, id):
        self.verify_fn(fn)   
        self.verify_id(id)
    
    @classmethod
    def verify_fn(cls, fn):
        if type(fn) != str:
            raise TypeError ("Must be line")
        
        f = fn.split()
        if len(f) != 3:
            raise TypeError("Please enter full name!") 
        
        let = ascii_letters + cls.RUS + cls.RUS_UPPER
        
        for i in f:
            if len(f) < 1:
                raise TypeError("One symbol should be added")
            if len(i.strip(let)) != 0:
                raise TypeError("Only letters and hyphen")
           
    @classmethod
    def verify_id(cls, id):
        if type(id) != int:
            raise TypeError("Must be digits")
        
        if len(id) > 6:
            raise ValueError("id can`t have more than 6 values")
        
                       
        
