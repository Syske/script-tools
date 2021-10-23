import requests
import os
from Crypto.Cipher import AES   # 用于AES解码

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
            }

def getTsFileUrlList(m3u8Url):
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
    m3u8Url = 'https://vod1.bdzybf1.com/20200819/wMgIH6RN/1000kb/hls/index.m3u8';
    videoList = getTsFileUrlList(m3u8Url);
    print(videoList)
    savePath = "./test"
    fileDownloadWithdecrypt(savePath, videoList);
    fileMerge(savePath);