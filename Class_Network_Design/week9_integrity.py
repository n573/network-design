import hashlib

# MD5
md5 = hashlib.md5()

msg = "Hello World!"
md5.update(msg.encode("utf-8"))

print(md5.digest())
print(md5.hexdigest())

print("")

# SHA 512
sha = hashlib.sha1(msg.encode("utf-8"))
print(sha.digest())
print(sha.hexdigest())