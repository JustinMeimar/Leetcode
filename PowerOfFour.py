# power of four, no math library using binary representation of num n and bit shifts 
# explanation: bin(16) == 01b0000; all powers of four have multiple of 2 trailing zeros
# knock off two zeros and call recursively on modified n. If the trailing digits of
# bin(n) == '100' then n == 4 and we return true 

def isPowerOfFour(n: int):
    
    if n == 4 or n ==1 :
        
        return True
    # print('cond',n, bin(n), bin(n)[-1])
    if bin(n)[-1] == '0' and bin(n)[-2] == "0":
        n = n >> 2
        return isPowerOfFour(n)
    return False

test = [x for x in range(0,1000000)]
for num in test:
    if isPowerOfFour(num) == True:
        
        print(num,'res:')



