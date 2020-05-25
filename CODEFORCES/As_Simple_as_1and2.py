for _ in[0]*int(input()):
    s=input();i=0;r=[]
    while i<len(s):
        if'twone'==s[i:i+5]:i+=3;r+=i,
        if s[i:i+3]in('one','two'):r+=i+2,
        i+=1
    print(len(r))
    print(*r)



