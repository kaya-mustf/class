




class ogrenci:


    def __init__(self,_ad,_soyad,_numara,_vize,_final):
        self.ad = _ad
        self.soyad = _soyad
        self.numara = _numara
        self.vize = _vize
        self.final = _final


    def ortalama(self):
        return self.vize * 0.4 + self.final * 0.6 
        
    

    def yazdır (self):
        print(f"""
                    ad : {self.ad}
                    soyad : {self.soyad}
                    numara : {self.numara}
                    vize : {self.vize}
                    final : {self.final}
                    ortalama : {self.ortalama()}   
                                                         """)

ogr1 = ogrenci("mustafa","kaya",2017507037,60,48)
ogr1.yazdır()
        



