from flask import Flask, render_template, url_for, request,redirect
from flask import Flask, render_template
from newsapi import NewsApiClient
from flask_sqlalchemy import SQLAlchemy
from flask import *
import pickle
import numpy as np
import pandas as pd
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import mysql.connector

#Popularity_df pkl files
popular_df = pd.read_pickle(open('populardf.pkl', 'rb'))
top_action = pd.read_pickle(open('top_action.pkl', 'rb'))
top_adv = pd.read_pickle(open('top_adv.pkl', 'rb'))
top_crime = pd.read_pickle(open('top_crime.pkl', 'rb'))
top_comedy = pd.read_pickle(open('top_comedy.pkl', 'rb'))
top_drama = pd.read_pickle(open('top_drama.pkl', 'rb'))
top_intl = pd.read_pickle(open('top_intl.pkl', 'rb'))
top_ninetys = pd.read_pickle(open('top_ninetys.pkl', 'rb'))

#Collabarative-Filtering pkl files
pt1 = pd.read_pickle(open('pt1.pkl', 'rb'))
similarity_scores = pd.read_pickle(open('similarity_scores.pkl', 'rb'))
movies_list = pd.read_pickle(open('movies.pkl', 'rb'))

#Content-Filtering pkl files
Tokenized_movielist = pd.read_pickle(open('Tokenized_movielist.pkl', 'rb'))
content_similarity = pd.read_pickle(open('content_similarity.pkl', 'rb'))

app = Flask(__name__, template_folder='templates')

#To establish the connection with XAMPP server
app.secret_key = 'Harsh' 
app.config['MYSQL_USER'] = 'HARSH'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'rec_users'
app.config['MYSQL_PORT'] = 3307
mysql = MySQL(app)


#-----------------------------------------Registation-----------
@app.route('/registration',methods=["GET", "POST"])
def register():
    message = ''
    if request.method == 'POST' and 'password' in request.form and 'email' in request.form and 'firstname' in request.form  and 'confirm_password' in request.form:
        
        password = request.form['password']
        email = request.form['email']
        firstname = request.form['firstname']        
        confirm_password = request.form['confirm_password']
        message=''
        #establishing the pointer...
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE email = % s', (email, ))
        account = cursor.fetchone()
        if account:
            message = 'Account already exists !'
            return render_template('registration.html', message=message)

        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            message = 'Invalid information !'
            return render_template('registration.html', message=message)
        
        elif not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$', password):
            message = 'Invalid password !'
            return render_template('registration.html', message=message)

        elif not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$', confirm_password):
            message = 'Invalid password !'
            return render_template('registration.html', message=message)    

        elif not password or not email or not firstname or not confirm_password:
            message = 'Please fill out the form !'
            return render_template('registration.html', message=message)
        else:
            cursor.execute(
                'INSERT INTO users VALUES (NULL, % s, % s, % s, %s)', 
                      (firstname, email, password, confirm_password))
            mysql.connection.commit()
            
    elif request.method == 'POST':
        message = 'Please fill out the form !'
        return render_template('registration.html')
    
    return render_template('login.html')


#-------------------------------------------Login-----------------------------------------------------
@app.route('/login')
def login1():
    newsapi = NewsApiClient(api_key="8f0e8a030b7149cab845ec046d68a5b4")
    topheadlines = newsapi.get_everything(q="movies",page_size=18,sort_by="relevancy")
    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    link = []
  
    for i in range(len(articles)):
        myarticles = articles[i] 
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        link.append(myarticles['url'])
  
    mylist = zip(news, desc, img, link)
    return render_template('login.html',context = mylist)


@app.route('/login',methods=["GET", "POST"])
def login():
    message = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE email = % s AND password = % s', (email, password, ))
        user = cursor.fetchone()

        # session for login and registration system 
        if user:
            session['loggedin'] = True
            session['id'] = user['id']
            session['firstname'] = user['firstname']
            session['email'] = user['email']
            message = 'Logged in successfully !'
            
            return render_template('userhomepage.html',                           
                           image=list(popular_df['image1'].values),
                           id=list(popular_df['id'].values),
                           

                           image_action=list(top_action['image1'].values),
                           id_action=list(top_action['id'].values),

                           image_adv=list(top_adv['image1'].values),
                           id_adv=list(top_adv['id'].values),

                           image_comedy=list(top_comedy['image1'].values),
                           id_comedy=list(top_comedy['id'].values),
                            
                           image_crime=list(top_crime['image1'].values),
                           id_crime=list(top_crime['id'].values),

                           image_drama=list(top_drama['image1'].values),
                           id_drama=list(top_drama['id'].values),
                           
                           image_intl=list(top_intl['image1'].values),
                           id_intl=list(top_intl['id'].values),
                           
                           image_ninetys=list(top_ninetys['image1'].values),
                           id_ninetys=list(top_ninetys['id'].values)                           
                           )

        else:
            message = 'Please enter correct email / password !'
    return render_template('login.html', message=message)


#------------------------------------Searching Movies--------------------------------------------------
@app.route('/searchmovies',methods=['GET', 'POST'])
def search():
    movie_title = request.form.get('movie_search', False)
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM movies WHERE original_titles LIKE '%%%s%%' LIMIT 27" % (movie_title))
    data2 = cursor.fetchall()
    print(data2)
    return render_template('search_result.html',data2=data2)

#Rating Management...........
@app.route('/rating', methods=['post', 'get'])
def process():
    rating_data = request.form.get('data')
    result = str(float(rating_data))     
    mo_id = request.form.get('id_data') 
    user_id = session['id']
    message=''
    #print(mo_id)
    #print(result)
    #print(user_id)
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM rating WHERE uid = % s AND mid = % s', (user_id,mo_id, ))
    initial_rating = cursor.fetchone()
    if initial_rating:

        cursor.execute(
                'UPDATE rating SET rating= % s WHERE uid = % s AND mid = % s',(result,user_id,mo_id, )
                 )
        mysql.connection.commit()
        
        return message
    else:
        cursor.execute(
                'INSERT INTO rating VALUES (NULL,% s, % s, % s)', 
                      (user_id,mo_id,result))
        mysql.connection.commit()
        
        return message

#-----------------------------------------FILTERING---------------------------------------------------------------
@app.route('/id')
def movie_id():
    movies_id = request.args.get('m_id') 
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM movies where id= %s",(movies_id,))
    data2 = cursor.fetchone()

    try:
    #--------------------------------------Collabarative-Filtering------------------------------------------------
        index_1 = next((i for i, m_id in enumerate(pt1.index) if m_id == movies_id), None)        
        similar_items = sorted(list(enumerate(similarity_scores[index_1])), key=lambda x: x[1], reverse=True)[1:10]
        data = []
        #print(movies_id)
        #print(pt1.index)
        #print(index_1)
        for i in similar_items:
            item = []
            temp_df = movies_list[movies_list['id'] == pt1.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('id')['id'].values))
            item.extend(list(temp_df.drop_duplicates('id')['image1'].values))
            #print(data)
            data.append(item)

     #--------------------------------------Content-Filtering------------------------------------------------
        movie_index = Tokenized_movielist[Tokenized_movielist['id'] == movies_id].index[0]
        distances = content_similarity[movie_index]
        contentmovies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:10]
        data1 = []    
        for i in contentmovies_list:
            item1 = []
            content_df = Tokenized_movielist[Tokenized_movielist['id']==Tokenized_movielist.iloc[i[0]].id]
            item1.extend(list(content_df.drop_duplicates('id')['id'].values))
            item1.extend(list(content_df.drop_duplicates('image1')['image1'].values))        
            #print(data1)
            data1.append(item1)

        #result
        return render_template('movie_Detail.html', data=data, data1 = data1,
                            fetch_id = data2['id'],
                            fetch_image2 = data2['image2'],                            
                            fetch_original_title = data2['original_titles'],
                            fetch_genres = data2['genres'],
                            fetch_cast = data2['cast'],
                            fetch_crew = data2['crew'],
                            fetch_image1 = data2['image1'],                            
                            fetch_runtime = data2['runtime'],
                            fetch_overview = data2['overview'],
                            fetch_avgrating = data2['avg_rating'],
                            fetch_lang = data2['original_language'],
                            fetch_year = data2['release_date'])

    except IndexError:
        return render_template('error.html')


#Routing..............    
@app.route('/registration_ui')
def userhome():
    return render_template('registration.html')

#Session end........
@app.route("/logout")
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('email', None)
    return redirect(url_for('login'))

#API Results.......
@app.route('/')
def index():
    newsapi = NewsApiClient(api_key="8f0e8a030b7149cab845ec046d68a5b4")
    topheadlines = newsapi.get_everything(q="movies",page_size=18,sort_by="relevancy")
    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    link = []
  
    for i in range(len(articles)):
        myarticles = articles[i] 
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        link.append(myarticles['url'])

    mylist = zip(news, desc, img, link)
    return render_template('index.html',context = mylist)


if __name__ == 'main':
    app.run(debug=True)
    