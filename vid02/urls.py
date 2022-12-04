"""
Definition of urls for vid02.
"""

from django.urls import path
from datetime import datetime
from . import Vid02

app_name = "vid02"

urlpatterns = [
    path('vid02001/', Vid02.vid02001, name = 'vid02001' ),
    path('vid02001/code/', Vid02.vid02001_code, name = 'vid02001_code' ),
    path('vid02001/komarigoto_input/', Vid02.vid02001_komarigoto_input, name = 'vid02001_komarigoto_input' ),
#path('/vid02/<int:komarigoto_code>/vid02001', Vid02.vid02001_code, name = 'vid02001_code' )
]
