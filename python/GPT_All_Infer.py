import torch
from transformers import GPT2Tokenizer, GPT2ForSequenceClassification
import pandas as pd
import numpy as np
import torch.nn as nn

# 定义简单的神经网络模型（与之前保存模型相同）
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(2, 64)  # 输入特征：今日价格和情绪得分
        self.fc2 = nn.Linear(64, 1)  # 输出：预测的明天价格

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# 加载GPT-2模型进行情绪分析
tokenizer = GPT2Tokenizer.from_pretrained('gpt2-xl')
tokenizer.pad_token = tokenizer.eos_token  # GPT-2需要pad token
model_path = './gpt_model.pth'  # 更新为您的模型路径
gpt_model = GPT2ForSequenceClassification.from_pretrained('gpt2-xl', num_labels=4)
gpt_model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
gpt_model.eval()

# 加载神经网络模型进行价格预测
nn_model = SimpleNN()
nn_model_path = './nn_model.pth'  # 更新为您的模型路径
nn_model.load_state_dict(torch.load(nn_model_path, map_location=torch.device('cpu')))
nn_model.eval()

# 读入数据
df = pd.read_csv('FinalModel_withoutGPT2/Bitcoin_with_Sentiment.csv')  # 更新为您的数据路径
sample_comment = df.iloc[0]['Comments']
sample_price = df.iloc[0]['Close']

# 使用GPT-2模型进行情绪推断
encoded_input = tokenizer(sample_comment, return_tensors='pt', padding=True, truncation=True, max_length=60)
with torch.no_grad():
    output = gpt_model(**encoded_input)
sentiment_score = torch.argmax(output.logits, dim=1).item()  # 获取情绪得分的索引

# 根据情绪得分索引映射到您指定的值：-1, 0, 1
if sentiment_score == 3:
    sentiment = 1  # Positive
elif sentiment_score == 2:
    sentiment = -1  # Negative
else:
    sentiment = 0  # Neutral/Irrelevant

# 准备输入神经网络模型的特征
nn_input = torch.FloatTensor([[sample_price, sentiment]])

# 使用神经网络模型预测明天的价格
with torch.no_grad():
    predicted_price = nn_model(nn_input).item()

print("Predicted price for tomorrow:", predicted_price)
