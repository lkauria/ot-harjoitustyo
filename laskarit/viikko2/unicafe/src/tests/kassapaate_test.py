import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luotu_kassa_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_konstruktori_asettaa_kassaan_syotetyt_maukkaat_lounaat_nollaksi(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_konstruktori_asettaa_kassaan_syotetyt_edulliset_lounaat_nollaksi(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_edullisesti_maksu_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(250)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_syo_maukkaasti_maksu_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_syo_maukkaasti_ja_maukkaiden_maara_lisaantyy(self):
        self.kassapaate.syo_maukkaasti_kateisella(1000)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_edullisesti_ja_edullisten_maara_lisaantyy(self):
        self.kassapaate.syo_edullisesti_kateisella(1000)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateista_liian_vahan_maukkaaseen_saldo_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateista_liian_vahan_maukkaaseen_myytyjen_maara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateista_liian_vahan_edulliseen_saldo_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateista_liian_vahan_edulliseen_myytyjen_maara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(self.kassapaate.edulliset, 0)


    def test_ostetaan_kortilla_edullinen(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        if maksukortti.saldo >= 240:
            maksukortti.ota_rahaa(240)
            return True
    
    def test_ostetaan_kortilla_maukas(self):
        maksukortti = Maksukortti(400)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        if maksukortti.saldo >= 400:
            maksukortti.ota_rahaa(400)
            return True


    def test_ostetaan_kortilla_edullinen(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        if maksukortti.saldo >= 240:
            self.assertEqual(self.kassapaate.edulliset, 1)

    def test_ostetaan_kortilla_maukas(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

        if maksukortti.saldo >= 240:
            self.assertEqual(self.kassapaate.maukkaat, 1)

    
    def test_kortin_saldo_ei_riita_edullinen(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 0)
        return False

    def test_kortin_saldo_ei_riita_edullinen_kortilta_ei_veloiteta(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        maksukortti.ota_rahaa(240)

        self.assertEqual(maksukortti.saldo, 100)
        return False
    
    def test_kortin_saldo_ei_riita_maukas_kortilta_ei_veloiteta(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        maksukortti.ota_rahaa(240)

        self.assertEqual(maksukortti.saldo, 100)
        return False
    
    def test_kassan_saldo_ei_muutu_korttiostossa(self):
        maksukortti = Maksukortti(10000)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataa_kortille_rahaa(self):
        kortti = Maksukortti(0)
        kortti.lataa_rahaa(10000)

        self.assertEqual(kortti.saldo, 10000)
    


