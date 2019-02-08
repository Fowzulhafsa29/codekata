InputValue=raw_input()
a,b,c=InputValue.split(" ")
a,b,c=int(a),int(b),int(c)
if((a>b) and(a>c)):
    print(a)
elif((b>a) and (b>c)):
    print(b)
elif((c>a) and(c>b)):
    print(c)
