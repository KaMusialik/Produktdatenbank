import pandas as pd
from pathlib import Path


class Mandant():
    def __init__(self, f_dict):
        self.f_dict = f_dict

        work_dir = self.f_dict.get('work_dir')
        self.tabelle = work_dir + 'mandant.csv'
        datei = Path(self.tabelle)
        if datei.is_file():
            text = 'Mandant/init: Die Datei ' + self.tabelle+ ' existiert. Also alles okay. Es geht weiter'
            print(text)
        else:
            text = 'Mandant/init: Die Datei ' + self.tabelle + ' existiert nicht! Ups! Baustelle!'
            print(text)

        self.tabelle_struktur = {'mandantIR':int, 'beschreibung':str}

    def pruefeMantant(self, mandantID):
        datei = self.tabelle
        struktur = self.tabelle_struktur

        df = pd.read_csv(filepath_or_buffer=datei, sep=";", dtype=struktur)
        df1 = df[df.mandantID == mandantID]

        if df1.__len__() == 0:
            text = f'Mandant/pruefeMantant: keine Daten vorhanden. mandantID={mandantID}'
            print(text)
        elif df1.__len__() > 1:
            text = f'Mandant/pruefeMantant: zu viele Daten. Da passt etwas nicht. mandantID={mandantID}'
            print(text)
        else:
            beschreibung = df1.iloc[0].beschreibung
            text = f'Mandant/pruefeMantant: wunderbar! Zu mandantID={mandantID} gehört Beschreibung={beschreibung}'
            print(text)
