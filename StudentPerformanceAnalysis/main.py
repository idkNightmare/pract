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

print(f'Кількість студентів з початковим рівнем - {df[df["Середній бал"] <= 3].shape[0]}')
print(f'Кількість студентів з середнім балом ниже семи - {df[df["Середній бал"] < 7].shape[0]}')

df['status']=np.where(df['Середній бал']>7,'Добре','Потребує уваги')
print(df)

plt.figure(figsize=(14, 10),layout='constrained')

plt.subplot(311)
plt.bar(df['№'],df['Середній бал'],color=np.where(df['status']=='Добре','blue','red'),label='Середні бали студентів з групи КІПЗс-25-3')
plt.xticks(df['№'],df['Студент'], rotation=90, ha='right')
plt.yticks(range(1,13))
plt.xlabel('ПІБ Студентів', fontsize=12)
plt.ylabel('Бали (1-12)', fontsize=12)
plt.legend(loc='upper right')
plt.show()

plt.subplot(311)
plt.plot()