import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def sort_students_manually(df):
    """
    Реалізація власного алгоритму Insertion Sort (Сортування включенням).
    Сортує студентів за зростанням їхнього середнього балу.
    """
    print('-' * 40)
    print("КРОК 5: РУЧНЕ СОРТУВАННЯ СТУДЕНТІВ (INSERTION SORT)")
    
    # 1. Отримуємо список кортежів (ПІБ, Середній бал)
    student_list = list(zip(df['Студент'].values, df['Середній бал'].values))
    
    # 2. Реалізація алгоритму Insertion Sort вручну
    for i in range(1, len(student_list)):
        key = student_list[i]  # Поточний елемент (Ім'я, Бал)
        j = i - 1
        
        # Порівнюємо елементи за середнім балом (key[1])
        while j >= 0 and student_list[j][1] > key[1]:
            student_list[j + 1] = student_list[j]
            j -= 1
        student_list[j + 1] = key
          
def linear_search_student(df, grade_columns, search_name):
    """
    Додаткове завдання: Лінійний пошук студента за ПІБ.
    Виводить середній бал, кількість оцінок та статус успішності.
    """
    print('-' * 40)
    print(f"ДОДАТКОВЕ ЗАВДАННЯ: ЛІНІЙНИЙ ПОШУК СТУДЕНТА")
    
    search_name_clean = search_name.strip().lower()
    
    # Проходимо циклом по рядках DataFrame (Лінійний пошук)
    for idx, row in df.iterrows():
        if row['Студент'].strip().lower() == search_name_clean:
            # Рахуємо кількість оцінок (ігноруючи NaN пропуски)
            total_grades = row[grade_columns].notna().sum()
            
            print(f"Знайдено студента: {row['Студент']}")
            print(f" -> Середній бал: {row['Середній бал']}")
            print(f" -> Кількість виставлених оцінок: {total_grades}")
            print(f" -> Статус успішності: {row['status']}")
            return
            
    print(f"Студента з ПІБ '{search_name}' не знайдено в журналі.")

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

sort_students_manually(df)

# 2. Запуск лінійного пошуку (автоматично перевіряємо першого студента з файлу для тесту)
if not df.empty:
    first_student_name = df['Студент'].iloc[0]
    linear_search_student(df, grade_columns, first_student_name)
    
df['Оцінок 1–3'] = df[grade_columns].apply(lambda row: sum((row >= 1) & (row <= 3)), axis=1)

# 4. Формування нової підсумкової таблиці (Крок 6)
df_results = df[['Студент', 'Середній бал', 'Оцінок 1–3', 'status']].copy()
df_results.columns = ['Студент', 'Середній бал', 'Оцінок 1–3', 'Статус']

# 5. Автоматичне збереження результатів у новий файл results.csv
df_results.to_csv('results.csv', index=False, encoding='utf-8-sig')

print('-' * 40)
print("КРОК 6 ВИКОНАНО: Новий файл 'results.csv' успішно збережено автоматично!")