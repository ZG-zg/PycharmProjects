a = "cn=Manager2,ou=Developer,o=swust,dc=mypaas,dc=com"
s = a.split(',')
s1 = s[0].split('=')
l ={(s1[0],s1[1])}
for i in range(1,len(s)):
    s1 = s[i].split('=')
    k = {(s1[0],s1[1])}
    l.update(k)
"dfdfdfdff"
print(l)