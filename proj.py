s=open("proj.txt").read()
a="";
for i in range(0,len(s)):
    if s[i] not in "<>!-](?:[^+|*_#@$%&=/\{)}" and s[i]!="\n":
        a=a+s[i];
print a
