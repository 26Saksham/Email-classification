from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from sklearn.feature_extraction.text import TfidfVectorizer
import string
import nltk
from nltk.corpus import stopwords
import pickle
import pandas as pd

def process_text(text):
    #remove punctuation from the text
    nopun = [char for char in text if char not in string.punctuation]
    nopun = ''.join(nopun)

    #remove stop words
    removeStopWord = [word for word in nopun.split() if word.lower() not in stopwords.words('english')]

    return removeStopWord


v = TfidfVectorizer(analyzer=process_text)

def Email_classifier(text,v,model): 
    messageConvertToMatrix = v.transform([text])

    print(messageConvertToMatrix.shape)
    checkSpam = model.predict(messageConvertToMatrix)[0]
    if(checkSpam == 0):
        return 'Not a Spam'
    return 'Spam'


model = pickle.load(open('email_classification_model', 'rb'))
v = pickle.load(open('v', 'rb'))
def home(request):
    return render(request, './index.html')

def EmailClassification(request):
    email = request.POST['emailText']
    result=Email_classifier(email,v,model)
    return render(request,'./index.html',{'data':result})