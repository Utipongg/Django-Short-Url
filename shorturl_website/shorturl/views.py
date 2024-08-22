from django.shortcuts import redirect, render
from .models import UrlDb
from django.http import HttpResponseNotFound

def create_url(request):
    if request.method == 'POST':
        longurl = request.POST.get('long_url')
        if longurl:
            urlchk = UrlDb.objects.filter(longurl=longurl).exists()
            if not urlchk:
                new_url = UrlDb.objects.create(longurl=longurl)
            else:
                new_url = UrlDb.objects.get(longurl=longurl)
            
            request.session['code_url'] = new_url.code
            request.session['localurl'] = request.build_absolute_uri('/')
            return redirect('/create')
        else:
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')

def createpage(request):
    code_url = request.session.get('code_url')
    localurl = request.session.get('localurl')
    return render(request, 'create.html', {'code_url': code_url, 'localurl': request.build_absolute_uri('/')})


def redirect_url(request, code):
    try:
        url = UrlDb.objects.get(code=code)
        return redirect(url.longurl)
    except UrlDb.DoesNotExist:
        return render(request, '404.html')