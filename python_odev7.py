"""
    module1 (db)      : urunler
    module2 (methods) : urunEkle(), urunGuncelle(), urunleriGetir()
    module3 (app)     :

        yeni ürün ekleme => urunEkle("iphone 15", 60000)
        ürün güncelle    => urunGuncelle(1, "iphone 15 pro", 80000)
        ürünleri listele => urunleriGetir() 
"""

urunler=[]

def urunEkle(urunAdi, fiyat):
    urun={"id": len(urunler) + 1,"urunAdi": urunAdi, "fiyat": fiyat}
    urunler.append(urun)
    return urun 

def urunGuncelle(urunId, yeniUrunAdi, yeniFiyati):
    for urun in urunler:
        if urun["id"]== urunId:
            urun["urunAdi"]=yeniUrunAdi
            urun["fiyat"]= yeniFiyati
            return urun
    return None

def urunleriGetir():
    return urunler

urunEkle("Iphone 15", 60000)

urunGuncelle(1, "Iphone 15 Pro", 80000)

liste=urunleriGetir()
for urun in liste:
    print(f"ID: {urun['id']}, Ürün:{urun['urunAdi']}, Fiyat: {urun['fiyat']}")