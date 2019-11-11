from django.conf.urls import url
from . import views

app_name = 'details'

urlpatterns = [   
    url(r'^$',views.stud_list, name="list"),
    url(r'^(?P<usn>[\w]+)/$',views.stud_details, name="details"),
]
