from django.shortcuts import render

# Create your views here.
def recipe_page(request):
    context = {'page_title': 'Recipe Page'}
    return render(request, 'all_recipes.html', context)