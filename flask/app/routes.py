#https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

from flask import Flask, render_template, redirect, request
from app import app
#import heapq
#import numpy as np
import pandas as pd
import pickle 
import re
#from sklearn.metrics.pairwise import linear_kernel
#from sklearn.feature_extraction.text import TfidfVectorizer

    
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('quiz 18.html')#, title='Home', user=user)
    
    
@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        #print(request.form.getlist("check"))
        cityname=request.form.get("check") #take cityname from website, return best match
       

        citydf = pd.read_csv('city_' +cityname+ '_df.csv', index_col=None)
        citydf.rename(columns = {'pic': 'Picture',
                                'name': 'Name', 
                                'type': 'Type',                                 
                                'my_rank': 'Rank',
                                'rating': 'Rating<br>(out of 5)', 
                                'ranking': 'Tripadvisor<br>popularity'}, inplace=True)
        citydf.drop(['num_reviews'],axis=1,inplace=True)
        table_to_print = citydf.to_html(index=False, escape=False, justify='center', classes='sortable')
        table_to_print = re.sub('<th>(?=Tripadvisor<br>popularity</th>)', '<th class="sorttable_numeric">', table_to_print)
        table_to_print = re.sub('<td>(?=\?</td>)', '<td sorttable_customkey="99999999">', table_to_print)


        citywords = pickle.load(open('city_' + cityname + '_keyword_list.pkl', 'rb'))


        return render_template('result.html', send_name= cityname, senddf=table_to_print, keyword1=citywords[0], keyword2 = citywords[1], keyword3=citywords[2], keyword4=citywords[3], keyword5=citywords[4]) 
        #return render_template('result.html', sendtext=cityname)
        #return render_template('result.html')
        
        
@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')#, title='Home', user=user)        


if __name__ == '__main__':
    app.run(debug=True)
