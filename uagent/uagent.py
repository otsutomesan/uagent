

import requests
import re

def read_page():
  url = 'https://developers.whatismybrowser.com/useragents/explore/software_name/chrome/?order_by=-software_version'
  ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
  headers = {
    'User-Agent': ua,
  }
  session = requests.Session()
  session.headers.update(headers)
  res = session.get(url)
  return res.text

def get_ua_string():
  html = read_page()

  re_str = r'<td class="useragent"><a href="/useragents/parse/(?:\d+)\-chrome\-windows\-blink">(.+?)</a></td>'
  r = re.search(re_str, html)
  ua = ''
  if r:
    ua = r.group(1)
  else:
    # print('------------- not match ...')
    raise Exception('can\'t get user-agent string !')
  return ua

  # for r in re.findall(re_str, html):
  #   print(r)
  
if __name__ == '__main__':
  ua = get_ua_string()
  print(ua)
