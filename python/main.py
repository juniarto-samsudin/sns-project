from dotenv import load_dotenv
import os, time
from package.influxWriter.writer import Writer
from package.sentimentDataGenerator.generator import Generator
load_dotenv()

token = os.getenv("token")
org = os.getenv("org")
url = os.getenv("url")
bucket = os.getenv("bucket")

myWriter = Writer(url, token, org, bucket)
#myWriter.write("home", "room", "kitchen", "temp", 250)
#myWriter.writeWithTime("home", "room", "kitchen", "temp", 2511, "2021-10-10")
myGenerator = Generator()

def populateComments():
    myMessageArray = myGenerator.getNews()
    for message in myMessageArray:
        mySentiment = myGenerator.getSentiment(message['Comments'])
        myWriter.write("Bitcoin", "Source", "Twitter", "Comments", message['Comments'], "Sentiment", mySentiment)
        time.sleep(10)

def populatePrice():
    myPriceArray = myGenerator.getPrice()
    for price in myPriceArray:
        myWriter.write("Bitcoin", "Source", "Yahoo", "Price", price['Close'])
        print(price['Close'])
        time.sleep(10)

def dropMeasurement():
    myWriter.dropMeasurement("Bitcoin")

#populateComments()
#populatePrice()
dropMeasurement()

""" myMessageArray = myGenerator.getNews()
print(myMessageArray[0])

for message in myMessageArray:
    mySentiment = myGenerator.getSentiment(message['Comments'])
    myWriter.write("Bitcoin", "Source", "Twitter", "Comments", message['Comments'], "Sentiment", mySentiment)
    time.sleep(10)

mySentiment = myGenerator.getSentiment(myMessageArray[0]['Comments'])
print(mySentiment) """