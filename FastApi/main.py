from fastapi import FastAPI
import pandas as pd
from typing import Optional
from typing import List, Tuple
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
app = FastAPI(title='API FILMS',description='Here, I´ll recomend you good movies', version='0.1')

#http://127.0.0.1:8000
'''''
Crear 6 funciones (recuerda que deben tener un decorador por cada una (@app.get(‘/’)):
'''
@app.get("/")
async def welcome():
    return "WELCOME!!! HERE YOU WILL FIND ALL MOVIES AND TV SHOW THAT YOU LOVE !!!"

@app.get("/index")
async def index():
    return "Function for searching: 1. get_max_duration, 2. get_score_count, 3. get_count_platform, 4. get_actor, 5.prod_per_county  y 6.get_contents(rating)"

#loading Data
path = 'datasets/total_Platforms.parquet'
platforms_df = pd.read_parquet(path)


'''''
Crear 6 funciones (recuerda que deben tener un decorador por cada una (@app.get(‘/’)):

1. Película (sólo película, no serie, etc) con mayor duración según año, plataforma y tipo de duración.
 La función debe llamarse get_max_duration(year, platform, duration_type) y debe devolver sólo el string del nombre de la película.
'''

@app.get("/get_max_duration/{year}/{platform}/{dtype}")
def get_max_duration(year:Optional[int] = None, platform:Optional[str] = None, duration_type:Optional[str] = None):
    # Creating a copy from original data in order to avoid any modification
    platforms_df_copy = platforms_df.copy()
    try:
        # Validando plataforma correcta
        platformList = ['amazon', 'disney', 'hulu', 'netflix']
        # filter applied by creating a for loop
        columns_att = dict(release_year=year,platform=platform,duration_type= duration_type)
        columns = list(columns_att.keys())
        attributes = list(columns_att.values())
                    
        if (platform == '' or platform not in platformList):
            return ValueError('PLATFORM NAME IS WRONG, YOU MUST WRITE amazon, disney, hulu OR netflix.')
        for i in range(len(columns_att)):
            if attributes[i] is not None:
                platforms_df_copy = platforms_df_copy[platforms_df_copy[columns[i]] == attributes[i]] 
            else:
                return ValueError(f'{attributes[i]} IS MISSING')
        # LOOKING FOR MOVIE'S MAX DURATION
        max_duration = platforms_df_copy.duration_int.max()
        max_duration_movie = platforms_df_copy.title[(platforms_df_copy.type == 'movie') & (platforms_df_copy.duration_int == max_duration)].iloc[0]
    
        # Creating a dictionary that will be shown off
        result = max_duration_movie
        #result = f'{max_duration_movie.title} IS THE MOVIE WHICH HAS A MAX DURATION OF {max_duration_movie.duration_int.max()}'
        return {'movie:': result}
    except ValueError as e:
        return {"ERROR": str(e)}
'''''    
#2. Cantidad de películas (sólo películas, no series, etc) según plataforma, 
#con un puntaje mayor a XX en determinado año. La función debe llamarse get_score_count(platform, scored, year) 
# y debe devolver un int, con el total de películas que cumplen lo solicitado. 
'''
@app.get("/get_score_count/{platform}/{scored}/{year}")
def get_score_count(platform:Optional[str]=None, scored:Optional[float]=None, year:Optional[int]=None):
    platforms_df_copy = platforms_df.copy()
    platformList = ['amazon', 'disney', 'hulu', 'netflix']
    try:
        if (platform == '' or platform not in platformList):
            return ValueError('PLATFORM NAME IS WRONG, YOU MUST WRITE amazon, disney, hulu OR netflix.')
        movies = platforms_df_copy[(platforms_df_copy.platform==platform) & (platforms_df_copy.score >=  scored) & (platforms_df_copy.release_year== year) & (platforms_df_copy.type=='movie')]
        result = movies.shape[0]
        return {
        'platform': platform,
        'quantity': result,
        'year': year,
        'score': scored
            }
    except ValueError as e:
        return {"ERROR": str(e)}

'''
3. Cantidad de películas (sólo películas, no series, etc) según plataforma. 
La función debe llamarse get_count_platform(platform) y debe devolver un int, 
 con el número total de películas de esa plataforma. 
 Las plataformas deben llamarse amazon, netflix, hulu, disney.
'''
@app.get("/get_count_platform/{platform}")
def get_count_platform(platform: Optional[str] = None):
    # Creating a copy from original data in order to avoid any modification
    platforms_df_copy = platforms_df.copy()
    platformList = ['amazon', 'disney', 'hulu', 'netflix']
    try:
        if (platform == '' or platform not in platformList):
            return ValueError('PLATFORM NAME IS WRONG, YOU MUST WRITE amazon, disney, hulu OR netflix.')
        # Computing the amount of movie acording to the platform
        amountMovies = platforms_df_copy[(platforms_df_copy.type=='movie') & (platforms_df_copy.platform == platform)]
        result = amountMovies.shape[0]
        return {'platform': platform, 'movies': result}
    except ValueError as e:
        return {"ERROR": str(e)}

'''
4. Actor que más se repite según plataforma y año. La función debe llamarse get_actor(platform, year) 
y debe devolver sólo el string con el nombre del actor que más se repite según la plataforma y el año dado.
'''
@app.get("/get_actor/{platform}/{year}")
def get_actor(platform:Optional[str]=None, year:Optional[int]=None):
    platforms_df_copy = platforms_df.copy()
    platformList = ['amazon', 'disney', 'hulu', 'netflix']

    try:
        if (platform == '' or platform not in platformList):
            return ValueError('PLATFORM NAME IS WRONG, YOU MUST WRITE amazon, disney, hulu OR netflix. ')
        cast =platforms_df_copy.cast[(platforms_df_copy.platform == platform) & (platforms_df_copy.release_year==year) & (platforms_df_copy.cast!='no data')]
        cast =cast.str.split(',')
        cast = cast.explode(['cast'])
        result = cast.describe()[2].strip(' ')
        appearances = cast.value_counts(ascending=False).to_list()[0]
        return {
        'platform': platform,
        'year': year,
        'actor': result,
        'appearances': appearances
        }
    except ValueError as e:
        return {"ERROR": str(e)}

'''
5. La cantidad de contenidos/productos (todo lo disponible en streaming) que se publicó por país y año. 
La función debe llamarse prod_per_county(tipo,pais,anio) deberia devolver el tipo de contenido (pelicula,serie)
por pais y año en un diccionario con las variables llamadas 'pais' (nombre del pais), 'anio' (año), 'pelicula' (tipo de contenido).
'''
@app.get("/prod_per_county/{type}/{country}/{year}")
def prod_per_county(type:Optional[str]=None,country:Optional[str]=None, year:Optional[int]=None):
    platforms_df_copy = platforms_df.copy()

    try:
        movies = platforms_df_copy.country[(platforms_df_copy.release_year == year) & (platforms_df_copy.type== type) & (platforms_df_copy.country!='no data')]
        movieList = movies.str.split(',')
        movieList = movieList.explode(['country'])
        result = movieList[movieList == country].shape[0]
        return  {'country': country, 'year': year, 'contenido': result}
    except ValueError as e:
        return {"ERROR": str(e)}
    
'''
6. La cantidad total de contenidos/productos (todo lo disponible en streaming, series, peliculas, etc)
    según el rating de audiencia dado (para que publico fue clasificada la pelicula).
    La función debe llamarse get_contents(rating) y debe devolver el numero total de contenido con ese rating de audiencias.
'''
@app.get("/get_contents/{rating}")
def get_contents(rating:Optional[str]=None):
    platforms_df_copy = platforms_df.copy()

    try:
        movies = platforms_df_copy[platforms_df_copy.rating == rating]
        result = movies.shape[0]
        return  {'rating': rating, 'content': result}
    except ValueError as e:
        return {"ERROR": str(e)}

##########recommendation function
@app.get('/get_recomendation/{title}')
def get_recomendation(title:Optional[str]=None):
    platforms_df_copy = platforms_df.copy()
    try:
    # Loading just two columns from CSV file call totalPlatforms using pandas.
        desc = platforms_df_copy[['title','description']]
    # Getting the description of the movie title given.
        desc = platforms_df_copy[platforms_df_copy['title'] == title]['description'].values[0]

    # Computing  TF-IDF features for all descriptions.
        tfidf = TfidfVectorizer()
        tfidf_matrix = tfidf.fit_transform(platforms_df_copy['description'])

    # Computing cosine similarities between description and move titles and all the other descriptions.
        tfidf_similarities = cosine_similarity(tfidf_matrix, tfidf.transform([desc]))

    # getting top 10 indexes of films wich best matech according to TF-IDF.
        tfidf_similar_movie_indices = tfidf_similarities.argsort(axis=0)[-10:][::-1].flatten()

    # Turn indexes into movie titles  
        tfidf_similar_movie_titles = platforms_df.loc[tfidf_similar_movie_indices, 'title'].tolist()
        result = tfidf_similar_movie_titles[1:6]
        return {'recommendation': result}
    except ValueError as e:
        return {"ERROR": str(e)}
    