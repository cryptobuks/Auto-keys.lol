import urllib.request
import time
import sys
import os
import re

pages = 0

try:
    while 5 > 1:
        webUrl = urllib.request.urlopen('https://keys.lol/bitcoin/random')
        time.sleep(5)
        data = webUrl.read()
        result = re.findall(r"[-+]?\d*\.\d+|\d+", str(data))
        for i in result:
            if str(i) + " btc" in str(data):
                if float(i) > 0:
                    print(str(i) + " btc")
                    print(webUrl.geturl())
                    with open('ValidWallets', 'a') as appendFile:
                        appendFile.write('{} btc\n'.format(str(i)))
                        appendFile.write('{}\n'.format(webUrl.geturl()))
        pages = pages + 1
        print("Pages read: " + str(pages))
except TimeoutError:
    os.execv(sys.executable, ['python'] + sys.argv)
