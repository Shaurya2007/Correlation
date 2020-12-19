import plotly.express as px
import csv 
import numpy as np

def getdatasource(data):
    studentmarks = []
    dayspresent = []
    with open(data) as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
            studentmarks.append(float(row['Marks In Percentage']))
            dayspresent.append(float(row['Days Present']))
    return{'x':studentmarks , 'y': dayspresent}
def findcorrelation(datasource):
    correlation = np.corrcoef(datasource['x'],datasource['y'])
    print('correlation between Student marks vs Days present : ',correlation[0,1])
def setup():
    data = './Student Marks vs Days Present.csv'
    datasource = getdatasource(data)
    findcorrelation(datasource)
setup()