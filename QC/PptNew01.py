from django.http import HttpResponse
from django.template import loader

from QC.models import Komarigotolist

def index(request):
    template = loader.get_template( 'QC/PptNew/PptNew01.html')

    komarigotolist = Komarigotolist.objects.all()

    context = {
        'komarigotolist': komarigotolist
        }
    return HttpResponse(template.render( context, request ))



