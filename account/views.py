from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from tela.models import Beneficiary, LocalGovArea, Neighborhood, Venue, TutorialType, Facilitator, Center, Equipment, Tutor, Enumerator,PreAssessment, PostAssessment;
@login_required
def dashboard(request):
    test = Beneficiary.objects.all();
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard',});


#create views for the model base pages

# Create your views here.
@login_required
def beneficiary_list(request):
    ben = Beneficiary.objects.all();
    return render(request,
                  'account/beneficiary_list.html',
                   {'ben':ben,});

@login_required
def tutor_list(request):
    tuts = Tutor.objects.all()
    return render(request, 'account/tutor_list.html',
           {'tuts':tuts,});

@login_required
def facilitator_list(request):
    facs = Facilitator.objects.all()
    return render(request, 'account/facilitator_list.html',
           {'facs':facs});
@login_required
def enumerator_list(request):
    ens = Enumerator.objects.all()
    return render(request, 'account/enumerator_list.html',
           {'ens':ens});

@login_required
def center_list(request):
    cens = Center.objects.all()
    return render(request, 'account/center_list.html',
           {'cens':cens});

@login_required
def lga_list(request):
    lgas = LocalGovArea.objects.all()
    return render(request, 'account/lga_list.html',
           {'lgas':lgas});

@login_required
# def neighborhood_list(request):
#     neighs = Neighborhood.objects.all()
#     return render(request, 'account/neigh_list.html',
#            {'neighs':neighs});

@login_required
def venue_list(request):
    vens = Venue.objects.all()
    return render(request, 'account/venue_list.html',
           {'vens':vens});

@login_required
def tutorialType_list(request):
    tut_types = TutorialType.objects.all()
    return render(request, 'account/tutType_list.html',
           {'tut_types':tut_types});

@login_required
def equipment_list(request):
    eqps = Equipment.objects.all()
    return render(request, 'account/equipment_list.html',
           {'eqps': eqps})

#create details views
@login_required
def beneficiary_detail(request, id):
    ben = get_object_or_404(Beneficiary, id=id)
    return render(request,
                  'account/beneficiary_detail.html',
                  {'ben':ben});