from django.shortcuts import render
import  requests
import json
from django.views.generic import View

# Create your views here.
#
# import requests
#
# url = "https://love-calculator.p.rapidapi.com/getPercentage"
#
# querystring = {"fname":"f1","sname":"f2"}
#
# headers = {
#     'x-rapidapi-host': "love-calculator.p.rapidapi.com",
#     'x-rapidapi-key': "baf14f4f41mshb086d71364eb03bp1ccc81jsne4c1b024005c"
#     }
#
# response = requests.request("GET", url, headers=headers, params=querystring)



# class LoveCalculator(View):
#     def get(self,request):
#         return render(request,"love.html")
#     def post(self,request):
#         # f1=request.POST.get('l1')
#         # f2=request.POST.get('l2')
def loveCalculator(request):
    if request.method=="POST":
         s1=request.POST['l1']
         s2=request.POST['l2']
         url = "https://love-calculator.p.rapidapi.com/getPercentage"

         querystring = {"fname": s1, "sname": s2}

         headers = {
                      'x-rapidapi-host': "love-calculator.p.rapidapi.com",
                      'x-rapidapi-key': "baf14f4f41mshb086d71364eb03bp1ccc81jsne4c1b024005c"
                 }

         response = requests.request("GET", url, headers=headers, params=querystring)
         details=response.json()
         print(details)
         return  render(request,"love.html",{"data":details})
    else:
        return render(request,"love.html")


        # payload = "{\"search\":\""+train_name+"\"}"
