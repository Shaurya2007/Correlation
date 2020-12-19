import plotly.express as px
import csv 
import numpy as np

def getdatasource(data):
    coffee = []
    sleep = []
    with open(data) as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
            coffee.append(float(row['Coffee in ml']))
            sleep.append(float(row['sleep in hours']))
    return{'x':coffee , 'y': sleep}
def findcorrelation(datasource):
    correlation = np.corrcoef(datasource['x'],datasource['y'])
    print('correlation between coffee vs sleep : ',correlation[0,1])
def setup():
    data = './coffee vs sleep.csv'
    datasource = getdatasource(data)
    findcorrelation(datasource)
setup()