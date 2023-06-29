from string import ascii_letters   
 
 
class Helper:
    def __set_name__(self, owner, name):
        return self.name
    
    

    
class Stud:
    
    RUS = "абвгдеёжзийклмнопрстуфхцчшщьыэюя-"
    RUS_UPPER = RUS.upper()
    
    def __init__(self, fio):
        self.verify_fio(fio)   
    
    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError ("Должна быть строка")
        
        f = fio.split()
        if len(f) != 3:
            raise TypeError("Фамилия, имя, отчество полное!") 
        
        let = ascii_letters + cls.RUS + cls.RUS_UPPER
        
        for i in f:
            if len(f) < 1:
                raise TypeError("Хотя бы 1 символ")
            if len(i.strip(let)) != 0:
                raise TypeError("Только буквы и дефис")   
        
p = Stud
x = p.verify_fio("ff")
print(x)         
        