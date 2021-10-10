## End-to-End Airline Twitter Sentiment Analysis NLP project

The methods used along to analyse and predict the sentiment is as follows:
1. Text/Data Preprocessing: I used neattext nlp_library functions to remove special characters,stopwords(not usedul for review analysis),did lemmatisation to find root words for same meaning words etc..
2. After Preprocessing, text data should be converted to machine understandable manner i.e. one-hot encoded(Count Vectorizer#Bag of Words) or list of vector of words(Word2Vec#Word Embedding) 
3. Most of the times Text data is imbalanced, so i checked that first and applied smote() oversampling technique..
4. splitted the data into train and validation..
5. Applied random_forest,SVC,Multinomial Naive_bayes, and finally naive bayes..
6. Neural Network is applied to check accuracy improvement.. in that i flatten the input vectors through gru for best features..and then feed to dense layers...
7. Source Code is Available in twitter-Airline-sentiment.ipynb file

## Libraries Used:



Here is My Airline Sentiment Analysis Webapp Link:
https://airline-sentiment-sam-app.herokuapp.com/
