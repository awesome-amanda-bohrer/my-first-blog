from django.shortcuts import render,render_to_response
from django.template import RequestContext
from models import InputForm,UploadModel,InputForm2,UploadModel2
from forms import UploadForm,UploadForm2
import os,glob

def my_fatigue(request):

    PlasticityIdentifier = 0.0
    CycleIdentifier      = 0.0
    DamageIdentifier     = 0.0
    form2 = 0.0
    newupload = 0.0
    formupload = 0.0
    FileName = 0.0
    if request.method == 'POST':
        form = InputForm(request.POST)
        PlasticityIdentifier    = request.POST.getlist('uniplasticity')
        CycleIdentifier         = request.POST.getlist('unicycle')
        DamageIdentifier        = request.POST.getlist('unidamage')

        try:
            PlasticityIdentifier    = str(PlasticityIdentifier[0])
        except:
            PlasticityIdentifier    = str(PlasticityIdentifier)
        try:
            CycleIdentifier         = str(CycleIdentifier[0])
        except:
            CycleIdentifier         = str(CycleIdentifier)
        try:
            DamageIdentifier        = str(DamageIdentifier[0])
        except:
            DamageIdentifier        = str(DamageIdentifier)

        try:
            formupload = UploadForm(request.POST, request.FILES)
            FileName   = request.FILES['upload']
            try:
                FileName   = str(FileName)
                os.remove('NumpySin/media/fatigue/' + FileName)
            except:
                FileName   = FileName
            if form.is_valid():
                form2 = form.save(commit=False)
                newupload = UploadModel(upload = request.FILES['upload'])
                try:
                    newupload.save()
                except:
                    newupload = newupload
        except:
            if form.is_valid():
                form2 = form.save(commit=False)

    else:
        form = InputForm()
        formupload = UploadForm()

    return render_to_response('fatigue/fatigue.html',
            {'PlasticityIdentifier': PlasticityIdentifier,
             'CycleIdentifier': CycleIdentifier,
             'DamageIdentifier': DamageIdentifier,
             'form': form,
             'newupload': newupload,
             'formupload': formupload,
             'FileName': FileName,
             }, context_instance=RequestContext(request))
#
def my_modelwizard(request):
    return render(request, 'fatigue/modelwizard.html')
#
def my_modelselection(request):
    return render(request, 'fatigue/modelselection.html')
#
#
#
def my_uniaxial(request):

    PlasticityIdentifier = 0.0
    CycleIdentifier      = 0.0
    DamageIdentifier     = 0.0
    form2 = 0.0
    newupload = 0.0
    formupload = 0.0
    FileName = 0.0
    if request.method == 'POST':
        form = InputForm(request.POST)
        PlasticityIdentifier    = request.POST.getlist('uniplasticity')
        CycleIdentifier         = request.POST.getlist('unicycle')
        DamageIdentifier        = request.POST.getlist('unidamage')

        try:
            PlasticityIdentifier    = str(PlasticityIdentifier[0])
        except:
            PlasticityIdentifier    = str(PlasticityIdentifier)
        try:
            CycleIdentifier         = str(CycleIdentifier[0])
        except:
            CycleIdentifier         = str(CycleIdentifier)
        try:
            DamageIdentifier        = str(DamageIdentifier[0])
        except:
            DamageIdentifier        = str(DamageIdentifier)

        try:
            formupload = UploadForm(request.POST, request.FILES)
            FileName   = request.FILES['upload']
            try:
                FileName   = str(FileName)
                os.remove('NumpySin/media/fatigue/' + FileName)
            except:
                FileName   = FileName
            if form.is_valid():
                form2 = form.save(commit=False)
                newupload = UploadModel(upload = request.FILES['upload'])
                try:
                    newupload.save()
                except:
                    newupload = newupload
        except:
            if form.is_valid():
                form2 = form.save(commit=False)

    else:
        form = InputForm()
        formupload = UploadForm()

    return render_to_response('fatigue/uniaxial.html',
            {'PlasticityIdentifier': PlasticityIdentifier,
             'CycleIdentifier': CycleIdentifier,
             'DamageIdentifier': DamageIdentifier,
             'form': form,
             'newupload': newupload,
             'formupload': formupload,
             'FileName': FileName,
             }, context_instance=RequestContext(request))
#

def my_uniplasticity(request):

    PlasticityIdentifier = 0.0
    CycleIdentifier      = 0.0
    DamageIdentifier     = 0.0
    form2 = 0.0
    newupload = 0.0
    formupload = 0.0
    FileName = 0.0
    if request.method == 'POST':
        form = InputForm(request.POST)
        PlasticityIdentifier    = request.POST.getlist('uniplasticity')
        CycleIdentifier         = request.POST.getlist('unicycle')
        DamageIdentifier        = request.POST.getlist('unidamage')

        try:
            PlasticityIdentifier    = str(PlasticityIdentifier[0])
        except:
            PlasticityIdentifier    = str(PlasticityIdentifier)
        try:
            CycleIdentifier         = str(CycleIdentifier[0])
        except:
            CycleIdentifier         = str(CycleIdentifier)
        try:
            DamageIdentifier        = str(DamageIdentifier[0])
        except:
            DamageIdentifier        = str(DamageIdentifier)

        try:
            formupload = UploadForm(request.POST, request.FILES)
            FileName   = request.FILES['upload']
            try:
                FileName   = str(FileName)
                os.remove('NumpySin/media/fatigue/' + FileName)
            except:
                FileName   = FileName
            if form.is_valid():
                form2 = form.save(commit=False)
                newupload = UploadModel(upload = request.FILES['upload'])
                try:
                    newupload.save()
                except:
                    newupload = newupload
        except:
            if form.is_valid():
                form2 = form.save(commit=False)

    else:
        form = InputForm()
        formupload = UploadForm()

    return render_to_response('fatigue/uniplasticity.html',
            {'PlasticityIdentifier': PlasticityIdentifier,
             'CycleIdentifier': CycleIdentifier,
             'DamageIdentifier': DamageIdentifier,
             'form': form,
             'newupload': newupload,
             'formupload': formupload,
             'FileName': FileName,
             }, context_instance=RequestContext(request))
#
def my_unicycle(request):

    PlasticityIdentifier = 0.0
    CycleIdentifier      = 0.0
    DamageIdentifier     = 0.0
    form2 = 0.0
    newupload = 0.0
    formupload = 0.0
    FileName = 0.0
    if request.method == 'POST':
        form = InputForm(request.POST)
        PlasticityIdentifier    = request.POST.getlist('uniplasticity')
        CycleIdentifier         = request.POST.getlist('unicycle')
        DamageIdentifier        = request.POST.getlist('unidamage')

        try:
            PlasticityIdentifier    = str(PlasticityIdentifier[0])
        except:
            PlasticityIdentifier    = str(PlasticityIdentifier)
        try:
            CycleIdentifier         = str(CycleIdentifier[0])
        except:
            CycleIdentifier         = str(CycleIdentifier)
        try:
            DamageIdentifier        = str(DamageIdentifier[0])
        except:
            DamageIdentifier        = str(DamageIdentifier)

        try:
            formupload = UploadForm(request.POST, request.FILES)
            FileName   = request.FILES['upload']
            try:
                FileName   = str(FileName)
                os.remove('NumpySin/media/fatigue/' + FileName)
            except:
                FileName   = FileName
            if form.is_valid():
                form2 = form.save(commit=False)
                newupload = UploadModel(upload = request.FILES['upload'])
                try:
                    newupload.save()
                except:
                    newupload = newupload
        except:
            if form.is_valid():
                form2 = form.save(commit=False)

    else:
        form = InputForm()
        formupload = UploadForm()


    return render_to_response('fatigue/unicycle.html',
            {'PlasticityIdentifier': PlasticityIdentifier,
             'CycleIdentifier': CycleIdentifier,
             'DamageIdentifier': DamageIdentifier,
             'form': form,
             'newupload': newupload,
             'formupload': formupload,
             'FileName': FileName,
             }, context_instance=RequestContext(request))
#
def my_unidamage(request):

    PlasticityIdentifier = 0.0
    CycleIdentifier      = 0.0
    DamageIdentifier     = 0.0
    form2 = 0.0
    newupload = 0.0
    formupload = 0.0
    FileName = 0.0
    if request.method == 'POST':
        form = InputForm(request.POST)
        PlasticityIdentifier    = request.POST.getlist('uniplasticity')
        CycleIdentifier         = request.POST.getlist('unicycle')
        DamageIdentifier        = request.POST.getlist('unidamage')

        try:
            PlasticityIdentifier    = str(PlasticityIdentifier[0])
        except:
            PlasticityIdentifier    = str(PlasticityIdentifier)
        try:
            CycleIdentifier         = str(CycleIdentifier[0])
        except:
            CycleIdentifier         = str(CycleIdentifier)
        try:
            DamageIdentifier        = str(DamageIdentifier[0])
        except:
            DamageIdentifier        = str(DamageIdentifier)

        try:
            formupload = UploadForm(request.POST, request.FILES)
            FileName   = request.FILES['upload']
            try:
                FileName   = str(FileName)
                os.remove('NumpySin/media/fatigue/' + FileName)
            except:
                FileName   = FileName
            if form.is_valid():
                form2 = form.save(commit=False)
                newupload = UploadModel(upload = request.FILES['upload'])
                try:
                    newupload.save()
                except:
                    newupload = newupload
        except:
            if form.is_valid():
                form2 = form.save(commit=False)

    else:
        form = InputForm()
        formupload = UploadForm()

    return render_to_response('fatigue/unidamage.html',
            {'PlasticityIdentifier': PlasticityIdentifier,
             'CycleIdentifier': CycleIdentifier,
             'DamageIdentifier': DamageIdentifier,
             'form': form,
             'newupload': newupload,
             'formupload': formupload,
             'FileName': FileName,
             }, context_instance=RequestContext(request))
#
def my_uniresults(request):

    PlasticityIdentifier = 0.0
    CycleIdentifier      = 0.0
    DamageIdentifier     = 0.0
    form2 = 0.0
    newupload = 0.0
    formupload = 0.0
    FileName = 0.0
    if request.method == 'POST':
        form = InputForm(request.POST)
        PlasticityIdentifier    = request.POST.getlist('uniplasticity')
        CycleIdentifier         = request.POST.getlist('unicycle')
        DamageIdentifier        = request.POST.getlist('unidamage')

        try:
            PlasticityIdentifier    = str(PlasticityIdentifier[0])
        except:
            PlasticityIdentifier    = str(PlasticityIdentifier)
        try:
            CycleIdentifier         = str(CycleIdentifier[0])
        except:
            CycleIdentifier         = str(CycleIdentifier)
        try:
            DamageIdentifier        = str(DamageIdentifier[0])
        except:
            DamageIdentifier        = str(DamageIdentifier)

        try:
            formupload = UploadForm(request.POST, request.FILES)
            FileName   = request.FILES['upload']
            try:
                FileName   = str(FileName)
                os.remove('NumpySin/media/fatigue/' + FileName)
            except:
                FileName   = FileName
            if form.is_valid():
                form2 = form.save(commit=False)
                newupload = UploadModel(upload = request.FILES['upload'])
                try:
                    newupload.save()
                except:
                    newupload = newupload
        except:
            if form.is_valid():
                form2 = form.save(commit=False)

    else:
        form = InputForm()
        formupload = UploadForm()

    return render_to_response('fatigue/uniresults.html',
            {'PlasticityIdentifier': PlasticityIdentifier,
             'CycleIdentifier': CycleIdentifier,
             'DamageIdentifier': DamageIdentifier,
             'form': form,
             'newupload': newupload,
             'formupload': formupload,
             'FileName': FileName,
             }, context_instance=RequestContext(request))
#
#
#
def my_multiaxial(request):

    PlasticityIdentifier = 0.0
    CycleIdentifier      = 0.0
    DamageIdentifier     = 0.0
    form2 = 0.0
    newupload = 0.0
    formupload = 0.0
    FileName = 0.0
    if request.method == 'POST':
        form = InputForm2(request.POST)
        PlasticityIdentifier    = request.POST.getlist('multiplasticity')
        CycleIdentifier         = request.POST.getlist('multicycle')
        DamageIdentifier        = request.POST.getlist('multidamage')

        try:
            PlasticityIdentifier    = str(PlasticityIdentifier[0])
        except:
            PlasticityIdentifier    = str(PlasticityIdentifier)
        try:
            CycleIdentifier         = str(CycleIdentifier[0])
        except:
            CycleIdentifier         = str(CycleIdentifier)
        try:
            DamageIdentifier        = str(DamageIdentifier[0])
        except:
            DamageIdentifier        = str(DamageIdentifier)

        try:
            formupload = UploadForm2(request.POST, request.FILES)
            FileName   = request.FILES['upload2']
            try:
                FileName   = str(FileName)
                os.remove('NumpySin/media/fatigue/' + FileName)
            except:
                FileName   = FileName
            if form.is_valid():
                form2 = form.save(commit=False)
                newupload = UploadModel2(upload2 = request.FILES['upload2'])
                try:
                    newupload.save()
                except:
                    newupload = newupload
        except:
            if form.is_valid():
                form2 = form.save(commit=False)

    else:
        form = InputForm2()
        formupload = UploadForm2()

    return render_to_response('fatigue/multiaxial.html',
            {'PlasticityIdentifier': PlasticityIdentifier,
             'CycleIdentifier': CycleIdentifier,
             'DamageIdentifier': DamageIdentifier,
             'form': form,
             'newupload': newupload,
             'formupload': formupload,
             'FileName': FileName,
             }, context_instance=RequestContext(request))
#

def my_multiplasticity(request):

    PlasticityIdentifier = 0.0
    CycleIdentifier      = 0.0
    DamageIdentifier     = 0.0
    form2 = 0.0
    newupload = 0.0
    formupload = 0.0
    FileName = 0.0
    if request.method == 'POST':
        form = InputForm2(request.POST)
        PlasticityIdentifier    = request.POST.getlist('multiplasticity')
        CycleIdentifier         = request.POST.getlist('multicycle')
        DamageIdentifier        = request.POST.getlist('multidamage')

        try:
            PlasticityIdentifier    = str(PlasticityIdentifier[0])
        except:
            PlasticityIdentifier    = str(PlasticityIdentifier)
        try:
            CycleIdentifier         = str(CycleIdentifier[0])
        except:
            CycleIdentifier         = str(CycleIdentifier)
        try:
            DamageIdentifier        = str(DamageIdentifier[0])
        except:
            DamageIdentifier        = str(DamageIdentifier)

        try:
            formupload = UploadForm2(request.POST, request.FILES)
            FileName   = request.FILES['upload2']
            try:
                FileName   = str(FileName)
                os.remove('NumpySin/media/fatigue/' + FileName)
            except:
                FileName   = FileName
            if form.is_valid():
                form2 = form.save(commit=False)
                newupload = UploadModel2(upload2 = request.FILES['upload2'])
                try:
                    newupload.save()
                except:
                    newupload = newupload
        except:
            if form.is_valid():
                form2 = form.save(commit=False)

    else:
        form = InputForm2()
        formupload = UploadForm2()

    return render_to_response('fatigue/multiplasticity.html',
            {'PlasticityIdentifier': PlasticityIdentifier,
             'CycleIdentifier': CycleIdentifier,
             'DamageIdentifier': DamageIdentifier,
             'form': form,
             'newupload': newupload,
             'formupload': formupload,
             'FileName': FileName,
             }, context_instance=RequestContext(request))
#
def my_multicycle(request):

    PlasticityIdentifier = 0.0
    CycleIdentifier      = 0.0
    DamageIdentifier     = 0.0
    form2 = 0.0
    newupload = 0.0
    formupload = 0.0
    FileName = 0.0
    if request.method == 'POST':
        form = InputForm2(request.POST)
        PlasticityIdentifier    = request.POST.getlist('multiplasticity')
        CycleIdentifier         = request.POST.getlist('multicycle')
        DamageIdentifier        = request.POST.getlist('multidamage')

        try:
            PlasticityIdentifier    = str(PlasticityIdentifier[0])
        except:
            PlasticityIdentifier    = str(PlasticityIdentifier)
        try:
            CycleIdentifier         = str(CycleIdentifier[0])
        except:
            CycleIdentifier         = str(CycleIdentifier)
        try:
            DamageIdentifier        = str(DamageIdentifier[0])
        except:
            DamageIdentifier        = str(DamageIdentifier)

        try:
            formupload = UploadForm2(request.POST, request.FILES)
            FileName   = request.FILES['upload2']
            try:
                FileName   = str(FileName)
                os.remove('NumpySin/media/fatigue/' + FileName)
            except:
                FileName   = FileName
            if form.is_valid():
                form2 = form.save(commit=False)
                newupload = UploadModel2(upload2 = request.FILES['upload2'])
                try:
                    newupload.save()
                except:
                    newupload = newupload
        except:
            if form.is_valid():
                form2 = form.save(commit=False)

    else:
        form = InputForm2()
        formupload = UploadForm2()


    return render_to_response('fatigue/multicycle.html',
            {'PlasticityIdentifier': PlasticityIdentifier,
             'CycleIdentifier': CycleIdentifier,
             'DamageIdentifier': DamageIdentifier,
             'form': form,
             'newupload': newupload,
             'formupload': formupload,
             'FileName': FileName,
             }, context_instance=RequestContext(request))
#
def my_multidamage(request):

    PlasticityIdentifier = 0.0
    CycleIdentifier      = 0.0
    DamageIdentifier     = 0.0
    form2 = 0.0
    newupload = 0.0
    formupload = 0.0
    FileName = 0.0
    if request.method == 'POST':
        form = InputForm2(request.POST)
        PlasticityIdentifier    = request.POST.getlist('multiplasticity')
        CycleIdentifier         = request.POST.getlist('multicycle')
        DamageIdentifier        = request.POST.getlist('multidamage')

        try:
            PlasticityIdentifier    = str(PlasticityIdentifier[0])
        except:
            PlasticityIdentifier    = str(PlasticityIdentifier)
        try:
            CycleIdentifier         = str(CycleIdentifier[0])
        except:
            CycleIdentifier         = str(CycleIdentifier)
        try:
            DamageIdentifier        = str(DamageIdentifier[0])
        except:
            DamageIdentifier        = str(DamageIdentifier)

        try:
            formupload = UploadForm2(request.POST, request.FILES)
            FileName   = request.FILES['upload2']
            try:
                FileName   = str(FileName)
                os.remove('NumpySin/media/fatigue/' + FileName)
            except:
                FileName   = FileName
            if form.is_valid():
                form2 = form.save(commit=False)
                newupload = UploadModel2(upload2 = request.FILES['upload2'])
                try:
                    newupload.save()
                except:
                    newupload = newupload
        except:
            if form.is_valid():
                form2 = form.save(commit=False)

    else:
        form = InputForm2()
        formupload = UploadForm2()

    return render_to_response('fatigue/multidamage.html',
            {'PlasticityIdentifier': PlasticityIdentifier,
             'CycleIdentifier': CycleIdentifier,
             'DamageIdentifier': DamageIdentifier,
             'form': form,
             'newupload': newupload,
             'formupload': formupload,
             'FileName': FileName,
             }, context_instance=RequestContext(request))
#
def my_multiresults(request):

    PlasticityIdentifier = 0.0
    CycleIdentifier      = 0.0
    DamageIdentifier     = 0.0
    form2 = 0.0
    newupload = 0.0
    formupload = 0.0
    FileName = 0.0
    if request.method == 'POST':
        form = InputForm2(request.POST)
        PlasticityIdentifier    = request.POST.getlist('multiplasticity')
        CycleIdentifier         = request.POST.getlist('multicycle')
        DamageIdentifier        = request.POST.getlist('multidamage')

        try:
            PlasticityIdentifier    = str(PlasticityIdentifier[0])
        except:
            PlasticityIdentifier    = str(PlasticityIdentifier)
        try:
            CycleIdentifier         = str(CycleIdentifier[0])
        except:
            CycleIdentifier         = str(CycleIdentifier)
        try:
            DamageIdentifier        = str(DamageIdentifier[0])
        except:
            DamageIdentifier        = str(DamageIdentifier)

        try:
            formupload = UploadForm2(request.POST, request.FILES)
            FileName   = request.FILES['upload2']
            try:
                FileName   = str(FileName)
                os.remove('NumpySin/media/fatigue/' + FileName)
            except:
                FileName   = FileName
            if form.is_valid():
                form2 = form.save(commit=False)
                newupload = UploadModel2(upload2 = request.FILES['upload2'])
                try:
                    newupload.save()
                except:
                    newupload = newupload
        except:
            if form.is_valid():
                form2 = form.save(commit=False)

    else:
        form = InputForm2()
        formupload = UploadForm2()

    return render_to_response('fatigue/multiresults.html',
            {'PlasticityIdentifier': PlasticityIdentifier,
             'CycleIdentifier': CycleIdentifier,
             'DamageIdentifier': DamageIdentifier,
             'form': form,
             'newupload': newupload,
             'formupload': formupload,
             'FileName': FileName,
             }, context_instance=RequestContext(request))
#
#
#
def my_user(request):
    return render(request, 'fatigue/user.html')
#
#
#
def my_settings(request):
    return render(request, 'fatigue/settings.html')
#
#
#
def my_software(request):
    return render(request, 'fatigue/software.html')
#
#
#




'''
def my_template2(request):
    return render(request, 'fatigue/template.html')
#
#
#
def my_buttons2(request):
    return render(request, 'fatigue/buttons.html')
#
#
#
def my_calendar2(request):
    return render(request, 'fatigue/calendar.html')
#
#
#
def my_charts2(request):
    return render(request, 'fatigue/charts.html')
#
#
#
def my_datatable2(request):
    return render(request, 'fatigue/datatable.html')
#
#
#
def my_elements2(request):
    return render(request, 'fatigue/elements.html')
#
#
#
def my_extended2(request):
    return render(request, 'fatigue/extended.html')
#
#
#
def my_fullscreen2(request):
    return render(request, 'fatigue/fullscreen.html')
#
#
#
def my_google2(request):
    return render(request, 'fatigue/google.html')
#
#
#
def my_grid2(request):
    return render(request, 'fatigue/grid.html')
#
#
#
def my_htmltutorial2(request):
    return render(request, 'fatigue/html-tutorial.html')
#
#
#
def my_icons2(request):
    return render(request, 'fatigue/icons.html')
#
#
#
def my_lock2(request):
    return render(request, 'fatigue/lock.html')
#
#
#
def my_login2(request):
    return render(request, 'fatigue/login.html')
#
#
#
def my_notifications2(request):
    return render(request, 'fatigue/notifications.html')
#
#
#
def my_panels2(request):
    return render(request, 'fatigue/panels.html')
#
#
#
def my_plainpage2(request):
    return render(request, 'fatigue/plain-page.html')
#
#
#
def my_register2(request):
    return render(request, 'fatigue/register.html')
#
#
#
def my_sweetalert2(request):
    return render(request, 'fatigue/sweet-alert.html')
#
#
#
def my_uniaxial(request):
    return render(request, 'fatigue/uniaxial.html')
#
#
#
def my_multiaxial(request):
    return render(request, 'fatigue/multiaxial.html')
#
#
#
def my_regular3(request):
    return render(request, 'fatigue/regular.html')
#
#
#
def my_typography2(request):
    return render(request, 'fatigue/typography.html')
#
#
#
def my_user2(request):
    return render(request, 'fatigue/user.html')
#
#
#
def my_validation2(request):
    return render(request, 'fatigue/validation.html')
#
#
#
def my_vector2(request):
    return render(request, 'fatigue/vector.html')
#
#
#
def my_wizard2(request):
    return render(request, 'fatigue/wizard.html')
#
#
#
def my_regular4(request):
    return render(request, 'fatigue/regulartable.html')
#
#
#
'''