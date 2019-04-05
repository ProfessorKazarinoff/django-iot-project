# channels/views.py

from django.shortcuts import render
# what we're going to return when a request is sent
from django.http import JsonResponse
from django.views.generic import ListView
from .models import Channels
from iot_data.models import IotData

# Create your views here.

class ChannelListView(ListView):
    model = IotData
    template_name = 'channel_listing.html'

# from Zach's gist: https://gist.github.com/kazarinoff/9e1e0dae9b51383333610df6c7b6cd2c

# an ok explanation of function vs. class based views: https://simpleisbetterthancomplex.com/article/2017/03/21/class-based-views-vs-function-based-views.html

#CREATE an entry into the database- often we would only allow POST Requests w/ "if method.POST:...", but doesn't actually matter in practical terms.
#this is for entryAttributes that are in the url params like you've done...
def createmydatabaseentry(request, entryAttribute1, entryAttribute2):
  #create a database object/entry using the django Object Relational Manager-ORM. MyDatBaseObject is whatever your Model object is.
  entry=MyDataBaseObject.objects.create(attr1=entryAttribute1,attr2=entryAttribute2)
  #returns Jsondata to whatever is calling the API. For your purposes it could return whatever, 
  #this just can test that it works correctly. You could also put some logic into the sensor to do something if it doesn't get a 'good' message back.
  return JsonResponse({'msg':"You successfully added me to the database", 'object':entry},safe=False)

#pull one entry- generally called 'show' in RESTful architecture
def showmydatabaseentry(request,entryID):
  
  #pull the entry from the db using djangos ORM.
  entry=MyDataBaseObject.objects.get(id=entryID)
  
  #translate the entry into a JsonObject- this part is annoying and dumb. You can create a method to your databasemodel to do it, 
  #since you're going to do it in a bunch of api views but you can also just copy this code.
  entrydict={'id':entry.id,'attr1':entry.attr1,'attr2'=entry.attr2}
  return JsonResponse(entrydict,safe=False)
  
#pull all entries- generally called 'index' method, or sometimes 'show all'
def indexdatabaseentrys(request):
  
  #pull all the entries from the db
  entrys=MyDataBaseObject.objects.all()
  entryarray=[]
  for entry in entrys:
      entryarray.append({'id':entry.id,'attr1':entry.attr1,'attr2'=entry.attr2})
      return JsonResponse({'entrys':entryarray},safe=False)
  
