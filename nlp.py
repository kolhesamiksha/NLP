import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from textblob import TextBlob


st.title('Airline Tweet Sentiment Analysis:airplane:')
st.markdown('This application is all about tweet sentiment analysis of airlines. We can analyse and predict the sentiment behind their reviews')

st.sidebar.title('Sentiment analysis of airlines')

st.sidebar.markdown(":beginner:We can analyse and predict sentiment of passengers review from this application:beginner:")

data=pd.read_csv('Tweets.csv')

if st.checkbox("Show Data"):
    st.write(data.head(50))
st.sidebar.subheader('Tweets Analyser')

tweets=st.sidebar.radio('Sentiment Type',('positive','negative','neutral'))
st.write(data.query('airline_sentiment==@tweets')[['text']].sample(1).iat[0,0])
st.write(data.query('airline_sentiment==@tweets')[['text']].sample(1).iat[0,0])
st.write(data.query('airline_sentiment==@tweets')[['text']].sample(1).iat[0,0])

st.sidebar.subheader('Sentiment Predictor')
if st.sidebar.checkbox("Let's predict"):
    input = st.text_input("Enter Your Reviews...")
    score = TextBlob(input).sentiment.polarity
    if st.button("Predict"):

        if score==0:
            st.write(":neutral_face:")
        elif score<0:
            st.write(":white_frowning_face:")
        elif score>0:
            st.write(":grinning_face_with_star_eyes:")

select=st.sidebar.selectbox('Visualisation Of Tweets',['Histogram','Pie Chart'],key=2)
sentiment=data['airline_sentiment'].value_counts()
sentiment=pd.DataFrame({'Sentiment':sentiment.index,'Tweets':sentiment.values})
st.markdown("###  Sentiment count")
if select == "Histogram":
        fig = px.bar(sentiment, x='Sentiment', y='Tweets', color = 'Tweets', height= 500)
        st.plotly_chart(fig)
else:
        fig = px.pie(sentiment, values='Tweets', names='Sentiment')
        st.plotly_chart(fig)


st.sidebar.markdown('Time & Location of tweets')
hr = st.sidebar.slider("Hour of the day", 0, 23)
data['Date'] = pd.to_datetime(data['tweet_created'])
hr_data = data[data['Date'].dt.hour == hr]
if not st.sidebar.checkbox("Hide", True, key='1'):
    st.markdown("### Location of the tweets based on the hour of the day")
    st.markdown("%i tweets during  %i:00 and %i:00" % (len(hr_data), hr, (hr+1)%24))


st.sidebar.subheader("Airline tweets by sentiment")
choice = st.sidebar.multiselect("Airlines", ('US Airways', 'United', 'American', 'Southwest', 'Delta', 'Virgin America'), key = '0')
if len(choice)>0:
    air_data=data[data.airline.isin(choice)]
    # facet_col = 'airline_sentiment'
    fig1 = px.histogram(air_data, x='airline', y='airline_sentiment', histfunc='count', color='airline_sentiment',labels={'airline_sentiment':'tweets'}, height=600, width=800)
    st.plotly_chart(fig1)



