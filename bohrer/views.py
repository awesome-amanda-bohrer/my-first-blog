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
def myselectionview(request):
    return render(request, 'bohrer/selection.html')
#
#
#
def myinputview(request):
    return render(request, 'bohrer/input.html')
#
#
#
def mysleeveview(request):
    return render(request, 'bohrer/sleeve.html')
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
