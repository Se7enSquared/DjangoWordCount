from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter
import operator
import string

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist= fulltext.split(' ')
    wordlist = [''.join(c for c in s if c not in string.punctuation) for s in wordlist]
    worddict = Counter(map(str.lower, wordlist))
    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 
                  'wordcounts': sortedwords})

def about(request):
    return render(request, 'about.html')