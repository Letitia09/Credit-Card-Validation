def ConIntLT3(li,a):
    l=[]
    for i in li:
       for j in range(4,17):
          c=i*j
          l.append(c)
    #print(l)
    for i in range(len(l)):
       if l[i] in a:
          return True
          break
    else:
        return False
           
def check_hyphen(a):
    if a[4]=='-' and a[9]=='-' and a[14]=='-' :
        return True
    else:
        return False

def validate_credit(a):
    choices=['4','5','6']
    if a.startswith(tuple(choices)):
        return True
    else:
        return False
n=int(input())
li=['0','1','2','3','4','5','6','7','8','9']
for i in range(n):
    a=input()
    b=a.split('-')
    c=''.join(b)
    #print(c)
    if ConIntLT3(li,a)==False and validate_credit(a) and a.isdigit() and len(a)==16:
        print('Valid')
    elif '-' in a and ConIntLT3(li,c)==False and validate_credit(c)and check_hyphen(a)==True and c.isdigit() and len(c)==16:
        print('Valid')
    else:
         print('Invalid')
       
   
