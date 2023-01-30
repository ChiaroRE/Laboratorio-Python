import math.py

class Calcolatrice():
    def __init__(self,a,b):
        self.a = a
        self.b = b
        try:
            self.a = float(self.a)
            self.b = float(self.b)
        except ValueError:
            raise Exception("It's impossible to compute given non-number inputs")


    def addizione(self):
        risultato = self.a + self.b 
        return risultato

    def sottrazione(self):
        risultato = self.a - self.b
        return risultato

    def moltiplicazione(self):
        risultato = self.a * self.b
        return risultato

    def divisione(self):
        try:
            risultato = self.a / self.b
            return risultato
        except ZeroDivisionError:
            raise Exception("You can't divide by zero")

    def potenza(self):
        a = int(self.a)
        b = int(self.b)
        risultato = 1
        if b == 0:
            return 1
        else:
            for i in range(1,b):
                risultato = risultato * a
            if b < 0:
                return (1/risultato)
            else:
                return risultato
        
    def modulo(self):
        risultato = self.a % self.b
        return risultato

    def radice(self):
        if(self.a <= 0):
            raise Exception("It's impossible to perform a root operation on a negative number in R")
        risultato = pow(self.a,1/self.b)
        return risultato

    def base2(self):
        a = int(self.a)
        risultato_a = 0
        i = 0
        while(a > 0):
            risultato_a = risultato_a + (int(a % 2) * int(pow(10,i)))
            i += 1
            a = a / 2
        b = int(self.b)
        risultato_b = 0
        i = 0
        while(b > 0):
            risultato_b = risultato_b + (int(b % 2) * int(pow(10,i)))
            i += 1
            b = b / 2
            
        print(risultato_a)
        print(risultato_b)
    
class Test():
    def test_addizione(self):
        c = Calcolatrice(5, 3)
        risultato = c.addizione()
        assert risultato == 8, f"Expected 8, but got {risultato}"
    
    def test_sottrazione(self):
        c = Calcolatrice(5, 3)
        risultato = c.sottrazione()
        assert risultato == 2, f"Expected 2, but got {risultato}"
    
    def test_moltiplicazione(self):
        c = Calcolatrice(2, 3)
        risultato = c.moltiplicazione()
        assert risultato == 6, f"Expected 6, but got {risultato}"
    
    def test_divisione(self):
        c = Calcolatrice(6, 3)
        risultato = c.divisione()
        assert risultato == 2, f"Expected 2, but got {risultato}"
    
    def test_potenza(self):
        c = Calcolatrice(2, 3)
        risultato = c.potenza()
        assert risultato == 8, f"Expected 8, but got {risultato}"
    
    def test_modulo(self):
        c = Calcolatrice(7, 3)
        risultato = c.modulo()
        assert risultato == 1, f"Expected 1, but got {risultato}"
    
    def test_radice(self):
        c = Calcolatrice(9, 2)
        risultato = c.radice()
        assert risultato == 3, f"Expected 3, but got {risultato}"
    
    def test_base2(self):
        c = Calcolatrice(5, 3)
        risultato = c.base2()
        assert risultato == (101, 11), f"Expected (101, 11), but got {risultato}"
        
    