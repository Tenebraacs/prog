# Python program a másodfokú egyenlet gyökereinek megtalálásához
import math 
  
  
# függvény a gyökerek megtalálásához
def equationroots( a, b, c): 
  
    # diszkrimináns kiszámítása képlet segítségével
    dis = b * b - 4 * a * c 
    sqrt_val = math.sqrt(abs(dis)) 
      
    # a feltétel ellenőrzése a diszkrimináns szempontjából
    if dis > 0: 
        print("Valódi és különböző gyök") 
        print((-b + sqrt_val)/(2 * a)) 
        print((-b - sqrt_val)/(2 * a)) 
      
    elif dis == 0: 
        print("Valódi és azonos gyök") 
        print(-b / (2 * a)) 
      
    # amikor a diszkrimináns kevesebb 0-nál
    else:
        print("Öszetett gyök") 
        print(- b / (2 * a), " + i", sqrt_val) 
        print(- b / (2 * a), " - i", sqrt_val) 
  
# Futtató program
a = float(input("Íja be az a értéket:"))
b = float(input("Íja be a b értéket:"))
c = float(input("Íja be a c értéket:"))
  
# Ha az a = 0 akkor helytelen az egyenlet 
if a == 0: 
        print("Helyes másodokú egyenlet összetevőket adjon meg!") 
  
else:
    equationroots(a, b, c)