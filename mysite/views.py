# I have created this file -nidhish 
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params={'name':'nidhish', 'place':'bangalore'}
    return render(request,'index.html',params)
   
     

def analyze(request):
    #get the text 
    dj_text=request.POST.get('text','default')
    remoPuncVar=request.POST.get('removepunc','off')
    print(dj_text)
    print(remoPuncVar)
    analyzeText=""
    punctunationList='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    if remoPuncVar == 'on':
        for char in dj_text:
            if char not in punctunationList:
                analyzeText+=char
        
    else:
        analyzeText=dj_text
    params={'developer' : "Remove Punctuations" , 'analyze_text': analyzeText}
    return render(request,'analyze.html',params)
