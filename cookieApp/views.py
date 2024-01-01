from django.shortcuts import render
from datetime import timedelta,datetime
from django.http import HttpResponse

# Create your views here.
def SetCookie(request):
    response= render(request,'set_cookie.html')
    response.set_cookie('name', 'Kopiko' ,expires= datetime.utcnow()+ timedelta(seconds=10))
    return response

def GetCookie(request):
    name= request.COOKIES.get('name')
    print(name)
    return render(request, 'get_cookie.html', {'name': name} )

def DeleteCookie(request):
    response= render(request, 'del_cookie.html')
    response.delete_cookie('name')
    return response


def SetSession(request):
    data={
        'name': 'Tora Bika',
        'Flavor': 'Coffee',
    }
    request.session.update(data)
    return render(request, 'set_cookie.html', {'data': data})


def GetSession1(request):
    title= request.session.get('name', 'guest') #kono name na thakle by default guest dekhabe
    return render(request, 'get_cookie.html', {'title': title})


def GetSession(request):
    if 'name' in request.session:
        title= request.session.get('name', 'guest') #kono name na thakle by default guest dekhabe
        request.sesssion.modified= True #eta korle each reload e time reset hobe
        return render(request, 'get_cookie.html', {'title': title})
    
    else:
        return HttpResponse('Your session has been expired')
        

def del_session(request):
    request.session.flush()
    return render(request,'del_cookie.html')