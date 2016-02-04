from django.shortcuts import render

def my_dashboard(request):
    return render(request, 'dash/index.html')
#
#
#