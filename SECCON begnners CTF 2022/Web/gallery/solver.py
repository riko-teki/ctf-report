import urllib
import urllib.request

URL = 'https://gallery.quals.beginners.seccon.jp/images/flag_7a96139e-71a2-4381-bf31-adf37df94c04.pdf'

req1 = urllib.request.Request(URL)
req1.add_header('Range', 'bytes=0-10000')

req2 = urllib.request.Request(URL)
req2.add_header('Range', 'bytes=10001-20000')

res1 = urllib.request.urlopen(req1).read()
res2 = urllib.request.urlopen(req2).read()

with open('./flag.pdf', mode='wb') as f:
    f.write(res1+res2)
