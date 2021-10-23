import requests
import re
import os
import _thread
from concurrent.futures import ThreadPoolExecutor, as_completed
from Crypto.Cipher import AES   # 用于AES解码
 
 
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
            }

def getTsList(index_url, m3u8Url):
    # 获取cookie        
    res = requests.get(url=index_url, headers=headers)
    cookies = res.cookies.items()
    print(cookies)
    cookie = ''
    for name, value in cookies:
      cookie += '{0}={1};'.format(name, value)
    headers['Cookie'] = cookie;
    print(cookie)
    msu8ViedoUrl = '{}/index.m3u8'.format(m3u8Url);
    rs = requests.get(url = msu8ViedoUrl, headers=headers).text
    print(rs)
     
    pattern = re.compile(r'\S+');
    m = pattern.match(rs);
    url = re.findall('\\S+', rs);
    ts_src_url = url[2]
    ts_video_url = '{}/{}'.format(m3u8Url, ts_src_url);
    print(ts_video_url)
    ts_rs = requests.get(url = ts_video_url, headers=headers).text
    print(ts_rs)
    list_content = ts_rs.split('\n');
    player_list = []
    index = 1;
    for line in list_content:
      # 以下拼接方式可能会根据自己的需求进行改动
      if '#EXTINF' in line:
        continue;
      else:
        if line.endswith('.ts'):
          href = m3u8Url + line
          player_list.append(href)
          index+=1;
    print('数据列表组装完成-size: {}'.format(len(player_list)));
    return player_list;
    
    
def getTsUrlList(index_url, m3u8Url):
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
            }
    # 获取cookie        
    res = requests.get(url=index_url, headers=headers)
    cookies = res.cookies.items()
    print(cookies)
    cookie = ''
    for name, value in cookies:
      cookie += '{0}={1};'.format(name, value)
    headers['Cookie'] = cookie;
    print(cookie)
    msu8ViedoUrl = '{}/index.m3u8'.format(str(m3u8Url));
    ts_rs = requests.get(url = msu8ViedoUrl, headers=headers).text
    print(ts_rs)
    list_content = ts_rs.split('\r\n');
    print('list_content:{}'.format(list_content))
    player_list = []
    index = 1;
    for line in list_content:
      # 以下拼接方式可能会根据自己的需求进行改动
      if '#EXTINF' in line:
        continue;
      else:
        if line.endswith('.ts'):
          href = '{}/{}'.format(m3u8Url, line);
          player_list.append(href)
          index+=1;
    print('数据列表组装完成-size: {}'.format(len(player_list)));
    return player_list;


def getTsFileUrlList(m3u8Url):
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
            }
    ts_rs = requests.get(url = m3u8Url, headers=headers).text
    print(ts_rs)
    list_content = ts_rs.split('\n');
    print('list_content:{}'.format(list_content))
    player_list = []
    index = 1;
    for line in list_content:
      # 以下拼接方式可能会根据自己的需求进行改动
      if '#EXTINF' in line:
        continue;
      elif line.endswith('.ts'):
        player_list.append(line)
    print('数据列表组装完成-size: {}'.format(len(player_list)));
    return player_list;

    
def fileDownload(fileSavePath, player_list):
    if not os.path.exists(fileSavePath):
        os.mkdir(fileSavePath);
    for index, url in enumerate(player_list):
        ts_video = requests.get(url = url, headers=headers)
        with open('{}/{}.ts'.format(fileSavePath, str(index + 1)), 'wb') as file:
            file.write(ts_video.content)
            print('正在写入第{}个文件'.format(index + 1))
    print('下载完成');
    
    
def fileDownloadWithdecrypt(fileSavePath, player_list):
    if not os.path.exists(fileSavePath):
        os.mkdir(fileSavePath);
    for index, url in enumerate(player_list):
        ts_video = requests.get(url = url, headers=headers)
        with open('{}/{}.ts'.format(fileSavePath, str(index + 1)), 'wb') as file:
            context = decrypt(ts_video.content);
            file.write(context)
            print('正在写入第{}个文件'.format(index + 1))
    print('下载完成');
    
    
def fileMerge(filePath):
    c = os.listdir(filePath)
    with open('%s.mp4' % filePath, 'wb+') as f:
      for i in range(len(c)):
        x = open('{}/{}.ts'.format(filePath, str(i + 1)), 'rb').read()
        f.write(x)
    print('合并完成')
    
    
def decrypt(context):
    key =  b'2cd1da2aedacaec8';
    cryptor = AES.new(key, AES.MODE_CBC, key);
    decrypt_content = cryptor.decrypt(context);
    return decrypt_content;
    
    
if __name__ == '__main__':
#    m3u8Url = 'https://vod1.bdzybf1.com/20200819/wMgIH6RN/1000kb/hls/index.m3u8';
#    videoList = getTsFileUrlList(m3u8Url);
#    print(videoList)
    savePath = "./test"
#    fileDownloadWithdecrypt(savePath, videoList);
    fileMerge(savePath);
#    with ThreadPoolExecutor(max_workers=20) as taskThread: 
#        for i in range(0, len(videoList), 20):
#            list = videoList[i:i + 20];
#            taskList = []
##           子线程
#            task = taskThread.submit(fileDownloadWithdecrypt, savePath, list)  
#            taskList.append(task)
#        for future in as_completed(taskList):
#            pass
#    fileMerge(savePath);
#  m3u8Url = 'http://223.110.243.171/PLTV/3/224/3221227204';
#  m3u8Url = 'https://6omm.com/new/hls/5a22eee778e341bc987d8f4fb67b4034';
#  index_url = 'https://3bmmyqcw.life/';
#  index_url = 'https://3bmmyqcw.life/';
#  player_list = getTsUrlList(index_url, m3u8Url);
#  print(player_list)
#  print(int(len(player_list)/20 + 1))
#  newList = [];
##   线程池
#  savePath = "./test"
#  with ThreadPoolExecutor(max_workers=20) as taskThread: 
#      for i in range(0, len(player_list), 20):
#          list = player_list[i:i + 20]
#          newList.append(list);        
#          taskList = []
##           子线程
#          task = taskThread.submit(fileDownload, savePath, list)  
#          taskList.append(task)
#      for future in as_completed(taskList):
#        pass
#  fileMerge(savePath)