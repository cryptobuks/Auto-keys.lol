import urllib.request
import time
import sys
import os
import re


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
except TimeoutError:
    os.execl(sys.executable, sys.executable, * sys.argv)
