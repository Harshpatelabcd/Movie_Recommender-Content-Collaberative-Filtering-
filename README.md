# Movie_Recommender-Content & Collaberative-Filtering

# Dataset Link: https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset
1. Rating.csv (Rating value-0.5 to 5)
2. Movies_metedata.csv
3. Users.csv
4. credits.csv

# API link: https://newsapi.org/
- To fetch the latest article based movies and entertainment.
- Installation: $ pip install newsapi-python

# Python Libraries
1. NLTK
2. scikit-learn
3. Requests
4. NewsApiClient
5. MySQL Connector
6. NumPy
7. Pandas

# Popularity Based: Based on the user's rating, it will identify the most popular movies which are highest rated among all users.
1. Top 20 highest rated movies
2. Based on genre: Highest rated action,comedy,crime,drama and adventure movies.
3. Based on releasing Year: Highest rated movies during 90's.
4. Based on language: Highest rated foreign movies.

# Collaberative Filtering 
-Collaborative filtering is a technique that can filter out items that a user might like on the basis of reactions by similar users.

=> Cosine Similarity: It measures the similarity between two vectors of an inner product space. It is measured by the cosine of the angle between two vectors and determines whether two vectors are pointing in roughly the same direction. A cosine similarity is a value that is bound by a constrained range of 0 and 1. The closer the value is to 0 means that the two vectors are orthogonal or perpendicular to each other. When the value is closer to one, it means the angle is smaller and the items are more similar. 

=> STEPS:
1. For getting better results the criteria is set for the movies who has minimum 30 ratings and users who has rated on minimum 30 movies.
2. Creating pivot table of columns:User-Id, index:Movie-Id with the value of rating on each movies by all the users.

  ![pt](https://github.com/Harshpatelabcd/Movie_Recommender-Content-Collaberative-Filtering-/assets/73551662/30ce0fad-4d5b-4d27-abd5-c6a1fa0a78f9)
 
3. Identify the Uclidian Distance between the all the movies.
   
  ![uclidian](https://github.com/Harshpatelabcd/Movie_Recommender-Content-Collaberative-Filtering-/assets/73551662/5ebad5ec-81e1-4587-ab2b-1249c0f72b8c)
 
4. Higher the value of uclidian distance, more similar the movie.

  ![cosine_similarity](https://github.com/Harshpatelabcd/Movie_Recommender-Content-Collaberative-Filtering-/assets/73551662/5ab749ab-51fb-485d-b8fe-cc543068fceb)

# Content-Based Filtering
-This type of recommendation systems, takes in a movie that a user currently likes as input. Then it analyzes the contents (storyline, genre, cast, director etc.) of the movie to find out other movies which have similar content.

=> Text Vectorization (Bags of Words): Text vectorization serves as a cornerstone in NLP, enabling machines to process and extract meaning from textual data. It  can transform raw text into numerical representations that facilitate various NLP tasks.

=> STEPS:
1. Creating a vector of content (movie story, cast, director and genre) identify as 'TAG'
   ![tags](https://github.com/Harshpatelabcd/Movie_Recommender-Content-Collaberative-Filtering-/assets/73551662/448da5da-287c-4fc8-aecc-817e350c719c)

   ![vector](https://github.com/Harshpatelabcd/Movie_Recommender-Content-Collaberative-Filtering-/assets/73551662/edaf8ff8-92d5-4bd6-b10d-924dc672f43b)

2. Apply stemming process of reducing a word to its word stem that eliminate the extra affixes, suffixes and prefixes.

   ![stemmer](https://github.com/Harshpatelabcd/Movie_Recommender-Content-Collaberative-Filtering-/assets/73551662/e21a6d9e-d1ff-4b9d-94e4-77e72cb455a9)

3. Compute the cosine similarity.
   -K(X, Y) = <X, Y> / (||X||*||Y||)
4. Higher the value, more similar the movies.
  
# UI Design
![FilmyBoxed-GoogleChrome2024-02-2723-26-11-ezgif com-video-to-gif-converter (2)](https://github.com/Harshpatelabcd/Movie_Recommender-Content-Collaberative-Filtering-/assets/73551662/512e30de-49a9-479f-a739-b1cf40b8ff91)

![FilmyBoxed-GoogleChrome2024-02-2723-27-11-ezgif com-video-to-gif-converter](https://github.com/Harshpatelabcd/Movie_Recommender-Content-Collaberative-Filtering-/assets/73551662/4203b3d0-6d80-416a-a027-beae19bdc17e)

Recommendation:
![Screenshot_27-2-2024_233050_127 0 0 1](https://github.com/Harshpatelabcd/Movie_Recommender-Content-Collaberative-Filtering-/assets/73551662/8339569f-592c-40ce-900f-52185de945b2)



  
  







