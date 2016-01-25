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
def myblog1(request):
    return render(request, 'bootstrap/blog-home-1.html')
#
#
#
def my404(request):
    return render(request, 'bootstrap/404.html')