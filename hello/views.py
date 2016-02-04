from django.shortcuts import render

def my_dashboard(request):
    return render(request, 'hello/dashboard.html')
#
#
#
def template(request):
    return render(request, 'hello/template.html')
#
#
#
def icons(request):
    return render(request, 'hello/icons.html')
#
#
#
def maps(request):
    return render(request, 'hello/maps.html')
#
#
#
def notifications(request):
    return render(request, 'hello/notifications.html')
#
#
#
def table(request):
    return render(request, 'hello/table.html')
#
#
#
def typography(request):
    return render(request, 'hello/typography.html')
#
#
#
def upgrade(request):
    return render(request, 'hello/upgrade.html')
#
#
#
def user(request):
    return render(request, 'hello/user.html')
#
#
#