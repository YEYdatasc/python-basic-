#sınıf ve örnek kavramları (class ve instance)
#class oluşturma 
#özellik ve metotları(attribute and methods)

class calisan:
    def __init__(self,a,b,c):
        self.name=a
        self.surname=b
        self.age=c
#self oluşturduğum değişkeni ifade etmekle beraber burada calisan1'i temsil etmektedir.
#a,b,c ve class değişkenlerdir, ve örneğe göre değişmektedir.
calisan1=calisan("Ali","Veli",20)
print(calisan1.name,calisan1.surname,calisan1.age)


class calisan():
    def __init__(self,a,b,c):     #self oluşturulan değişkeni temsil eder,yani calisan1 i temsil eder.
        self.name=a               #calisan1'in name değişkeni fonskiyondan gelen değişkendir.
        self.surname=b
        self.age=c
    def show_info(self):
        print(f"Ad:{self.name}  Soyad:{self.surname}  Yaş:{self.age}")
        
calisan1=calisan("Ali","Veli",20)
print(calisan1.name,calisan1.surname,calisan1.age)

calisan1.age        
calisan1.name
calisan1.surname

calisan2=calisan("Ahmet","Mehmet",25)
print(calisan2.name,calisan2.surname,calisan2.age) 
calisan1.show_info()
calisan2.show_info()
...................................
#class variables-instance variables 
#zam oranı ifadesi class içindeki her instanceiçin geçerlidir.
class calisan:
   zam_orani=1.2
   def __init__(self,isim,maas):
        self.isim=isim
        self.maas=maas  
calisan2=calisan("Ahmet",6000)
print(calisan1.isim)        
print(calisan2.maas)
print(calisan1.__dict__)    
print(calisan2.__dict__)   #calisan 2 için değerleri sözlük olarak yansıtır.
print(calisan.zam_orani)
print(calisan1.zam_orani)
print(calisan2.zam_orani)

calisan.zam_orani=1.2
print(calisan.zam_orani)
print(calisan1.zam_orani)
print(calisan2.zam_orani)

..........................................


class kisi:
    zam_orani=1.1
    kisi_sayisi= 0
    def __init__(self,isim,yas):
        self.isim=isim
        self.yas=yas 
        kisi.kisi_sayisi+=1
        
    def bilgilerini_soyle(self): #instance method
        return f" Ad: {self.isim} yas: {self.yas}"
    @classmethod
    def kisi_sayisini_soyle(cls):
        return cls.kisi_sayisi
        


        
        

        
print(kisi.kisi_sayisi)
kisi1=kisi("Ali",20)
kisi2=kisi("Veli",30)
print(kisi.kisi_sayisi)
print(kisi1.bilgilerini_soyle())

#inheritance(kalıtım)

 class Calisan:
     zam_orani=1.1
     def __init__(self,isim,soyisim,maas):
        self.isim=isim
        self.soyisim=soyisim
        self.maas=maas
        self.email=isim+soyisim+ "@sirket.com"
     def bilgileri_goster(self):
        return "Ad: {} Soyad: {} Maas: {} Email:{}" .format(self.isim,self.soyisim,self.maas,self.email)
                    
 class Yazilimci(Calisan):
     def __init__(self,isim,soyisim,maas,bildigi_dil):
         super().__init__(isim,soyisim,maas) # super komutu ile yukardaki calisan klasındaki bütün attributler taşınmış oldu ve hangi attributtları miras aldıgını söyledi.
         self.bildigi_dil=bildigi_dil
     zam_orani=1.2
     def bilgileri_goster(self):
         return "Ad: {} Soyad: {} Maas: {} Email: {} Dil {}" .format(self.isim,self.soyisim,self.maas,self.email,self.bildigi_dil)
           
calisan1=Calisan("Ali","Caliskan",5000)
calisan2=Calisan("Veli","Uzun",6000)
yazilimci2=Yazilimci("Fatma","Ay",8000, "Python")


class Yonetici(Calisan):
    def __init__(self,isim,soyisim,maas,calisanlar=None):
        super().__init__(isim,soyisim,maas)
        if calisanlar == None:
            self.calisanlar= []
        else:
            self.calisanlar=calisanlar 
    def calisan_ekle(self,calisan):
        if calisan not in self.calisanlar:
            self.calisanlar.append(calisan)
    
    def calisan_sil(self,calisann):
        if calisan in self.calisanlar:
            self.calisanlar.remove(calisan)
    def calisanları_goster(self):
        for calisan in self.calisanlar:
            print(calisan.bilgileri_goster())
    
yonetıcı1=Yonetici("Metın","Ali",10000)
yonetıcı1.calisan_ekle(calisan1)
yonetıcı1.calisan_ekle(yazilimci2)
yonetıcı1.calisanları_goster()    
 print("************") 
yonetıcı1.calisan_sil(calisan1)  
yonetıcı1.calisanlari_goster()
#sorumlu oldugu kişiler yonetıcı oluştururuken, oluşturuldu.
#yukardaki listede ise ayrı olarak eklendi.
yonetıcı2=Yonetici("Feyyaz","Beşiktaş",11000,[yazilimci2,calisan1])
yonetıcı2.calisanları_goster()


    
            










