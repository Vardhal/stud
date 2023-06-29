from string import ascii_letters   
 
 
class Helper:
    def __set_name__(self, owner, name):
        return self.name
    
    

    
class Stud:
    
    RUS = "абвгдеёжзийклмнопрстуфхцчшщьыэюя-"
    RUS_UPPER = RUS.upper()
    
    def __init__(self, fn, id, order, form, data):
        self.verify_fn(fn)   
        self.verify_id(id)
        self.verify_order(order)
        self.verify_form(form)
        self.verify_data(data)
    
    @classmethod
    def verify_fn(cls, fn):
        if type(fn) != str:
            raise TypeError ("Must be line")
        
        f = fn.split()
        if len(f) > 3:
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
        
        
    @classmethod
    def verify_order(cls, order):
        if type(order) != str:
            raise TypeError("Must be line")
        
        ord = order.split()
        if len(ord) != 3 or len(ord[0]) != 2 or len(ord[1]) !=2 or len(ord[2]) !=5:
            raise TypeError("Please fill 3 sectors")
        
        for s in ord:
            if not s.isdigit():
                raise TypeError("Please enter digit number")
            
    @classmethod
    def verify_form(cls, form):
        if type(form) != str:
            raise TypeError ("Must be line")
        
        l = ascii_letters + cls.RUS + cls.RUS_UPPER
        
        g = form.split()
        for p in g:
            if len(g) < 1:
                raise TypeError("One symbol should be added")
            if len(p.strip(l)) != 0:
                raise TypeError("Only letters and hyphen")
            
    @classmethod
    def verify_data(cls, data):
        if type(data) != str:
            raise TypeError("Must be line")
        
        dat = data.split()
        if len(dat) != 2:
            raise TypeError("Please fill 3 sectors")
        
            
            
p = Stud("Baba Jora Pasha", 245678, "20 04 20134", 'ochnaya', "september 2013")
print(p)                                             
        
                       
        
