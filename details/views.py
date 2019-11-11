from django.shortcuts import render
from django.shortcuts import get_list_or_404
from entry.models import Stud_PD,Stud_Admn

def stud_list(request):
    stud_pds = Stud_PD.objects.all()   
    return render(request, 'details/stud_list.html', {'stud_pds':stud_pds})

def stud_details(request,usn):
    #return HttpResponse(usn)
    stud_pd = Stud_PD.objects.get(USN=usn)
    stud_ad = Stud_Admn.objects.get(Sid=stud_pd.Sid)
    return render(request, 'details/stud_details.html', {'stud_pd':stud_pd, 'stud_ad':stud_ad})