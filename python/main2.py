from dotenv import load_dotenv
import os, time
from package.influxWriter.writer import Writer
from package.gptInference.inference import Inference
load_dotenv()

token = os.getenv("token")
org = os.getenv("org")
url = os.getenv("url")
bucket = os.getenv("bucket")

myInference = Inference()
myWriter = Writer(url, token, org, bucket)

def main():
    myMessageArray = myInference.getNews()
    print(myMessageArray)
    #[{'date':'2022-01-22','Comments': 'I love this product', 'Close': 100}, {'date':'2022-01-23','Comments': 'I hate this product', 'Close': 200}]
    for i in range(len(myMessageArray)):
        myMessage = myMessageArray[i]
        if i < len(myMessageArray) - 1:
            myMessageNext = myMessageArray[i+1]
        else:
            myMessageNext = myMessageArray[i]
        mySentimentAndPrice = myInference.getSentimentAndPrice(myMessage)
        print(mySentimentAndPrice)
        myWriter.writeWithTime("Bitcoin", "Source", "Current Close", "Price", myMessage['Close'], myMessage['Date'])
        myWriter.writeWithTimePlus1Day("Bitcoin-Prediction", "Source", "Predicted Close", "Predicted-Price", mySentimentAndPrice['predicted_price'], myMessage['Date'], myMessageNext['Date'])

if __name__ == "__main__":
    main()

"""  for myMessage in myMessageArray:
        mySentimentAndPrice = myInference.getSentimentAndPrice(myMessage)
        print(mySentimentAndPrice)
        myWriter.writeWithTime("Bitcoin", "Source", "Current Close", "Price", myMessage['Close'], myMessage['Date'])
        myWriter.writeWithTimePlus1Day("Bitcoin-Prediction", "Source", "Predicted Close", "Predicted-Price", mySentimentAndPrice['predicted_price'], myMessage['Date'])

if __name__ == "__main__":
    main() """