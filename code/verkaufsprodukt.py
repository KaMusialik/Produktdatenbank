#import pandas as pd
from pathlib import Path


class Verkaufsprodukt():
    def __init__(self, f_dict):
        self.f_dict = f_dict

        work_dir = self.f_dict.get('work_dir')
        self.tabelle = work_dir + 'verkaufsprodukt.csv'
        datei = Path(self.tabelle)
        if datei.is_file():
            text = 'Verkaufsprodukt/init: Die Datei ' + self.tabelle+ ' existiert. Also alles okay. Es geht weiter'
            print(text)
        else:
            text = 'Verkaufsprodukt/init: Die Datei ' + self.tabelle + ' existiert nicht! Ups! Baustelle!'
            print(text)

        self.tabelle_struktur = {'vpdID':int, 'mandantIR':int, 'name':str, 'von':int, 'bis':int, 'pdID':int}