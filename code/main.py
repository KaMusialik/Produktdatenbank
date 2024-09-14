import verkaufsprodukt

files_dict = {}
# work directory in linux:
files_dict['work_dir'] = '/home/karol/PycharmProjects/Produktdatenbank/daten/'

if __name__ == "__main__":
    overkaufsprodukt = verkaufsprodukt.Verkaufsprodukt(files_dict)
