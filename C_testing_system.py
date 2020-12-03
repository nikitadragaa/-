b=int(input())#bot's answer
a=int(input())#student's answer
if (b == 1 and b!=a) or (a==1 and a!=b):
    print("NO")
if (a != 1 and b != 1) or (b==1 and a==1):
    print("YES")