## End-to-End Airline Twitter Sentiment Analysis NLP project


The methods used along to analyse and predict the sentiment is as follows:
1. Text/Data Preprocessing: I used neattext nlp_library functions to remove special characters,stopwords(not usedul for review analysis),did lemmatisation to find root words for same meaning words etc..
2. After Preprocessing, text data should be converted to machine understandable manner i.e. one-hot encoded(Count Vectorizer#Bag of Words) or list of vector of words(Word2Vec#Word Embedding) 
3. Most of the times Text data is imbalanced, so i checked that first and applied smote() oversampling technique..
4. splitted the data into train and validation..
5. I have done PCA to visualise the best fit model to our data
6. Applied random_forest,SVC,Multinomial Naive_bayes, and finally naive bayes..
7. Neural Network is applied to check accuracy improvement.. in that i flatten the input vectors through gru for best features..and then feed to dense layers...

![image](https://user-images.githubusercontent.com/73512374/179816831-54755849-97ac-4f9c-8083-2d240ca4e48a.png)

Here is the image of the framework i applied for neural network processing
![image](https://user-images.githubusercontent.com/73512374/136689327-c3a2461f-9cf8-48d5-b273-e5ea5993bf55.png)

9. Source Code is Available in twitter-Airline-sentiment.ipynb file

## Libraries Used:
1. Tensorflow
2. Neattext
3. Numpy
4. Pandas
5. Matplotlib
6. WordCloud
7. Sci-kit learn
8. gensim for Word2Vec

## Performance:
1. Accuracy for Random Forest         = 95%
2. Accuracy for MultinomialNaiveBayes = 75%
3. Accuracy for SVM                   = 65%
4. Accuracy for neural network        = 96%


Here is My Airline Sentiment Analysis Webapp Link:
https://airline-sentiment-sam-app.herokuapp.com/

