from urllib import request as url
import os

os.system("touch /usr/local/bin/aptman")
f = open("/usr/local/bin/aptman", 'w')
f.write(url.urlopen(url.Request("https://raw.githubusercontent.com/electromeow/aptman/master/main.py",headers={"User-Agent": "Mozilla/5.0"})).read().decode("utf-8"))
f.close()
os.system("chmod +x /usr/local/bin/aptman")
