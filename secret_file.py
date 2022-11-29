import hashlib
import getpass


#원본 비밀번호
passwd = 'safe2580!'

#비밀번호 해싱
h = hashlib.sha256()
h.update(passwd.encode('utf-8'))

#해싱된 비밀번호
h_passwd = h.digest()
print(h_passwd)