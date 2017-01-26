x=open('proj2.txt').read()
a="";
for i in range(8,len(x)):
    if not x[i-8].isupper() and x[i-7].isupper() and x[i-6].isupper() and x[i-5].isupper() and x[i-4].islower() and x[i-3].isupper() and x[i-2].isupper() and x[i-1].isupper() and not x[i].isupper():
        a=a+x[i-4];
print a
