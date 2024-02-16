import pandas as pd
import random

class Generator:
    def __init__(self):
        self.df = pd.read_csv('data.csv')
        #self.myDate = self.df.iloc[:, 0]
        #self.myMsg = self.df.iloc[:, -1]
    def getNews(self):
        dateMsgDf = self.df.iloc[:, [0, -1]]
        result_dict = dateMsgDf.to_dict(orient='records')
        return result_dict
    def getSentiment(self, msg):
        sentiments = ['POS', 'NEG', 'NEU']
        return random.choice(sentiments)
    def getPrice(self):
        datePriceDf = self.df.iloc[:, [0, 4]]
        result_dict = datePriceDf.to_dict(orient='records')
        return result_dict