from django.views.generic import ListView
from elections.models import ElectionRequirement, CarouselImage
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import Voter
from django.contrib.auth import authenticate, login

class RequirementsListView(ListView):
    model = ElectionRequirement
    template_name = 'home.html'
    context_object_name = 'requirements'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousel_images'] = CarouselImage.objects.all()
        return context



def register(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        username = request.POST['username']
        email = request.POST['email']
        residence = request.POST['residence']
        age = request.POST['age']
        dob = request.POST['dob']
        phone = request.POST['phone']
        password = request.POST['password']

        # Create a new voter instance
        voter = Voter(
            full_name=full_name,
            username=username,
            email=email,
            residence=residence,
            age=age,
            dob=dob,
            phone=phone,
            password=password 
        )
        
        voter.save()
        
        messages.success(request, 'Registration successful! You can now log in.')
        return redirect('login')  # Redirect to login page after successful registration

    return render(request, 'register.html')

def voter_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        voter = authenticate(request, username=username, password=password)
        
        if voter is not None:
            print("this is the intro")
            login(request, voter)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')

def dashboard(request):
    response = requests.get("https://en.wikipedia.org/api/rest_v1/page/summary/Past_elections")
    past_elections_data = response.json() if response.status_code == 200 else {}

    user_residence = None
    if request.user.is_authenticated:
        try:
            voter = Voter.objects.get(username=request.user.username)
            user_residence = voter.residence
        except Voter.DoesNotExist:
            user_residence = None

    # Fetch election requirements from the database
    requirements = Election.objects.filter(status='COMPLETED')

    context = {
        'past_elections': past_elections_data,
        'requirements': requirements,
        'user_residence': user_residence,
    }
    
    return render(request, 'dashboard.html', context)