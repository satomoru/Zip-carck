import zipfile
 
 
def crack_password(password_list, obj):
   
    idx = 0
    with open(password_list, 'rb') as file:
        for line in file:
            for word in line.split():
                try:
                    idx += 1
                    obj.extractall(pwd=word)
                    print("parol topildi: ", idx)
                    print("parol: ", word.decode())
                    return True
                except:
                    continue
    return False
 
 
password_list = "rockyou.txt"
 
zip_file = "gfg.zip"
 

obj = zipfile.ZipFile(zip_file)
 
cnt = len(list(open(password_list, "rb")))
 
print("qidiruv", cnt,
      "parollar royxati ")
 
if crack_password(password_list, obj) == False:
    print("parol topilmadi !"
