## Find repeat DNA sequences in a given string. Gene is '10 codons'
## Output: ['AAAAACCCCC','CCCCCAAAAA']

def findRepeatedDnaSequences(s: str):
        start, j = 0, 10
        seen = set()
        repeated = set()

        while start <= len(s) - j:
    
            chunk = s[start:start+j]

            if chunk in seen:
                repeated.add(chunk)
            seen.add(chunk)
            start += 1
            
        print(repeated)
        return repeated


first = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
findRepeatedDnaSequences(first)
# print('hello')

