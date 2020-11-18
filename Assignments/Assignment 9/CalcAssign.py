from Calculator import Calculator
from random import randint

x = randint(0,20)
y = randint(0,20)


calc = Calculator

print(x,"+",y,"=",calc().addition(x,y))
print(x,"-",y,"=",calc().subtraction(x,y))
print(x,"*",y,"=",calc().multiplication(x,y))
print(x,"/",y,"=",calc().division(x,y))
print(x,"**",y,"=",calc().exponent(x,y))
print(x,"** (1/2)=",calc().negate(x))
print(x,"* -1=",calc().square_root(x))



    
        



    
    

