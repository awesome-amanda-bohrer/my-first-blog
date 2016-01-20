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