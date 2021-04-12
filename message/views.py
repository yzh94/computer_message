from django.shortcuts import render

# Create your views here.
def index(request):

    hostname=request.META['COMPUTERNAME']
    ipaddr = request.META['REMOTE_ADDR']
    os = request.META['OS']

    return render(request,'index.html',{'hostname':hostname,'ipaddr':ipaddr,'os':os})
