import plotly.express as px
import csv 
import numpy as np

def getdatasource(data):
    icecreamsales = []
    tempreature = []
    with open(data) as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
            tempreature.append(float(row['Temperature']))
            icecreamsales.append(float(row['Ice-cream Sales']))
    return{'x':icecreamsales , 'y': tempreature}
def findcorrelation(datasource):
    correlation = np.corrcoef(datasource['x'],datasource['y'])
    print('correlation between temprature vs icecream sales : ',correlation[0,1])
def setup():
    data = './Ice-Cream vs Cold-Drink vs Temperature - Ice Cream  vs Temperature.csv'
    datasource = getdatasource(data)
    findcorrelation(datasource)
setup()