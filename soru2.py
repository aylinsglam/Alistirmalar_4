def sezar():
    x=input("lütfen metni giriniz")
    a=(len(x)**(1/2))
    if int(a)==a: #metin uzunluğunun tam kare olup olmadığını kontrol ediyorum
        b=int(a)
        for i in range(0,b):
            for j in range(0,b):
                print(x[b*j+i],end="")
                # matris şeklindeki metni, sütun sütun yazmak için harfleri bu sırayla yazmalıyız.
    else:
        b=int(a)+1
        for i in range(0,b):
            j=0
            while b*j+i<len(x):
            #metin uzunluğu tamkare olmadığı için, yukarıdaki içerideki for'a denk gelen aralığı
            #kontrol etmemiz lazım
                print(x[b*j+i],end="")
                j+=1
sezar()
