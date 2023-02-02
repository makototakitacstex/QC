
# Commit and push from QC_CSTex Github Desktop Cloned.

from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.urls import path
from django.core import serializers

from .models import Komarigotolist
from .models import Eikyo1
from .models import Eikyo2
from .models import Genin1
from .models import Genin2
from .models import KomarigotoInput

def vid02001(request):
    template = loader.get_template( 'vid02/vid02001.html')

    komarigotolist = Komarigotolist.objects.all()

    context = {
        'komarigotolist': komarigotolist
        }
    return HttpResponse(template.render( context, request ))

def back():
    return "back"

def forward():
    return "forward"

def save(request):

    komarigoto = request.POST['komarigoto']

    eikyo1 = request.POST['eikyo1']
    eikyo2 = request.POST['eikyo2']

    genin1 = request.POST['genin1']
    genin2 = request.POST['genin2']

    komarigotoInput = KomarigotoInput()
    komarigotoInput.komarigoto = komarigoto

    komarigotoInput.eikyo1_code = eikyo1
    komarigotoInput.eikyo2_code = eikyo2

    komarigotoInput.genin1_code = genin1
    komarigotoInput.genin2_code = genin2



    return "save"

def default():
    return "default"

def vid02001_komarigoto_input(request):

    btn_selected = request.POST['btn_selected']

    if btn_selected == '保存':
        save(request)

    elif btn_selected == '戻る':
        back()

    else:
        default()

    return



def vid02001_code(request):
#    template = loader.get_template( 'vid02/vid02001.html')

    komarigoto_code = request.POST['komarigoto_code']

#    komarigotolist = Komarigotolist.objects.all()

#    komarigotolist = serializers.serialize("json", Komarigotolist.objects.all())

    komarigoto = Komarigotolist.objects.get(pk=komarigoto_code)






    eikyo1 = Eikyo1.objects.get(pk= komarigoto_code )
    eikyo2 = Eikyo2.objects.get(pk= komarigoto_code )

    genin1 = Genin1.objects.get(pk= komarigoto_code )
    genin2 = Genin2.objects.get(pk= komarigoto_code )

    context = {
#        'komarigotolist': komarigotolist,
        'komarigoto': f"'{komarigoto}'",
        'eikyo1': f"'{eikyo1}'",
        'eikyo2': f"'{eikyo2}'",
        'genin1': f"'{genin1}'",
        'genin2': f"'{genin2}'",
        }

    return JsonResponse( context )
