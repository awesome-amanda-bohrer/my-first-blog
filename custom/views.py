from django.shortcuts import render

def my_blankpage(request):
    return render(request, 'custom/blank-page.html')
#
#
#