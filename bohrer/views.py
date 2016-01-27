from django.shortcuts import render

def my_third_bootstrap(request):
    return render(request, 'bohrer/index.html')
#
#
#
def mychartsview(request):
    return render(request, 'bohrer/charts.html')
#
#
#
def myblankpagesview(request):
    return render(request, 'bohrer/blank-page.html')
#
#
#
def myelementsview(request):
    return render(request, 'bohrer/bootstrap-elements.html')
#
#
#
def mygridview(request):
    return render(request, 'bohrer/bootstrap-grid.html')
#
#
#
def myformsview(request):
    return render(request, 'bohrer/forms.html')
#
#
#
def myrtlview(request):
    return render(request, 'bohrer/index-rtl.html')
#
#
#
def mytablesview(request):
    return render(request, 'bohrer/tables.html')