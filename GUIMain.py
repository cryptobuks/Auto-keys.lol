import urllib.request
import time
import os
from tkinter import *
import threading
running = False
pages = 0
print("Close this window to close the program.")


def run():
    try:
        while running is True:
            webUrl = urllib.request.urlopen('https://keys.lol/bitcoin/random')
            time.sleep(5)
            data = webUrl.read()
            result = re.findall(r"[-+]?\d*\.\d+|\d+", str(data))
            for i in result:
                if str(i) + " btc" in str(data):
                    if float(i) > 0:
                        with open('ValidWallets.txt', 'a') as appendFile:
                            appendFile.write('{} btc\n'.format(str(i)))
                            appendFile.write('{}\n'.format(webUrl.geturl()))
            if running is False:
                break
            global pages
            pages = pages + 1
            output.config(text="Pages read: {}".format(str(pages)))
    except TimeoutError:
        os.execv(sys.executable, ['python'] + sys.argv)


def start():
    output.config(text="Started reading on page {}".format(pages))
    global running
    running = True
    thread = threading.Thread(target=run)
    thread.start()


def stop():
    output.config(text="Stopped on page {}".format(pages))
    global running
    running = False


master = Tk()
w = Canvas(master, width=300, height=100)
w.pack()
master.title('Auto keys GUI VERSION 1.0')
output = Label(master, text="Messages will show up here", font=("Courier", 12))
output.pack()
button = Button(w, text='Start', width=10, font=("Courier", 20), fg="green", command=lambda: start())
button.grid(column=1, row=2)
stopButton = Button(w, text='Stop', width=10, font=("Courier", 20), fg="red", command=lambda: stop())
stopButton.grid(column=2, row=2)
master.mainloop()
