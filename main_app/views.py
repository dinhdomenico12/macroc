from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from main_app.models import Goals, Macros 
from django.views.generic.edit import CreateView, UpdateView
# Create your views here.

def index(request):
      macros = Macros.objects.all()
      goals = Goals.objects.filter(user=request.user)
      return render(request, 'macro/index.html', {'macros': macros,'goals':goals})

def home(request):
  return render(request, 'home.html')


class Macro_create(CreateView):
      model = Macros
      fields = '__all__'
      success_url = '/meals/'

class Goals_create(CreateView):
      model = Goals
      fields = '__all__'
      success_url = '/meals/'



class Macroupdate(UpdateView):
    model = Macros
    fields = '__all__'
    success_url = '/meals/' 

def macro_delete(request, macro_id):
    Macros.objects.filter(id=macro_id).delete()
    return redirect('/meals/')

# sign up form

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)