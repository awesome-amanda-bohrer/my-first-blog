from django.shortcuts import render

def my_second_bootstrap(request):
    return render(request, 'bootstrap/index.html')
#
#
#
def mycontactview(request):
    return render(request, 'bootstrap/contact.html')
#
#
#
def myportfolio1(request):
    return render(request, 'bootstrap/portfolio-1-col.html')
#
#
#
def myportfolio2(request):
    return render(request, 'bootstrap/portfolio-2-col.html')
#
#
#
def myportfolio3(request):
    return render(request, 'bootstrap/portfolio-3-col.html')
#
#
#
def myportfolio4(request):
    return render(request, 'bootstrap/portfolio-4-col.html')
#
#
#
def myportfolio(request):
    return render(request, 'bootstrap/portfolio-item.html')