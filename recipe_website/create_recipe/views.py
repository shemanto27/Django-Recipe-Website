from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
# Create your views here.


@login_required(login_url='/login')
def create_recipe_page(request):
    context = {'page_title': 'Create Recipe'}
    if request.method == 'POST':
        data = request.POST

        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        Create_Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_image = recipe_image,
        )
        messages.info(request, 'Recipe Published!')
        return redirect('/create-recipe')
    return render(request, 'create_recipe.html', context)
