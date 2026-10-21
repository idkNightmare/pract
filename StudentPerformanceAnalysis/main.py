import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file='КІПЗс-25-3_оцінки_готові.csv'
df=pd.read_csv(file)

print(df.head(5).to_string(index=False))

shape=df.shape
columns=df.columns
print(f'Кількість рядків - {shape[0]} \nКількість стовпців - {shape[1]}')

df['Середній бал'] = df.iloc[:, 2:].mean(axis=1, skipna=True).round(2)
print('-'*30)
print(df[['Студент', 'Середній бал']].to_string(index=False))

print('-'*30)
mean_grade_all=df['Середній бал'].sum()/shape[0]
print(f'Середній бал всієї групи - {mean_grade_all}')

max_grate=df.iloc[:,2:].max().max()
min_grate=df.iloc[:,2:].min().min()
print('-'*30)
print(f'Максимальна оцінка в журналі - {max_grate} \nМінімальна оцінка в журналі - {min_grate}')
