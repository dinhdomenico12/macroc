from django.shortcuts import render

# Create your views here.
def index(request,):
  # database stuff 0-
  return render(request, 'macro/index.html')
