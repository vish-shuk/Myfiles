listn = range(30)
x = 20
for a in listn:
    if a <= x/2: 
        if (x-a) in listn:
            b = x-a
            if a <= b:
                print a, b
        
    
