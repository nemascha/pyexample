#URL Decoder/Encoder
#http://meyerweb.com/eric/tools/dencoder/
#
from urllib2 import urlopen
from urlparse import unquote
import re

urlic = r'https://www.youtube.com/watch?v=DAMM8JVbr8g'

response = urlopen(urlic)
content = response.read()
direct_urls = re.findall(r'"url_encoded_fmt_stream_map":.*?url=(https.*?),', content)

direct_url = unquote(direct_urls[0])

print('DEBUG: url is {}'.format(direct_url))

# d = urlopen(direct_url)
# f = open('testy.mp4', 'wb')
# f.write(d.read())
# d.close()
# f.close()

#direct_urls = re.findall(r'"url_encoded_fmt_stream_map":.*url=(https:*?)(.+)', content)

