from django.shortcuts import render


def test(request):
    return render(request,'appenv/appenv.html')

def test1(request):
        return render(request, 'appenv/firststep.html')
