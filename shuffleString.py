def restoreString(s: str, indices: list) -> str:
    
    output = [None]*len(s)
    
    for i in range(0,len(s)):
        output[indices[i]] = s[i]
        
    
    return "".join(output)


print(restoreString('codeleet',[4,5,6,7,0,2,1,3]))