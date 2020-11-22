satuan = ["", "one", "two", "three", "four", "five", "six" , "seven", "eight", "nine"]

def terbilang(n) :
    if n < 10 :
        return satuan[n]
    elif n >= 1000000000 :
        return terbilang(n//1000000000) + "billion" + terbilang(n % 1000000000)
    elif n >= 1000000 :
        return terbilang(n//1000000) + "million" + terbilang(n % 1000000) 
    elif n >= 1000 :
        return terbilang (n//1000) + "thousand" + terbilang(n % 1000)
    elif n >= 100 :
        return terbilang (n//100) + "hundred" + terbilang(n % 100) 
    elif n >= 20:
        if n // 10 == 2 :
            return "twenty" + terbilang(n % 10)
        elif n // 10 == 3 :
            return "thirty" + terbilang(n % 10)
        elif n // 10 == 5 :
            return "fifty" + terbilang(n % 10)
        elif n // 10 == 8 :
            return "eighty" + terbilang(n % 10)
        else :
            return terbilang (n//10) + "ty" + terbilang(n % 10) 
    else:
        if n == 10:
            return "ten"
        elif n == 11:
            return "eleven"
        elif n == 12:
            return "twelve"
        elif n == 18:
            return "eighteen"
        else:
            return terbilang(n % 10) + "teen"
            
n = 9800000000
print(f"{n} = {terbilang(n)}")