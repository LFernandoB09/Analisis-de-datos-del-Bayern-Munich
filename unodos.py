import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv('Bundesliga/Bundesliga Season 19-20.csv')  # Asegúrate de reemplazar 'ruta_al_archivo.csv' con la ruta real de tu archivo

# Filtrar por los partidos donde el FC Bayern fue el equipo local
bayern_home_games = df[df['HomeTeam'] == 'Bayern Munich']

# Contar cuántos de esos partidos resultaron en victorias, empates y derrotas para el FC Bayern
bayern_home_wins = bayern_home_games[bayern_home_games['FTR'] == 'H'].shape[0]
bayern_home_draws = bayern_home_games[bayern_home_games['FTR'] == 'D'].shape[0]
bayern_home_losses = bayern_home_games[bayern_home_games['FTR'] == 'A'].shape[0]

# Imprimir los resultados
print(f"El FC Bayern tuvo {bayern_home_wins} victorias, {bayern_home_draws} empates y {bayern_home_losses} derrotas como local en la temporada 2019-2020.")

# Generar el gráfico de barras
results = ['Victorias', 'Empates', 'Derrotas']
counts = [bayern_home_wins, bayern_home_draws, bayern_home_losses]

plt.figure(figsize=(10, 6))
plt.bar(results, counts, color=['green', 'blue', 'red'])
plt.xlabel('Resultados')
plt.ylabel('Cantidad de Partidos')
plt.title('Resultados del FC Bayern como Local en la Temporada 2019-2020')
plt.show()
