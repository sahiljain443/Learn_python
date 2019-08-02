#Capitalize first character of every word

def first_Capitalize(str):
    l = str.split()
    
    for i in range(len(l)):
        l[i] = l[i][0].upper() + l[i][1:]
    return (' '.join(l))
    
    
print (first_Capitalize('whats up'))