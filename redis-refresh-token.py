import redis
import _thread

# 为线程定义一个函数
def refreshToken( threadName, spiltContents, redis):      
      token = "access_token:{}".format(line[0:32])
      # userVerificationCode.login.15914428356.123456 "2041-03-01 22:18:28"
      result = redis.expire(token ,3600*24*15)
      print ("{}: token: {}, result: {}".format( threadName, line[0:32], result))



r = redis.StrictRedis(host='r-bp1b8l4f2wczfofrwz.redis.rds.aliyuncs.com', port=6379,password='ma44tjdHG=np', db=80)


# 
# 