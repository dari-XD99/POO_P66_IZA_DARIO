import pandas as pd
titulos = pd.read_csv('titles.csv')
##print(titulos.head(10))
##print("\n"*2)
elenco = pd.read_csv('cast.csv', encoding='utf-8')
##print(elenco.head(10))
#print(len('titles.csv'))
#resultado = titulos[titulos['title'] == 'Romeo and Juliet'].sort_values('year').head(1)
#print(resultado)
#print(len(titulos[titulos['year'] == 1980]))
#print(len(titulos[titulos['year'] == 2020]))
#print(len(titulos[(titulos['year'] >= 1950) & (titulos['year'] <= 1959)]))
# Exacto: títulos que son exactamente "Star Wars"
#print(titulos[titulos['title'] == 'Star Wars'])

# Parcial: títulos que contienen "Star War", sin distinguir mayúsculas
#print(titulos[titulos['title'].str.contains('Star War', case=False, na=False)])
'''print(len(elenco[elenco['title'] == 'The Godfather']))
print(len(elenco[(elenco['title'] == 'The Godfather') & (elenco['n'].isna())]))
resultado = titulos[titulos['title'].str.contains('The Godfather', case=False, na=False)]
print(resultado[['title', 'year']])

anio = 2003  # o cualquier otro año
pelis = titulos[titulos['year'] == anio]
print(pelis[['title', 'year']])'''

titulo_mas_repetido = titulos['title'].value_counts().head(1)
print("Título más repetido:")
print(titulo_mas_repetido)

# Creamos una nueva columna de décadas
titulos['decada'] = (titulos['year'] // 10) * 10

# Contamos cuántas películas hay por década
decada_mas_peliculas = titulos['decada'].value_counts().sort_values(ascending=False).head(1)
print("\nDécada con más películas:")
print(decada_mas_peliculas)


# Contar cuántos personajes distintos hay por título
pelis_mas_personajes = elenco['title'].value_counts().head(5)
print("\nPelículas con más personajes:")
print(pelis_mas_personajes)


papeles_leo = elenco[elenco['name'] == 'Leonardo DiCaprio']
print("\nPapeles de Leonardo DiCaprio:")
print(papeles_leo[['title', 'character', 'year']].sort_values('year'))


pelis_the = titulos[titulos['title'].str.startswith('The')]
print("\nPelículas que comienzan con 'The':")
print(pelis_the[['title', 'year']].sort_values('year'))


# Filtrar solo actrices
actrices = elenco[elenco['type'] == 'actress']

# Contar los personajes más comunes
personajes_femeninos_comunes = actrices['character'].value_counts().head(10)
print("\nPersonajes femeninos más comunes:")
print(personajes_femeninos_comunes)


nombre = "Natalie Portman"  # Puedes cambiarlo por quien quieras
papeles = elenco[elenco['name'] == nombre]
print(f"\nPapeles de {nombre}:")
print(papeles[['title', 'character', 'year']].sort_values('year'))
