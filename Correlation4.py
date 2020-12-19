import plotly.express as px
import csv 
import numpy as np

def getdatasource(data):
    sizeoftv = []
    timespentwatchingtv = []
    with open(data) as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
            sizeoftv.append(float(row['Size of TV']))
            timespentwatchingtv.append(float(row[' Average time spent watching TV in a week']))
    return{'x':sizeoftv , 'y': timespentwatchingtv}
def findcorrelation(datasource):
    correlation = np.corrcoef(datasource['x'],datasource['y'])
    print('correlation between Size of tv vs % time spent watching tv in 1 week : ',correlation[0,1])
def setup():
    data = './Size of TV,% time spent watching TV in a week.csv'
    datasource = getdatasource(data)
    findcorrelation(datasource)
setup()