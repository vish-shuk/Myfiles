listn = range(30)
x = 20
for a in listn:
    if a <= x/2: 
        b = x-a
        if b in listn and a != b and a < b:
            print a, b
        
    
