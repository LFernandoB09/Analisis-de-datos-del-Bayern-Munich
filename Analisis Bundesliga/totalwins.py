import pandas as pd
import matplotlib.pyplot as plt

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

bayern_homewins1213 = bayern_homegames1213[bayern_homegames1213['FTR'] == 'H'].shape[0]
bayern_homewins1314 = bayern_homegames1314[bayern_homegames1314['FTR'] == 'H'].shape[0]
bayern_homewins1415 = bayern_homegames1415[bayern_homegames1415['FTR'] == 'H'].shape[0]
bayern_homewins1516 = bayern_homegames1516[bayern_homegames1516['FTR'] == 'H'].shape[0]
bayern_homewins1617 = bayern_homegames1617[bayern_homegames1617['FTR'] == 'H'].shape[0]
bayern_homewins1718 = bayern_homegames1718[bayern_homegames1718['FTR'] == 'H'].shape[0]
bayern_homewins1819 = bayern_homegames1819[bayern_homegames1819['FTR'] == 'H'].shape[0]
bayern_homewins1920 = bayern_homegames1920[bayern_homegames1920['FTR'] == 'H'].shape[0]
bayern_homewins2021 = bayern_homegames2021[bayern_homegames2021['FTR'] == 'H'].shape[0]
bayern_homewins2122 = bayern_homegames2122[bayern_homegames2122['FTR'] == 'H'].shape[0]
bayern_homewins2223 = bayern_homegames2223[bayern_homegames2223['FTR'] == 'H'].shape[0]
bayern_homewins2324 = bayern_homegames2324[bayern_homegames2324['FTR'] == 'H'].shape[0]

bayern_awaywins1213 = bayern_awaygames1213[bayern_awaygames1213['FTR'] == 'A'].shape[0]
bayern_awaywins1314 = bayern_awaygames1314[bayern_awaygames1314['FTR'] == 'A'].shape[0]
bayern_awaywins1415 = bayern_awaygames1415[bayern_awaygames1415['FTR'] == 'A'].shape[0]
bayern_awaywins1516 = bayern_awaygames1516[bayern_awaygames1516['FTR'] == 'A'].shape[0]
bayern_awaywins1617 = bayern_awaygames1617[bayern_awaygames1617['FTR'] == 'A'].shape[0]
bayern_awaywins1718 = bayern_awaygames1718[bayern_awaygames1718['FTR'] == 'A'].shape[0]
bayern_awaywins1819 = bayern_awaygames1819[bayern_awaygames1819['FTR'] == 'A'].shape[0]
bayern_awaywins1920 = bayern_awaygames1920[bayern_awaygames1920['FTR'] == 'A'].shape[0]
bayern_awaywins2021 = bayern_awaygames2021[bayern_awaygames2021['FTR'] == 'A'].shape[0]
bayern_awaywins2122 = bayern_awaygames2122[bayern_awaygames2122['FTR'] == 'A'].shape[0]
bayern_awaywins2223 = bayern_awaygames2223[bayern_awaygames2223['FTR'] == 'A'].shape[0]
bayern_awaywins2324 = bayern_awaygames2324[bayern_awaygames2324['FTR'] == 'A'].shape[0]

bayern_totalwins1213 = bayern_homewins1213 + bayern_awaywins1213
bayern_totalwins1314 = bayern_homewins1314 + bayern_awaywins1314
bayern_totalwins1415 = bayern_homewins1415 + bayern_awaywins1415
bayern_totalwins1516 = bayern_homewins1516 + bayern_awaywins1516
bayern_totalwins1617 = bayern_homewins1617 + bayern_awaywins1617
bayern_totalwins1718 = bayern_homewins1718 + bayern_awaywins1718
bayern_totalwins1819 = bayern_homewins1819 + bayern_awaywins1819
bayern_totalwins1920 = bayern_homewins1920 + bayern_awaywins1920
bayern_totalwins2021 = bayern_homewins2021 + bayern_awaywins2021
bayern_totalwins2122 = bayern_homewins2122 + bayern_awaywins2122
bayern_totalwins2223 = bayern_homewins2223 + bayern_awaywins2223
bayern_totalwins2324 = bayern_homewins2324 + bayern_awaywins2324

print(f"El Bayern Munich gano {bayern_totalwins1213} veces en la temporada 2012-2013")
print(f"El Bayern Munich gano {bayern_totalwins1314} veces en la temporada 2013-2014")
print(f"El Bayern Munich gano {bayern_totalwins1415} veces en la temporada 2014-2015")
print(f"El Bayern Munich gano {bayern_totalwins1516} veces en la temporada 2015-2016")
print(f"El Bayern Munich gano {bayern_totalwins1617} veces en la temporada 2016-2017")
print(f"El Bayern Munich gano {bayern_totalwins1718} veces en la temporada 2017-2018")
print(f"El Bayern Munich gano {bayern_totalwins1819} veces en la temporada 2018-2019")
print(f"El Bayern Munich gano {bayern_totalwins1920} veces en la temporada 2019-2020")
print(f"El Bayern Munich gano {bayern_totalwins2021} veces en la temporada 2020-2021")
print(f"El Bayern Munich gano {bayern_totalwins2122} veces en la temporada 2021-2022")
print(f"El Bayern Munich gano {bayern_totalwins2223} veces en la temporada 2022-2023")
print(f"El Bayern Munich gano {bayern_totalwins2324} veces en la temporada 2023-2024")


seasons = ["12-13", "13-14", "14-15","15-16","16-17","17-18","18-19","19-20","20-21","21-22","22-23","23-24"]
count = [bayern_totalwins1213,
         bayern_totalwins1314,
         bayern_totalwins1415,
         bayern_totalwins1516,
         bayern_totalwins1617,
         bayern_totalwins1718,
         bayern_totalwins1819,
         bayern_totalwins1920,
         bayern_totalwins2021,
         bayern_totalwins2122,
         bayern_totalwins2223,
         bayern_totalwins2324]

plt.figure(figsize=(10,6))
plt.bar(seasons, count)
plt.xlabel("Temporada")
plt.ylabel("Cantidad De Victorias")
plt.yticks(range(int(max(count)) + 1))
plt.title("Cantidad De Victorias Como Local Del Bayern Munich")
plt.show()