import pandas as pd


left, top = map(int, input().split())
right, bottom = map(int, input().split())
df = pd.read_csv('data.csv')
print(df.query('x >= @left and x <= @right and y >= @bottom and y <= @top'))
# print(df[(left <= df['x']) & (df['x'] <= right) & (bottom <= df['y']) & (df['y'] <= top)])