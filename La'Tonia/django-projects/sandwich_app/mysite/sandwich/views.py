from django.shortcuts import render
from django.http import Http404
import random

# define ingredients outside of view functions
# edited and added to for practice 
ingredients = {
    'meats':  [' Turkey Loins', ' Venison ', ' Tempeh '],
    'cheeses': ['feta', 'provolone', 'gruyere'],
    'toppings': ['spinach leaves', 'spicy jalapenos', 'black olives'],
    'breads': ['sourdough', 'honeyseed', 'pumpernick'],
    'sides': ['wedges', 'celery dips', 'bornbread'],
    'drinks': ['sup juice'],
    'sweets': ['cakey pie', 'gourmet maple strips']
}

# assign full menu to empty list - append iterations of sandwiches
full_menu = []

def sandwich(request):
    if request.method == 'GET':
        return render(request = request, 
                      template_name = 'sandwich.html', 
                      context = {'ingredients': ingredients.keys()})

def ingredients_list(request, ingredient_type):
    if request.method == 'GET':
        # if ingredient type doesn't exist, raise Http404
        if ingredient_type not in ingredients:
                    raise Http404(f'No such ingredient: {ingredient_type}')

        return render(request = request, template_name = 'ingredients_list.html', 
                      context={ 'ingredients': ingredients[ingredient_type],
                                'ingredient_type': ingredient_type })

def sandwich_generator(request):
    if request.method == 'GET':
        """ Build a random cold-cut sandwich """
        selected_meat = random.choice(ingredients['meats'])
        selected_cheese = random.choice(ingredients['cheeses'])
        selected_topping = random.choice(ingredients['toppings'])

        sandwich = f'{selected_meat} & {selected_cheese} with {selected_topping}'
        return render(request, 'sandwich_generator.html', context={ 'sandwich': sandwich })



def full_menu(request):

    menu = []
    
    if request.method == 'GET':
        # return render(request=request, template_name='full_menu.html', context={ 'full_menu': full_menu })
        # selected_meat = random.choice(ingredients['meats'])
        # selected_cheese = random.choice(ingredients['cheeses'])
        # selected_topping = random.choice(ingredients['toppings'])
        # selected_bread = random.choice(ingredients['breads'])
        # selected_side = random.choice(ingredients['sides'])
        # selected_drinks = random.choice(ingredients['drinks'])
        # selected_sweet = random.choice(ingredients['sweets'])

        # menu = [f'{selected_meat} on {selected_bread} with {selected_cheese}, {selected_topping}, {selected_side}, {selected_drinks}, and a bit of {selected_sweet} to polish off this fine fiesty feast.'  ].append

        for cheese in ingredients['cheeses']:
            for meat in ingredients['meats']:
                for topping in ingredients['toppings']:
                    for bread in ingredients['breads']:
                        for side in ingredients['sides']:
                            for drink in ingredients['drinks']:
                                for sweet in ingredients['sweets']:
                                    # menu.append(x+y+z+a+b+c+d)
                                    menu.append(f'{meat} on {bread} with {cheese}, {topping}, {side}, {drink}, and a bit of {sweet}.')

        return render(request, 'full_menu.html', context={'menu': menu})