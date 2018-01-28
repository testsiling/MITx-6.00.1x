'''
MIT 6.00.1x Week 1 Problem set
Problem 3
'''
index = 0
maxlen = 0
for i in range(len(s) - 1):  
    long = 1  
    for j in range(i, len(s) - 1):        
        if ord(s[j+1]) - ord(s[j]) >= 0:
            long += 1         
        else:     
            break       
    if long > maxlen:
        maxlen = long
        index = i
print('Longest substring in ' + s + ' order is: ' + s[index : index+maxlen])