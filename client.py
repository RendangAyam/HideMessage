import base65536
import os

with open("meme.png","rb") as x:
    f = x.read()
# membaca file dan print panjang dari file tersebut
print(len(f))
# masukan kata-kata yang akan dihidden di gambar
text = input("Input your secret : ")
text = text.encode()
# encode kata-kata
encoded = base65536.encode(text)
length_enc = len(encoded)
# memasukan kata-kata setelah IEND
newfile = f + encoded.encode()
os.chdir("db")
# membuat file baru didalam db directory
with open("newmeme_{}.png".format(length_enc),"wb") as n:
    n.write(newfile)
n.close()
os.chdir("..")
