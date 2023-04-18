<div align="center">

![](https://camo.githubusercontent.com/35b81f213ddb0e019b3567f6982d740bb2d01ae5dd712a1537e09e826e940228/68747470733a2f2f643331757a386c77666d796e38672e636c6f756466726f6e742e6e65742f4173736574732f6c6f676f2d68656e72792d77686974652d6c672e706e67)

</div>
<center><h1><b> 
	 INDIVIDUAL PROJECT Nº1 <br>
<h1>Machine Learning Operations (MLOps)</h1> </b></h1></center><br>
	



<div align="center"> Henry's Labs <br>
	 by  William Andres Agurto Prado (DTS-09) </div>

<div align="center">

![](https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png)

</div>

### **Project Estructure**

------------
This is my first individual project focus on doing ETL(Extract, Transform and load), EDA (Exploratory data Analysis).<br><br>

### **Project Development**

------------
**1. ETL Process Stage ➡️**
Main file: [etl_principal.ipynb](https://github.com/WilliamAgurto/PI_01_ML_OPS/blob/master/ETL.ipynb)
- The ETL (Extraction, Transformation, and Load) process was carried out.
- The necessary dataframes for the process were prepared, resulting from the treatment of the four provided datasets (amazon_prime_titles.csv, disney_plus_titles.csv, hulu_titles.csv, netflix_titles.csv) of movies and series (titles).
- A single dataframe was prepared for the treatment of the eight provided datasets with information on the ratings.
- The required MVP (Minimum Viable Product) tasks were performed by:<br>

		i. Generating an ID field with the first letter of the platform name, followed by the show_id already present in the datasets.<br>

		ii.Replacing the null values in the 'rating' field with the string "G".<br>
	
		iii.Setting the date fields to the format YYYY-mm-dd.<br>
	
		iv. Doing All text fields were converted to lowercase.<br>
	
		v. Spliting the 'duration' field  into two fields: 'duration_int' (integer type) and 'duration_type' (string type).<br>

**2. API Development Stage ➡️**
Main file: [main.py](https://github.com/WilliamAgurto/PI_01_ML_OPS/blob/master/FirstApi/main.py)
- The process of making the information available through the FastAPI framework was carried out.
- The Render cloud was used to deploy the project.
[Access to the documentation on render.com](http://127.0.0.1:8000/docs#/default/get_score_count_score_count_get) where you can access all the developed queries.

- The required MVP queries (functions) were performed:<br>

		i. Function get_max_duration: movie with the longest duration with filter options for Year, Platform, and Duration Type.<br>

		ii.Function get_score_count: number of movies per platform with a score greater than a certain number (from 1 to 5) in a specific year.<br>

		iii.Function get_count_platform: number of movies per platform with a Platform filter.<br>

		iv.Function get_actor: actor that appears the most times according to Platform and Year.<br>

		v. Function prod_per_county: return the amount of content according to type, country and year.<br>

		vi. Function get_contents: return the amount of content according to the rating.<br>
    
		vii. Function get_recomendation: return top 5 the best match according to the title.<br><br>


**3. Exploratory Data Analysis Stage ➡️** Main file: [eda_principal.ipynb](https://github.com/WilliamAgurto/PI_01_ML_OPS/blob/master/EDA.ipynb)

- The required MVP tasks were performed:
- The dataframes (titles and scores/ratings) were analyzed in terms of their structure, shape, information, null values, duplicate values, etc.
- Histograms were created with Matplotlib and Seaborn to obtain a general overview of the data distribution of the movie and series dataframe.<br><br>

**4. Recommendation System Stage ➡️**
Main file: [RecommendationSystem.ipynb](https://github.com/WilliamAgurto/PI_01_ML_OPS/blob/master/RecomendationSystem.ipynb)
- The Surprise library was used, based on the SVD algorithm.
- Also, it was used TfidfVectorizer library in order to achieve project requests and this was used on FastApi.<br><br>

**Data Source  ➡️** [Data](https://github.com/WilliamAgurto/PI_01_ML_OPS/tree/master/datasets)
------------

Dataset: The ['ratings'](https://github.com/WilliamAgurto/PI_01_ML_OPS/tree/master/datasets/ratings) folder contains several files with user reviews, and the root folder contains a dataset for each streaming service provide.<br><br>

**Supporting Material ⚪** 
------------

In this same repository, you can find some helpful links. they were useful to achive the project requests.<br>
Click on [here](https://github.com/WilliamAgurto/PI_01_ML_OPS/blob/master/SupportMaterial.md) if you want to check some of them.
