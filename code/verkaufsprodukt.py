import pandas as pd
from pathlib import Path


class Verkaufsprodukt():
    def __init__(self, f_dict):
        self.f_dict = f_dict

        work_dir = self.f_dict.get('work_dir')
        self.tabelle = work_dir + 'verkaufsprodukt.csv'
        datei = Path(self.tabelle)
        if datei.is_file():
            text = 'Verkaufsprodukt/init: Die Datei ' + self.tabelle + ' existiert. Also alles okay. Es geht weiter'
            print(text)
        else:
            text = 'Verkaufsprodukt/init: Die Datei ' + self.tabelle + ' existiert nicht! Ups! Baustelle!'
            print(text)

        self.tabelle_struktur = {'vpdID': int, 'mandantIR': int, 'name': str, 'von': int, 'bis': int, 'pdID': int}


    def leseVerkaufsprodukt(self, vpdID: int, mandantID: int):
        datei = self.tabelle
        struktur = self.tabelle_struktur

        df = pd.read_csv(filepath_or_buffer=datei, sep=";", dtype=struktur)
        df1 = df[((df.vpdID == vpdID) & (df.mandantID == mandantID))]

        myDict = {}  # hier werden die Ergebnisse abgelegt

        if df1.__len__() == 0:
            text = f'Verkaufsprodukt/leseVerkaufsprodukt: keine Daten vorhanden. vpdID={vpdID} und mandantID={mandantID}'
            print(text)
        elif df1.__len__() > 1:
            text = f'Verkaufsprodukt/leseVerkaufsprodukt: zu viele Daten. Da passt etwas nicht. vpdID={vpdID} und mandantID={mandantID}'
            print(text)
        else:
            for key, wert in df1.items():

                myDict[key] = wert.iloc[0]


        return myDict
