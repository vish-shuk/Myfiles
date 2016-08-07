num = int(raw_input("How many numbers of the fibonacci sequence do you want? : "))

def fibo(num):
    seq = [1, 1]
    n = 2
    while n < num:
        next_num = seq[n-1] + seq[n-2]
        n += 1 
        seq.append(next_num)
    print seq
    
fibo(num)
    
