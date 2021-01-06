import string

def sifre():
    x=input("Lütfen metninizi giriniz.")
    alfabe= "abcçdefgğhıijklmnoöprsştuüvyzxqwABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZXQW" 
    yenisi ="qwertyuıopğüasdfghjklşizxcvbnmöçQWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ" #her harfe denk gelen rasgele harfler seçtim
    eslestirme=str.maketrans(alfabe,yenisi) #maketrans metodu bu iki stringin eşleştirilmesini sağlıyor
    
    return x.translate(eslestirme) #bu metod ile x inputuna denk gelen yeni metni döndürür
print(sifre())
    
