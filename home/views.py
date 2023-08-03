from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
# index
def index(request):
    now =  datetime.now()
    html = f'''
        <html><body>
            <h1>The time</h1>
            <p>The time is { now }.</p>
        </body></html>
    '''
    return HttpResponse(html)