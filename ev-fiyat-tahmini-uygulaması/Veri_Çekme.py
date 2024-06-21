from bs4 import BeautifulSoup
import requests
import pandas as pd

def parse_page(soup):
    bilgiler_div = soup.find("div", id="bilgiler")

    if bilgiler_div:
        veri_elemanlari = bilgiler_div.find_all("div", class_="_1bVOdb")

        bilgiler = {}
        for i in range(0, len(veri_elemanlari), 2):
            baslik = veri_elemanlari[i].text.strip()
            deger = veri_elemanlari[i+1].text.strip()
            bilgiler[baslik] = deger

        return bilgiler
    else:
        return None
    


liste = []
a = 1

while a < 17:

     url = "https://www.emlakjet.com/satilik-daire/istanbul-sisli/" + str(a) + "/" 
     r = requests.get(url)

     soup = BeautifulSoup(r.content, "html.parser")

     div1 = soup.find("div",attrs={"class":"ej64"}) 

     div2 = soup.find_all("div" , attrs= {"class" : "_3qUI9q"}) 

     

     for item in div2: 
      link_sonu = item.a.get("href")
      link_bası = "https://www.emlakjet.com/"
      link = link_bası + link_sonu 
       
       #fiyatı alma
      fiyat_div = item.find("p",attrs = {"class":"_2C5UCT"})
      fiyat_span = fiyat_div.find("span") 
      fiyat_veri = fiyat_span.text.strip() 
 
      
      #şehir, semt,
      ozel_div = item.find("div", attrs={"class": "_2wVG12"})
      if ozel_div:
           adres_span = ozel_div.find("span")
           if adres_span:
               veri = adres_span.text.strip()
               ayrilmis_veri = veri.split(" - ")
               sehir = ayrilmis_veri[0].strip()
               semt = ayrilmis_veri[1].strip()
               

    
     
      r1 = requests.get(link)
      soup1 = BeautifulSoup(r1.content, "html.parser")
      sayfa_bilgileri = parse_page(soup1)
      if sayfa_bilgileri: 
          bulundugu_kat = sayfa_bilgileri.get("Bulunduğu Kat","Bilinmiyor")
          oda_sayisi = sayfa_bilgileri.get("Oda Sayısı","Bilinmiyor")
          net_metrekare = sayfa_bilgileri.get("Net Metrekare" , "Bilinmiyor")
          brut_metrekare = sayfa_bilgileri.get("Brüt Metrekare","Bilinmiyor")
          banyo_sayisi = sayfa_bilgileri.get("Banyo Sayısı", "Bilinmiyor")
          balkon_sayisi = sayfa_bilgileri.get("Tipi", "Bilinmiyor")
          wc_sayisi = sayfa_bilgileri.get("WC Sayısı","Bilinmiyor")
          isitma = sayfa_bilgileri.get("Isıtma Tipi","Bilinmiyor")
          balkon_durumu = sayfa_bilgileri.get("Balkon Durumu","Bilinmiyor")
          yapi_durumu = sayfa_bilgileri.get("Yapı Durumu","Bilinmiyor")
          binanin_yasi = sayfa_bilgileri.get("Binanın Yaşı","Bilinmiyor") 
          kat_sayisi = sayfa_bilgileri.get("Binanın Kat Sayısı","Bilinmiyor") 
          site_durumu = sayfa_bilgileri.get("Site İçerisinde","Bilinmiyor") 
          
      def get_text_contains(label):
           result = soup1.find('li', text=lambda text: text and label in text)
           return 1 if result else 0
      adsl = get_text_contains("ADSL")
      wifi = get_text_contains("Wi-Fi")
      isi_yalitimi = get_text_contains("Isı Yalıtımı")
      asansor = get_text_contains("Asansör") 
      ses_yalitimi = get_text_contains("Ses Yalıtımı")
      sehir_manzarali = get_text_contains("Şehir Manzaralı") 
      yesil_alan_manzarali = get_text_contains("Yeşil Alan Manzaralı")
      deniz_manzarali = get_text_contains("Deniz Manzaralı")
      kamera_sistemi = get_text_contains("Kamera Sistemi") 
      otoban = get_text_contains("Otoban") 
      anayol = get_text_contains("AnaYol")
      otobus = get_text_contains("Otobüs") 
      metro = get_text_contains("Metro") 
      dolmus = get_text_contains("Dolmuş") 
      hastane = get_text_contains("Hastaneye Yakın") 
      cami = get_text_contains("Camiye Yakın")
      okul = get_text_contains("Okula Yakın")

      liste.append([sehir,semt,fiyat_veri,bulundugu_kat,oda_sayisi,net_metrekare,brut_metrekare,banyo_sayisi,wc_sayisi,isitma,
                    balkon_durumu,balkon_sayisi,yapi_durumu,binanin_yasi,kat_sayisi,site_durumu,
                    adsl,wifi,isi_yalitimi,asansor,ses_yalitimi,sehir_manzarali,yesil_alan_manzarali,deniz_manzarali,kamera_sistemi,
                    otoban,anayol,otobus,metro,dolmus,hastane,cami,okul
                    ])
     
      df = pd.DataFrame(liste, columns=["Sehir", "Semt","Fiyat","Bulunduğu Kat","Oda Sayısı","Net Metrekare","Brüt Metrekare",
                                        "WC Sayısı","Isıtma","Balkon Durumu","Balkon Sayısı","Yapı Durumu","Binanin Yaşı","Kat Sayısı", 
                                        "Site Durumu","ADSL","Wifi","Isı Yalıtımı","Asansor","Ses Yalıtımı","Sehir Manzarası",
                                        "Yesil Alan Manzarası","Deniz Manzarası","Kamera Sistemi","Otoban","Anayol","Banyo Sayısı"
                                        ,"Otobus","Metro","Dolmus","Hastane","Cami","Okul"])
                            
      df.to_csv('emlak_listesi.csv', index=False)
  
      
     a = a + 1
     print(a)
  
    




