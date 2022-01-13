import os,base65536

# mengambil path dan menambahi nama directory lalu melakukan listing file pada dir db
path = os.path.dirname( os.path.abspath(__file__)) + "\\db"
dirl = os.listdir(path)
length_img = len(dirl)
print("Select what image you want to extract the message:")

# memberikan opsi untuk file mana yang akan di extrak persan tersembunyinya
for i in range(len(dirl)):
    print(f"{i}. {dirl[i]}")
selection = input("Input image number > ")
assert 0 <= int(selection) <= len(dirl)
print("Extracted message: ")
os.chdir("db")

with open(dirl[int(selection)],"rb") as m:
    f = m.read()
os.chdir("..")
# melakukan decode pesan pada file dengan panjang file yang telah disesuaikan
print(base65536.decode(f[40755:].decode()))