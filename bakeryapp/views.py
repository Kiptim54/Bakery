from django.shortcuts import render

# Create your views here.

def index(request):
    '''
    home page for Bakery
    '''
    title="Bakery | Home Page"
    return render(request, 'home/index.html',{"title":title})

def contact(request):
    '''
    contact page to receive email from clients
    '''
    title='Bakery | Contact us'
    return render(request, 'home/contact.html', {"title":title})
