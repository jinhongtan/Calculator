import pandas as pd
from Calculator import *

#AddictionPath = 'C:\Users\Bruce Tan\PycharmProjects\Calculator\venv\UnitTestAddition.csv'
basePath = "/code/src/"
AdditionPath = basePath + "data/UnitTestAddition.csv"
SubtractionPath = basePath +  "data/UnitTestSubtraction.csv"
MultiplicationPath = basePath + "data/UnitTestMultiplication.csv"
SquareRootPath = basePath + "data/UnitTestSquareRoot.csv"
SquarePath = basePath + "data/UnitTestSquare.csv"
DivisionPath = basePath + "data/UnitTestDivision.csv"


def read_data(TestDataPath):
    data= pd.read_csv(TestDataPath)
    df = pd.DataFrame(data, columns=['Value 1','Value 2','Result'])
    return df


def read_square(TestDataPath):
    data= pd.read_csv(TestDataPath)
    df = pd.DataFrame(data, columns=['Value 1','Result'])
    return df
