import hashlib
vle=input("Vvedite stroku")

x1=str(vle)

#x1.encode('utf-8')
shifr=hashlib.sha1(x1.encode('utf-8')).hexdigest()
print(shifr)
#fb96ef592fd4ea79ed13312e4d6ba31c59068654 :1q1q
#fb96ef592fd4ea79ed13312e4d6ba31c59068654