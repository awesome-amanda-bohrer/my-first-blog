from django.shortcuts import render

def my_second_bootstrap(request):
    return render(request, 'bootstrap/index2.html')
