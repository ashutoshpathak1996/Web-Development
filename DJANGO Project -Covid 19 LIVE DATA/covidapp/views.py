from django.shortcuts import render
import requests
import json
url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
	"X-RapidAPI-Key": "6591c6d84bmsha8a3c80fe5b2f9bp1a112cjsndaac827017a0",
	"X-RapidAPI-Host": "covid-193.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers).json()

# Create your views here.
def helloworldview(request):
    noofresults = int(response['results'])
    mylist = []
    for x in range(0, noofresults):
        mylist.append(response['response'][x]['country'])
        mylist.sort()
    if request.method=="POST":
        selectedcountry = request.POST['selectedcountry']
        for x in range(0,noofresults):
            if selectedcountry==response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total) - int(active) - int(recovered)
        context = {'selectedcountry' : selectedcountry, 'mylist' : mylist, 'new' : new, 'active' : active, 'critical' : critical, 'recovered' : recovered, 'total' : total, 'deaths' : deaths}
        return render(request, 'helloworld.html', context)
    context={'mylist' : mylist}
    return render(request,'helloworld.html',context)