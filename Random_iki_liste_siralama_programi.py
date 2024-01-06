#random modülünü sayesinde rastgele sayılar oluşturabiliriz
import random

#iki boş liste oluşur --> list1 ve list2
list2 = []
list1 = []

#her biri 1 ile 50 arasında 10 tane rastgele sayılar üret
for i in range(1,11):

    sayi= random.randint(1,50) #random değer oluştur ve liste1'e ekle
    list1.append(sayi)

    sayi= random.randint(1,50) #random değer oluştur ve liste2'ye ekle
    list2.append(sayi)

#oluşturulan listeleri ekrana yaz
print("\nListe 1:", list1)
print("\nListe 2:", list2)

#iki listeyi tek listede topla ve yazdır
toplam_liste= list2+list1 
print("\nBirlestirilmis liste:",toplam_liste)

#listenin eleman sayısını hesapla
eleman_sayisi = 0 
for i in toplam_liste:
    eleman_sayisi += 1


#sıralama işlemini gerçekleştiren iki for döngüsü
#eleman sayısı kadar döndsün
for i in range(eleman_sayisi):

    for j in range(eleman_sayisi):
        
        if toplam_liste[i] < toplam_liste[j]: 
             #elemanları yer değiştirin küçükten büyüğe sırala
            toplam_liste[i] , toplam_liste[j] =  toplam_liste[j] , toplam_liste[i]
        

#sıralanmış listeyi ekrana yazdır
print("\nSirali yeni liste:",toplam_liste)