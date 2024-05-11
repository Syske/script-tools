a=open('token.txt','r').readlines()
n=10 #份数
qty=len(a)//n if len(a)%n==0 else len(a)//n+1  #每一份的行数
for i in range(n):
    f=open(str(i+1)+'.txt', 'a')
    f.writelines(a[i*qty:(i+1)*qty])
    f.close()