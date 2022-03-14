#İlk fonksiyonumuzu SELAMlayalım
print("Selam, Merhaba, Günaydın")

def selam():
  print("Selam, Merhaba, Günaydın")


selam()

#Fonksiyonumuzu biraz daha kişiselleştirelim
print("Selam olsun sana Python")

def selamla(x):
  print("Selam olsun sana ",x)


selamla("Anıl")
selamla("Medium")
selamla("İstanbul")


#Matematiksel bir fonksiyon oluşturalım
def okur_teoremi(a, b, c):
  print(a+b-c)

okur_teoremi(3, 4, 2)

#okur teoreminden çıkan sonucun 2 ile çarpılması
#error
okur_teoremi(3, 4, 2) * 2

#print'in 3 ile çarpılması
#error
print(5) * 2


#Return kullanımı
def okur_teoremi(a, b, c):
  return a+b-c

okur_teoremi(3, 4, 2)
okur_teoremi(3, 4, 2) * 2
okur_teoremi(5, 10, 1) / 7


#Return kullanarak birbiriyle etkileşime girebilen fonksiyonlar yazalım
#toplama, ikiyebolme, dortekleme fonksiyonları oluşturalım
def topla(a,b,c):
  return a+b+c

def ikiyebol(x):
  return x/2

def dortekle(x):
  return x+4

#3 sayıyı birbiriyle toplayarak ikiye bölelim daha sonra dört ekleyelim
print(dortekle(ikiyebol(topla(4,5,6))))


#Fonksiyondan fonksiyon üretme
def ussu_kac_olsun(n):
  def tabani_kac_olsun(x):
    sonuc = x ** n
    return sonuc
  return tabani_kac_olsun

karesi = ussu_kac_olsun(2)
kubu = ussu_kac_olsun(3)
dorduncu = ussu_kac_olsun(4)

karesi(5)
kubu(3)
dorduncu(5)


#Ön Tanımlı Fonksiyon
def daire_cevresi(yaricap,pi=3.14):
  return 2*yaricap*pi

#pi'nin ön tanım değeri vardır. 
#Eğer pi yerine bir değer girilmezse ön tanım değeri geçerli olur
print(daire_cevresi(3))

#(pi'yi 3 kabul ediniz)
print(daire_cevresi(3,3))


#lambda
toplama = lambda a, b, c: a + b + c
toplama(3, 4, 1)

okur_teoremi = lambda a, b, c: a + b - c
okur_teoremi(6, 7, 2)


