import pandas as pd
import matplotlib.pyplot as plt

#Leer el archivo CSV
df1 = pd.read_csv('Bundesliga/Bundesliga Season 12-13.csv')
df2 = pd.read_csv('Bundesliga/Bundesliga Season 13-14.csv')
df3 = pd.read_csv('Bundesliga/Bundesliga Season 14-15.csv')
df4 = pd.read_csv('Bundesliga/Bundesliga Season 15-16.csv')
df5 = pd.read_csv('Bundesliga/Bundesliga Season 16-17.csv')
df6 = pd.read_csv('Bundesliga/Bundesliga Season 17-18.csv')
df7 = pd.read_csv('Bundesliga/Bundesliga Season 18-19.csv')
df8 = pd.read_csv('Bundesliga/Bundesliga Season 19-20.csv')
df9 = pd.read_csv('Bundesliga/Bundesliga Season 20-21.csv')
df10 = pd.read_csv('Bundesliga/Bundesliga Season 21-22.csv')
df11 = pd.read_csv('Bundesliga/Bundesliga Season 22-23.csv')
df12 = pd.read_csv('Bundesliga/Bundesliga Season 23-24.csv')

#Filtrar el equipo
bayern_homegames1213 = df1[df1['HomeTeam'] == 'Bayern Munich']
bayern_homegames1314 = df2[df2['HomeTeam'] == 'Bayern Munich']
bayern_homegames1415 = df3[df3['HomeTeam'] == 'Bayern Munich']
bayern_homegames1516 = df4[df4['HomeTeam'] == 'Bayern Munich']
bayern_homegames1617 = df5[df5['HomeTeam'] == 'Bayern Munich']
bayern_homegames1718 = df6[df6['HomeTeam'] == 'Bayern Munich']
bayern_homegames1819 = df7[df7['HomeTeam'] == 'Bayern Munich']
bayern_homegames1920 = df8[df8['HomeTeam'] == 'Bayern Munich']
bayern_homegames2021 = df9[df9['HomeTeam'] == 'Bayern Munich']
bayern_homegames2122 = df10[df10['HomeTeam'] == 'Bayern Munich']
bayern_homegames2223 = df11[df11['HomeTeam'] == 'Bayern Munich']
bayern_homegames2324 = df12[df12['HomeTeam'] == 'Bayern Munich']

bayern_awaygames1213 = df1[df1['AwayTeam'] == 'Bayern Munich']
bayern_awaygames1314 = df2[df2['AwayTeam'] == 'Bayern Munich']
bayern_awaygames1415 = df3[df3['AwayTeam'] == 'Bayern Munich']
bayern_awaygames1516 = df4[df4['AwayTeam'] == 'Bayern Munich']
bayern_awaygames1617 = df5[df5['AwayTeam'] == 'Bayern Munich']
bayern_awaygames1718 = df6[df6['AwayTeam'] == 'Bayern Munich']
bayern_awaygames1819 = df7[df7['AwayTeam'] == 'Bayern Munich']
bayern_awaygames1920 = df8[df8['AwayTeam'] == 'Bayern Munich']
bayern_awaygames2021 = df9[df9['AwayTeam'] == 'Bayern Munich']
bayern_awaygames2122 = df10[df10['AwayTeam'] == 'Bayern Munich']
bayern_awaygames2223 = df11[df11['AwayTeam'] == 'Bayern Munich']
bayern_awaygames2324 = df12[df12['AwayTeam'] == 'Bayern Munich']

#Obtener la suma de goles 
bayern_totalgoals1213_home = bayern_homegames1213['FTHG'].sum()
bayern_totalgoals1314_home = bayern_homegames1314['FTHG'].sum()
bayern_totalgoals1415_home = bayern_homegames1415['FTHG'].sum()
bayern_totalgoals1516_home = bayern_homegames1516['FTHG'].sum()
bayern_totalgoals1617_home = bayern_homegames1617['FTHG'].sum()
bayern_totalgoals1718_home = bayern_homegames1718['FTHG'].sum()
bayern_totalgoals1819_home = bayern_homegames1819['FTHG'].sum()
bayern_totalgoals1920_home = bayern_homegames1920['FTHG'].sum()
bayern_totalgoals2021_home = bayern_homegames2021['FTHG'].sum()
bayern_totalgoals2122_home = bayern_homegames2122['FTHG'].sum()
bayern_totalgoals2223_home = bayern_homegames2223['FTHG'].sum()
bayern_totalgoals2324_home = bayern_homegames2324['FTHG'].sum()

bayern_totalgoals1213_away = bayern_awaygames1213['FTAG'].sum()
bayern_totalgoals1314_away = bayern_awaygames1314['FTAG'].sum()
bayern_totalgoals1415_away = bayern_awaygames1415['FTAG'].sum()
bayern_totalgoals1516_away = bayern_awaygames1516['FTAG'].sum()
bayern_totalgoals1617_away = bayern_awaygames1617['FTAG'].sum()
bayern_totalgoals1718_away = bayern_awaygames1718['FTAG'].sum()
bayern_totalgoals1819_away = bayern_awaygames1819['FTAG'].sum()
bayern_totalgoals1920_away = bayern_awaygames1920['FTAG'].sum()
bayern_totalgoals2021_away = bayern_awaygames2021['FTAG'].sum()
bayern_totalgoals2122_away = bayern_awaygames2122['FTAG'].sum()
bayern_totalgoals2223_away = bayern_awaygames2223['FTAG'].sum()
bayern_totalgoals2324_away = bayern_awaygames2324['FTAG'].sum()

#Suma de goles de local y visitante
bayern_totalgoals1213 = bayern_totalgoals1213_home + bayern_totalgoals1213_away
bayern_totalgoals1314 = bayern_totalgoals1314_home + bayern_totalgoals1314_away
bayern_totalgoals1415 = bayern_totalgoals1415_home + bayern_totalgoals1415_away
bayern_totalgoals1516 = bayern_totalgoals1516_home + bayern_totalgoals1516_away
bayern_totalgoals1617 = bayern_totalgoals1617_home + bayern_totalgoals1617_away
bayern_totalgoals1718 = bayern_totalgoals1718_home + bayern_totalgoals1718_away
bayern_totalgoals1819 = bayern_totalgoals1819_home + bayern_totalgoals1819_away
bayern_totalgoals1920 = bayern_totalgoals1920_home + bayern_totalgoals1920_away
bayern_totalgoals2021 = bayern_totalgoals2021_home + bayern_totalgoals2021_away
bayern_totalgoals2122 = bayern_totalgoals2122_home + bayern_totalgoals2122_away
bayern_totalgoals2223 = bayern_totalgoals2223_home + bayern_totalgoals2223_away
bayern_totalgoals2324 = bayern_totalgoals2324_home + bayern_totalgoals2324_away

#Imprimir el total de goles 
print(f"El Bayern Munich anotó {bayern_totalgoals1213} en la temporada 2012-2013")
print(f"El Bayern Munich anotó {bayern_totalgoals1314} en la temporada 2013-2014")
print(f"El Bayern Munich anotó {bayern_totalgoals1415} en la temporada 2014-2015")
print(f"El Bayern Munich anotó {bayern_totalgoals1516} en la temporada 2015-2016")
print(f"El Bayern Munich anotó {bayern_totalgoals1617} en la temporada 2016-2017")
print(f"El Bayern Munich anotó {bayern_totalgoals1718} en la temporada 2017-2018")
print(f"El Bayern Munich anotó {bayern_totalgoals1819} en la temporada 2018-2019")
print(f"El Bayern Munich anotó {bayern_totalgoals1920} en la temporada 2019-2020")
print(f"El Bayern Munich anotó {bayern_totalgoals2021} en la temporada 2020-2021")
print(f"El Bayern Munich anotó {bayern_totalgoals2122} en la temporada 2021-2022")
print(f"El Bayern Munich anotó {bayern_totalgoals2223} en la temporada 2022-2023")
print(f"El Bayern Munich anotó {bayern_totalgoals2324} en la temporada 2023-2024")

#Parte de los graficos

# Datos
seasons = ["12-13","13-14","14-15","15-16","16-17","17-18","18-19","19-20","20-21","21-22","22-23","23-24"]
count = [bayern_totalgoals1213,
         bayern_totalgoals1314,
         bayern_totalgoals1415,
         bayern_totalgoals1516,
         bayern_totalgoals1617,
         bayern_totalgoals1718,
         bayern_totalgoals1819,
         bayern_totalgoals1920,
         bayern_totalgoals2021,
         bayern_totalgoals2122,
         bayern_totalgoals2223,
         bayern_totalgoals2324]


# Crear el gráfico de barras
plt.figure(figsize=(10,6))
plt.bar(seasons, count)
plt.xlabel("Temporada")
plt.ylabel("Cantidad De Goles")
plt.title("Suma De Goles Por Temporada Del Bayern Munich")
plt.show()

