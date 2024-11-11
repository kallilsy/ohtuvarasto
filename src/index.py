from varasto import Varasto

def luo_varastot():
    """Luo varastot ja palauttaa ne."""
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    return mehua, olutta

def tulosta_varastot(mehua, olutta):
    """Tulostaa varastojen tiedot."""
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

def olut_tiedot(olutta):
    """Tulostaa olutvaraston tiedot."""
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

def mehu_lisaa_ota(mehua):
    """Lisää ja ottaa mehua varastosta."""
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

def virhetilanteet():
    """Testaa virhetilanteita."""
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

def olut_lisaa_ota(olutta):
    """Lisää ja ottaa olutta varastosta."""
    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")

def mehu_lisaa_ota_virhe(mehua):
    """Lisää ja ottaa mehua virheellisillä määrillä."""
    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")

def ota_varastosta(olutta, mehua):
    """Ota olutta ja mehua varastosta."""
    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")

    print(f"Mehuvarasto: {mehua}")
    print("mehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")

def main():
    """Pääohjelma."""
    mehua, olutta = luo_varastot()
    tulosta_varastot(mehua, olutta)
    olut_tiedot(olutta)
    mehu_lisaa_ota(mehua)
    virhetilanteet()
    olut_lisaa_ota(olutta)
    mehu_lisaa_ota_virhe(mehua)
    ota_varastosta(olutta, mehua)

if __name__ == "__main__":
    main()
