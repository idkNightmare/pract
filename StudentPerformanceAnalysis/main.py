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

plt.bar(df['№'],df['Середній бал'],color=np.where(df['status']=='Добре','blue','red'),label='Середні бали студентів з групи КІПЗс-25-3')
plt.xticks(df['№'],df['Студент'], rotation=90, ha='right')
plt.yticks(range(1,13))
plt.xlabel('ПІБ Студентів', fontsize=12)
plt.ylabel('Бали (1-12)', fontsize=12)
plt.legend(loc='upper right')
plt.savefig('student_averages.png')

grade_columns = df.columns[2:-2] 
group_means_by_date = df[grade_columns].mean(axis=0)
all_grades = df[grade_columns].values.flatten()

plt.figure(figsize=(10, 5))
plt.plot(grade_columns, group_means_by_date, marker='o', color='green', linewidth=2, label='Середній бал групи')
plt.title('Динаміка успішності групи за датами занять', fontsize=14)
plt.xlabel('Дата заняття', fontsize=12)
plt.ylabel('Середній бал', fontsize=12)
plt.grid(True, linestyle=':')
plt.legend()
plt.savefig('group_dynamics.png') 
plt.show()


plt.figure(figsize=(10, 5))
plt.hist(all_grades, bins=range(1, 14), rwidth=0.8, color='orange', edgecolor='black', align='left')
plt.title('Розподіл усіх виставлених оцінок у журналі', fontsize=14)
plt.xlabel('Бали (1-12)', fontsize=12)
plt.ylabel('Скільки разів зустрічається оцінка', fontsize=12)
plt.xticks(range(1, 13))
plt.savefig('grades_distribution.png') 
plt.show()

def sort_students(data):
    return data.sort_values(by='Середній бал', ascending=False)

def find_student(data, name):
    result = data[data['Студент'].str.strip().str.lower() == name.strip().lower()]
    if not result.empty:
        row = result.iloc[0]
        print(f"\nЗнайдено: {row['Студент']}\n -> Бал: {row['Середній бал']}\n -> Оцінок: {row[grade_columns].notna().sum()}\n -> Статус: {row['status']}")
    else:
        print(f"\nСтудента '{name}' не знайдено.")
        
df_sorted = sort_students(df)
find_student(df, df['Студент'].iloc[0])
    
df['Оцінок 1–3'] = df[grade_columns].apply(lambda row: sum((row >= 1) & (row <= 3)), axis=1)

df_results = df[['Студент', 'Середній бал', 'Оцінок 1–3', 'status']].copy()
df_results.columns = ['Студент', 'Середній бал', 'Оцінок 1–3', 'Статус']

df_results.to_csv('results.csv', index=False, encoding='utf-8-sig')