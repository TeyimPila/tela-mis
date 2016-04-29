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
    bens = Beneficiary.objects.all();
    number_of_beneficiaries = bens.count()
    number_in_school = Beneficiary.objects.filter(is_in_school='True').count()
    number_out_of_school = number_of_beneficiaries - number_in_school
    ordered = Beneficiary.objects.order_by('age')
    youngest_beneficiary = ordered[0]
    oldest_beneficiary = ordered[number_of_beneficiaries-1]
    return render(request,
                  'account/beneficiary_list.html',
                   {'bens':bens,'number_in_school': number_in_school,
                    'number_of_beneficiaries': number_of_beneficiaries,
                   'number_out_of_school': number_out_of_school,
                   'youngest_beneficiary': youngest_beneficiary,
                   'oldest_beneficiary': oldest_beneficiary,});

@login_required
def tutor_list(request):
    tuts = Tutor.objects.all()
    num_of_tutors = tuts.count()
    freshmen = Tutor.objects.filter(classification='FR').count()
    sophmores = Tutor.objects.filter(classification='SO').count()
    juniors = Tutor.objects.filter(classification='JR').count()
    seniors = Tutor.objects.filter(classification='SR').count()
    graduates = Tutor.objects.filter(classification='GR').count()
    return render(request, 'account/tutor_list.html',
           {'tuts':tuts, 'num_of_tutors': num_of_tutors, 'freshmen': freshmen,
            'sophmores': sophmores, 'juniors': juniors, 'seniors': seniors,
            'graduates': graduates,});

@login_required
def facilitator_list(request):
    facs = Facilitator.objects.all()
    number_of_facilitators = facs.count()
    males = Facilitator.objects.filter(gender='male').count()
    females = Facilitator.objects.filter(gender='female').count()
    return render(request, 'account/facilitator_list.html',
           {'facs':facs, 'number_of_facilitators': number_of_facilitators,
            'males': males, 'females': females,});
@login_required
def enumerator_list(request):
    ens = Enumerator.objects.all()
    number_of_enumerators = ens.count()
    males = Enumerator.objects.filter(gender='male').count()
    females = Enumerator.objects.filter(gender='female').count()
    return render(request, 'account/enumerator_list.html',
           {'ens':ens, 'number_of_enumerators': number_of_enumerators, 'males': males,
            'females': females});

@login_required
def center_list(request):
    cens = Center.objects.all()
    number_of_centers = cens.count()
    ordered_centers = Center.objects.order_by('-group_size')
    biggest_center = ordered_centers[0]
    smallest_center = ordered_centers[number_of_centers-1]
    max_size = biggest_center.group_size
    return render(request, 'account/center_list.html',
           {'cens':cens, 'number_of_centers': number_of_centers, 'max_size': max_size,
            'biggest_center': biggest_center, 'smallest_center': smallest_center});

@login_required
def lga_list(request):
    lgas = LocalGovArea.objects.all()
    lga_number = lgas.count()
    return render(request, 'account/lga_list.html',
           {'lgas':lgas, 'lga_number': lga_number});

@login_required
def neighborhood_list(request):
    neighs = Neighborhood.objects.all()
    neighborhoods_number = neighs.count()
    return render(request, 'account/neigh_list.html',
           {'neighs':neighs,
            'neighborhoods_number': neighborhoods_number, });

@login_required
def venue_list(request):
    vens = Venue.objects.all()
    venues_number = vens.count()
    return render(request, 'account/venue_list.html',
           {'vens':vens, 'venues_number': venues_number, });

@login_required
def tutorialType_list(request):
    tut_types = TutorialType.objects.all()
    tutorial_type_number = tut_types.count()
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

def index(request):
    return render(request,
                  'account/index.html',{

                  } )

#add pagination
# def entry_index(request, template='account/beneficiary_list.html'):
#     context = {
#         'number_of_beneficiaries': Beneficiary.objects.all(),
#     }
#     return render_to_response(
#         template, context, context_instance=RequestContext(request))