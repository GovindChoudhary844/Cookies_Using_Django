from django.shortcuts import render


def Set(request):
    response = render(request, 'set.html')
    response.set_cookie("Name", "Ducat")
    return response


def Get(request):
    name = request.COOKIES.get('Name')
    return render(request, 'get.html', {'name': name})


def Del(request):
    response = render(request, 'del.html')
    response.delete_cookie("Name")
    return response
    
