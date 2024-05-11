import redis
import _thread

# 为线程定义一个函数
def refreshToken( threadName, spiltContents, redis):
   for line in spiltContents:
      
      token = "access_token:{}".format(line[0:32])
      result = redis.expire(token ,3600*24*15)
      print ("{}: token: {}, result: {}".format( threadName, line[0:32], result))

a=open('D:/workspace/tokenD.txt','r').readlines()
n=30 #份数
qty=len(a)//n if len(a)%n==0 else len(a)//n+1  #每一份的行数

#spilt = a[i*qty:(i+1)*qty]

# 创建两个线程
try:
  r = redis.StrictRedis(host='r-bp1b8l4f2wczfofrwz.redis.rds.aliyuncs.com', port=6379,password='ma44tjdHG=np', db=0)
  for i in range(30):
     _thread.start_new_thread( refreshToken, ("Thread-{}".format(i), a[i*qty:(i+1)*qty], r, ) )
except:
   print ("Error: 无法启动线程")

while 1:
   pass


# 
# 