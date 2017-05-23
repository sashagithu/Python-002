from skpy import Skype
from skpy import SkypeContacts
import cfg
i = 0
query = input("Enter value: ")
sk = Skype(cfg.login, cfg.password)
sk2 = SkypeContacts(sk)
search = sk2.search(query=query)
lenth = len(search)
f = open('output.txt', 'w')
while i < lenth:
    item = int(i)
    info = search[item]
    info = str(info)
    f.write(info + '\n' + '\n')
    i += 1
