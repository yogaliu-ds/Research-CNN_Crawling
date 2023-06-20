import pandas as pd

data = pd.read_csv(r"C:\Users\denne\python_projects\cnn_news\google.csv")
print(data.iloc[:,:2])

print(data.shape)

print(data['content'][0])
