from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from main_app.models import Goals, Macros
from django.views.generic.edit import CreateView, UpdateView
# Create your views here.
@login_required
def index(request):
      macros = Macros.objects.filter(user=request.user)
      goals = Goals.objects.filter(user=request.user)
      count = Macros.objects.values('calories', 'protein','carbohydrates','fats').filter(user=request.user)
      total = [
            {"calories":0},
            {"protein":0},
            {"carbohydrates":0},
            {"fats":0},]
      calories = 0
      protein = 0
      carbohydrates = 0
      fats = 0
      for c in count:
            calories += c['calories']
            protein += c['protein']
            carbohydrates += c['carbohydrates']
            fats += c['fats']
      total[0] =  calories
      total[1] =  protein
      total[2] =  carbohydrates
      total[3] =  fats
      print(total[0])
      return render(request, 'macro/index.html', {'macros': macros,'goals':goals,'total':total})
@login_required
def home(request):
  return render(request, 'home.html')
class Macro_create(LoginRequiredMixin,CreateView):
      model = Macros
      fields = ['name','calories', 'protein', 'carbohydrates', 'fats']
      success_url = '/meals/'
      def form_valid(self, form):
            form.instance.user = self.request.user
            return super().form_valid(form)
class Goals_create(LoginRequiredMixin,CreateView):
      model = Goals
      fields = ['calories', 'protein', 'carbohydrates', 'fats']
      success_url = '/meals/'
      def form_valid(self, form):
            form.instance.user = self.request.user
            return super().form_valid(form)
class Macroupdate(LoginRequiredMixin,UpdateView):
      model = Macros
      fields = ['name', 'calories','protein','carbohydrates','fats']
      success_url = '/meals/'
@login_required
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