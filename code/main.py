import mandant
import verkaufsprodukt

files_dict = {}
# work directory in linux:
files_dict['work_dir'] = '/home/karol/PycharmProjects/Produktdatenbank/daten/'

if __name__ == "__main__":

    mandantID = 4
    vpdID = 1

    omandant = mandant.Mandant(files_dict)
    omandant.pruefeMantant(mandantID)

    overkaufsprodukt = verkaufsprodukt.Verkaufsprodukt(files_dict)
    myDict = overkaufsprodukt.leseVerkaufsprodukt(vpdID, mandantID)
    print(myDict)
