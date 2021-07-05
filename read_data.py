import pandas as pd
from Calculator import *

#AddictionPath = 'C:\Users\Bruce Tan\PycharmProjects\Calculator\venv\UnitTestAddition.csv'

AdditionPath ="C:/Users/Bruce Tan/Downloads/Unit Test Addition.csv"
SubtractionPath ="C:/Users/Bruce Tan/Downloads/Unit Test Subtraction.csv"
MultiplicationPath ="C:/Users/Bruce Tan/Downloads/Unit Test Multiplication.csv"
SquareRootPath ="C:/Users/Bruce Tan/Downloads/Unit Test Square Root.csv"
SquarePath ="C:/Users/Bruce Tan/Downloads/Unit Test Square.csv"
DivisionPath ="C:/Users/Bruce Tan/Downloads/Unit Test Division.csv"


def read_data(TestDataPath):
    data= pd.read_csv(TestDataPath)
    df = pd.DataFrame(data, columns=['Value 1','Value 2','Result'])
    return df


def read_square(TestDataPath):
    data= pd.read_csv(TestDataPath)
    df = pd.DataFrame(data, columns=['Value 1','Result'])
    return df