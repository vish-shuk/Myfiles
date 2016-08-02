print "Lists out the divisors of a given number"

ip = int(raw_input("Enter a number: "))
div = []

def divisor(ip):
    for a in range(1, ip/2 + 1):
        if ip % a == 0:
            div.append(a)
    div.append(ip)            
    print "The divisors of %d are: " %ip, div

divisor(ip)

if len(div) % 2 == 0:
    print "%d is not a perfect square" %ip
else:
    sqrt = div[len(div)/2]
    print "%d is a perfect square whose square root is %d" %(ip, sqrt)

