import requests;
from bs4 import BeautifulSoup;
import re;
import os;

global index;

def get_blog_list(page, index, file):
  r = requests.get('https://www.cnblogs.com/caoleiCoding/default.html?page={}'.format(page));
  print(r.text);
  soup = BeautifulSoup(r.text,'lxml');
  
  # 搜索class属性为postTitle的div
  for tag in soup.find_all('div', class_='postTitle'):
    print(tag);
    content = tag.span.contents;
    if index == 0 and page == 1:
      index += 1;
      continue;
    print(content)
    title = next(tag.span.children)
    print(str(title));
    title = title.replace('\n', '').strip();
    print(title);
    print(tag.a.href);
    url = tag.a['href']
    print(tag.a['href']);
    file.write('{}. [{}]({})\n'.format(index, title, url));
    index += 1;
    inedx = index;
    
if __name__ == "__main__":
  index = 0;
  file = open('syske-blog-list.md', 'w')
  for page in range(59):
    get_blog_list(page + 1, index, file);