a=int(raw_input())
b=a
rev=0
while b!=0:
    rev=(rev*10)+(b%10)
    b=b//10
if a==rev:
    print("yes")
else:
    print("no")
