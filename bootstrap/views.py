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
def portfolio1(request):
    return render(request, 'bootstrap/portfolio-1-col.html')
#
#
#
def portfolio2(request):
    return render(request, 'bootstrap/portfolio-2-col.html')
#
#
#
def portfolio3(request):
    return render(request, 'bootstrap/portfolio-3-col.html')
#
#
#
def portfolio4(request):
    return render(request, 'bootstrap/portfolio-4-col.html')
#
#
#
def portfolio(request):
    return render(request, 'bootstrap/portfolio-item.html')