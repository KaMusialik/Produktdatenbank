from fastapi import FastAPI

import mandant
#import verkaufsprodukt

files_dict = {}
# work directory in linux:
files_dict['work_dir'] = '/home/karol/PycharmProjects/Produktdatenbank/daten/'

app = FastAPI()

@app.get("/mandant/{mandantID}")
async def get_mandant(mandantID: int):
    omandant = mandant.Mandant(files_dict)
    text = omandant.pruefeMandant(mandantID)

    return {text}@app.get("/mandant/{mandantID}")
