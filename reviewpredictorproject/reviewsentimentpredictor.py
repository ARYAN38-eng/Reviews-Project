import streamlit as st 
st.header("Review Sentiment Predictor")
import pickle
import numpy as np
import pandas as np

model=pickle.load(open('pipeReviews.pkl','rb'))

user_input=st.text_area("Enter the Review here...")
your_review=st.write("Your given review:",user_input)
#from sklearn.feature_extraction.text import TfidfVectorizer
#tfidf_vectorizer = TfidfVectorizer(max_features=5000)  
review_list = [user_input]
#test=tfidf_vectorizer.fit_transform(review_list)
model1=model.predict(review_list)[0]
if model1 == 0:
    st.write("Negative Review")
elif model1==1:
    st.write("Neutral Review")
else:
    st.write("Positive Review")
    