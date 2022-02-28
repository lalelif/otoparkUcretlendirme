def main():
    devam="e"
    GAZI_INDIRIM=0 # indirim uygulanması durumunda gaziler ücret ödemediği için 0'çarpma yapılır
    ENGELLI_INDIRIM=0.5
    MOTOSIKLET_KATSAYI=1
    BINEK_KATSAYI=2
    MINIBUS_OTOBUS_KATSAYI=3
    KAMYON_TIR_KATSAYI=4
    TON_UCRET=2.5

    top_arac=0 #toplam araç sayısını tutar
    # türlere göre araç sayısını tutar
    motosiklet=0
    binek=0
    minibus=0
    otobus=0
    kamyon=0
    tir=0

    top_gelir=0 #toplam geliri tutar
    #türlere göre gelirleri tutar
    motosiklet_gelir=0
    binek_gelir=0
    minibus_gelir=0
    otobus_gelir=0
    kamyon_gelir=0
    tir_gelir=0

    #türlere göre toplam süreyi tutar
    motosiklet_sure=0
    binek_sure=0
    minibus_sure=0
    otobus_sure=0
    kamyon_sure=0
    tir_sure=0

    bir_tondan_az_binek=0 # ağırlığı bir tondan az binek araçların sayısını tutar
    on_tondan_fazla_okt=0
    otuz_dkden_az_mb=0
    bir_gunden_fazla_mo=0
    otuz_gun_veya_bin_liradan_fazla=0
    gazi_engelli_sure=0
    gazi_engelli_arac=0
    uc_saaten_uzunkalan_indirimli=0
    max_sure=0
    max_surenin_geliri=0
    max_gelir=0
    max_gelirin_suresi=0
    while devam=="e" or devam=="E":
        ucret = 0
        gun=0
        saat=0
        dk=0
        kod_adi=""
        plaka=input("Araç plakası:")
        kod=int(input(" Araç sınıfı kodu:(1-6 arasında)"))
        while kod<1 or kod>6:
            kod = int(input(" Araç sınıfı kodu:(1-6 arasında)"))
        agirlik=float(input("Araç ağırlığı(kg):"))
        while agirlik<=0:
            agirlik = float(input("Araç ağırlığı(kg):"))
        sure=int(input("Otoparkta kalınan süre(dk):(0'dan büyük bir tam sayı)"))
        while sure<=0:
            sure = int(input("Otoparkta kalınan süre(dk):(0'dan büyük bir tam sayı)"))
        ad_soyad=input("Sürücü ad soyad:")
        if kod==1 or kod==2:
            ozel_durum=input("Sürücünün özel durumu:Yok/Gazi/Engelli(Y/y/G/g/E/e)") # motosiklet veya binek sınıfı araç ise sor
            while not (ozel_durum=="Y" or ozel_durum=="y" or ozel_durum=="E" or ozel_durum=="e" or ozel_durum=="G" or ozel_durum=="g"):
                ozel_durum = input("Sürücünün özel durumu:Yok/Gazi/Engelli(Y/y/G/g/E/e)")
            if ozel_durum == "G" or ozel_durum == "g" or ozel_durum=="E" or ozel_durum=="e":
                if sure / 60 > 3:
                    uc_saaten_uzunkalan_indirimli += 1
                gazi_engelli_sure += sure
                gazi_engelli_arac += 1


        while sure>0:

            if (sure/60)<1:
                ucret+=3
                dk=sure
                sure=0
            elif (sure/60)<3:
                ucret+=5
                saat=sure//60

                sure = sure - saat * 60
            elif (sure / 60) < 5:
                ucret+=7
                saat = sure // 60

                sure = sure - saat * 60
            elif (sure / 60) < 10:
                ucret+=10
                saat = sure // 60

                sure = sure - saat * 60
            elif (sure / 60) < 24:
                ucret+=14
                saat = sure // 60

                sure=sure-saat*60
            elif (sure / 60) ==24:
                ucret+=15
                gun+=1
                saat=0

                sure = sure - 24 * 60
            else:
                ucret+=15
                gun+=1
                sure=sure-24*60
        sure=gun*24*60+saat*60+dk
        agirlik_ucret=(agirlik // 1000) * TON_UCRET

        if kod==1:
            kod_adi="Motosiklet"
            ucret= ucret*MOTOSIKLET_KATSAYI+agirlik_ucret
            if ozel_durum=="G" or ozel_durum=="g":
                ucret=ucret*GAZI_INDIRIM
            elif ozel_durum=="E" or ozel_durum=="e":
                ucret= ucret*ENGELLI_INDIRIM
            motosiklet_gelir+=ucret
            motosiklet+=1
            motosiklet_sure=sure
            if motosiklet_sure<=30:
                otuz_dkden_az_mb+=1

        elif kod==2:
            kod_adi="Binek"
            ucret =ucret*BINEK_KATSAYI+agirlik_ucret
            if ozel_durum=="G" or ozel_durum=="g":
                ucret=ucret*GAZI_INDIRIM
            elif ozel_durum=="E" or ozel_durum=="e":
                ucret= ucret*ENGELLI_INDIRIM
            binek_gelir+=ucret
            binek+=1
            binek_sure=sure
            if agirlik<1000:
                bir_tondan_az_binek+=1
            if binek_sure<=30:
                otuz_dkden_az_mb+=1
            if max_gelir > ucret:
                max_gelir = ucret
                max_gelirin_suresi = sure

        elif kod==3:
            kod_adi="Minibüs"
            ucret= ucret*MINIBUS_OTOBUS_KATSAYI+agirlik_ucret
            minibus_gelir=ucret
            minibus+=1
            minibus_sure = sure
            if minibus_sure/(24*60)>1:
                bir_gunden_fazla_mo+=1
        elif kod==4:
            kod_adi="Otobüs"
            ucret = ucret*MINIBUS_OTOBUS_KATSAYI+agirlik_ucret
            otobus_gelir+=ucret
            otobus+=1
            otobus_sure = sure
            if agirlik>10000:
                on_tondan_fazla_okt+=1
            if otobus_sure / (24 * 60) > 1:
                bir_gunden_fazla_mo += 1
        elif kod==5:
            kod_adi="Kamyon"
            ucret= ucret*KAMYON_TIR_KATSAYI+agirlik_ucret
            kamyon_gelir+=ucret
            kamyon+=1
            kamyon_sure=sure
            if agirlik>10000:
                on_tondan_fazla_okt+=1
        else:
            kod_adi="Tır"
            ucret= ucret*KAMYON_TIR_KATSAYI+agirlik_ucret
            tir_gelir+=ucret
            tir+=1
            tir_sure=sure
            if agirlik>10000:
                on_tondan_fazla_okt+=1
        if ucret>1000 or sure>30*24*60:
            otuz_gun_veya_bin_liradan_fazla+=1

        top_arac=motosiklet+binek+minibus+otobus+kamyon+tir

        if sure>max_sure:
            max_sure=sure
            max_surenin_geliri=ucret

        top_gelir += ucret
        print("BİLGİ FİŞİ")
        print("**********")
        print("Araç plakası:",plaka)
        print("Araç sınıfı:",kod)
        print("Araç sınıfı adı:",kod_adi)
        print("Araç ağırlığı(kg):",agirlik)
        print("Otoparkta kaldığı süre: ",gun," gün, ",saat," saat, ",dk," dakika")
        print("Sürücü ad soyad:",ad_soyad)

        if ( kod==1 or kod==2) :
            print("Sürücünün özel durumu:",ozel_durum)
            if ozel_durum=="G" or ozel_durum=="g":
                print(" Uygulanan indrim oranı:%100")
                print("Otopark ücreti:{0}TL".format(round(ucret*GAZI_INDIRIM,2)))
            elif ozel_durum=="E" or ozel_durum=="e":
                print(" Uygulanan indrim oranı:%50")
                print("Otopark ücreti:{0}TL".format(round(ucret*ENGELLI_INDIRIM,2) ))
            else:
                print("Otopark ücreti:{0}TL".format(round(ucret, 2))) #kod 1 veya iki olup özel durumun yok olması durumu için
        else:
            print("Otopark ücreti:{0}TL".format(round(ucret,2)))
        devam=input("Başka araç var mı?(E/e/H/h)")
        while not(devam=="E" or devam=="e" or devam=="H" or devam=="h"):
            devam = input("Başka araç var mı?(E/e/H/h)")
    print("{:<10}  {:<15}  {:<10} ".format('\nAraç sınıfı','Araç Sayısı','Oranı %'))
    print(f'{"Motosiklet":<15}  {motosiklet:<11}  {motosiklet/top_arac*100:<10.2f} ')
    print(f'{"Binek":<15}  {binek:<11}  {binek / top_arac * 100:<10.2f} ')
    print(f'{"Minibüs":<15}  {minibus:<11}  {minibus/top_arac*100:<10.2f} ')
    print(f'{"Otobüs":<15}  {otobus:<11}  {otobus/top_arac*100:<10.2f} ')
    print(f'{"Kamyon":<15}  {kamyon:<11}  {kamyon/top_arac*100:<10.2f} ')
    print(f'{"Tır":<15}  {tir:<11}  {tir / top_arac * 100:<10.2f} ')

    print("Otoparkın toplam geliri:",top_gelir)
    print("{:<10}  {:<15}  {:<10} ".format('Araç sınıfı', 'Toplam gelir', 'Oranı %'))
    print(f'{"Motosiklet":<15}  {round(motosiklet_gelir,2):<11}  {motosiklet_gelir / top_gelir * 100:<10.2f} ')
    print(f'{"Binek":<15}  {round(binek_gelir,2):<11}  {binek_gelir / top_gelir * 100:<10.2f} ')
    print(f'{"Minibüs":<15}  {round(minibus_gelir,2):<11}  {minibus_gelir / top_gelir * 100:<10.2f} ')
    print(f'{"Otobüs":<15}  {round(otobus_gelir,2):<11}  {otobus_gelir / top_gelir * 100:<10.2f} ')
    print(f'{"Kamyon":<15}  {round(kamyon_gelir,2):<11}  {kamyon_gelir / top_gelir* 100:<10.2f} ')
    print(f'{"Tır":<15}  {round(tir_gelir,2):<11}  {tir_gelir / top_gelir * 100:<10.2f} ')

    print("{:<15}  {:<20}  {:<10} ".format('Araç sınıfı', 'Ortalama süre', 'Ortalama gelir'))
    print(f'{"Motosiklet":<15}  {ort_gun_saat_dk_hesapla(motosiklet_sure,motosiklet):<11}    {round(motosiklet_gelir / motosiklet,2 ):>10}TL')
    print(f'{"Binek":<15}  {ort_gun_saat_dk_hesapla(binek_sure,binek):<11}    {round(binek_gelir / binek,2 ):>10}TL ')
    print(f'{"Minibüs":<15}  {ort_gun_saat_dk_hesapla(minibus_sure,minibus):<11}    {round(minibus_gelir / minibus,2 ):>10}TL ')
    print(f'{"Otobüs":<15}  {ort_gun_saat_dk_hesapla(otobus_sure,otobus):<11}    {round(otobus_gelir / otobus,2 ):>10}TL ')
    print(f'{"Kamyon":<15}  {ort_gun_saat_dk_hesapla(kamyon_sure,kamyon):<11}    {round(kamyon_gelir / kamyon ,2):>10}TL ')
    print(f'{"Tır":<15}  {ort_gun_saat_dk_hesapla(tir_sure,tir):<11}    {round(tir_gelir / tir * 100,2):>10}TL ')


    print("Ağırlığı 1 tondan az binek araçların tüm binek araçlar içindeki oranı: %{0:.2f}".format(bir_tondan_az_binek/binek*100))
    print("Ağırlığı 10 tondan fazla otobüs, kamyon ve tırların tüm otobüs kamyon ve tırlar içindeki oranı: %{0:.2f}".format(on_tondan_fazla_okt/(kamyon+otobus+tir)*100))
    print("Otoparkta 30 dakika veya daha kısa süre kalan motosiklet ve binek tipi araçların, tüm motosiklet ve binek tipi araçlar içindeki oranı: %{0:.2f}".format(otuz_dkden_az_mb/(motosiklet+binek)*100))
    print("Otoparkta 1 günden daha uzun süre kalan minibüs ve otobüs tipi araçların, tüm minibüs ve otobüs tipi araçlar içindeki oran: %{0:.2f}".format(bir_gunden_fazla_mo/(minibus+otobus)*100))
    print("Otoparkta 30 günden daha uzun süre kalan veya 1000 TL’den daha yüksek gelir edilen araçların, tüm araçlar içindeki oranı: %{0:.2f}".format(otuz_gun_veya_bin_liradan_fazla/top_arac*100))
    print("Sürücüsü gazi veya engelli olan araçların sayıları: {0}, tüm araçlar içindeki oranları: %{1:.2f} ve araç başına ortalama otoparkta kalma süreleri (gün, saat, dakika):{2}".format(gazi_engelli_arac,gazi_engelli_arac/top_arac*100,ort_gun_saat_dk_hesapla(gazi_engelli_sure,gazi_engelli_arac)))
    print("Otoparkta 3 saatten daha uzun süre kalan indirim uygulanan araçların, tüm indirim uygulanan araçlar içindeki oranı: %{0:.2f}".format(uc_saaten_uzunkalan_indirimli/gazi_engelli_arac*100))
    print("En uzun süre otoparkta kalan aracın otoparkta kaldığı süre(gün, saat, dakika): ",ort_gun_saat_dk_hesapla(max_sure,1)," ve elde edilen gelir: {0}TL".format(max_surenin_geliri))
    print("En çok gelir elde edilen binek aracın otoparkta kaldığı süre(gün, saat, dakika):",ort_gun_saat_dk_hesapla(max_gelirin_suresi,1)," ve elde edilen gelir: {0}TL".format(max_gelir))
def ort_gun_saat_dk_hesapla(sure,arac_say):# 3. maddenin ilk kısmındaki kod tekrarından doğacak hataları azaltmak ve okunabilirliği artırmak için ortalama gün saat ve dakikayı veren fonksiyon yazdım
    sure/=arac_say
    gun = int(sure // 1440)
    saat = int((sure % 1440) // 60)
    dk = int(sure % 60)

    return f'{gun} gün,{saat} saat,{dk}dakika'

main()





