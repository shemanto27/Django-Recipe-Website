from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login')
def recipe_page(request):
    context = {'page_title': 'Recipe Page'}
    return render(request, 'all_recipes.html', context)