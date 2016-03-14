from django.shortcuts import render

def my_blankpage(request):
    return render(request, 'custom/blank-page.html')
#
#
#
def my_index(request):
    return render(request, 'custom/index.html')
#
#
#
def my_indexrtl(request):
    return render(request, 'custom/index-rtl.html')
#
#
#