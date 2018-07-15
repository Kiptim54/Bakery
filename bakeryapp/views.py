from django.shortcuts import render

# Create your views here.

def index(request):
    '''
    home page for Bakery
    '''
    title="Bakery | Home Page"
    return render(request, 'home/index.html',{"title":title})