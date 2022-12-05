from django.http import HttpResponse
from django.shortcuts import render
import requests
import translators as ts
from bs4 import BeautifulSoup
from gingerit.gingerit import GingerIt

def home(request):
    return render(request,'home.html')
def logic(request):
    url=request.GET.get('url')
    r=requests.get(url)
    htmlContent = r.content
    soup=BeautifulSoup(htmlContent,'lxml')
    topic=soup.find('h1')
    headline=soup.find_all('p')
    print(headline)
    image=soup.find('img',"")
    data=headline[7:len(headline) - 5]
    desc=""""""
    desc2=""""""
    ts._google.language_map
    for i in data:
        tran_text=str(ts.google(str(i.get_text()),from_language='hi', to_language='en'))
        desc2+=tran_text
        desc+="<p>"+tran_text+"</p>"
    print(desc2)





    return HttpResponse("<textarea style='width: 704px; height: 52px;'>"+ts.google(str(topic.get_text()),from_language='hi', to_language='en')+"</textarea><div contenteditable='true' style='height:400px'>"+desc+"</div>"+str(image))

