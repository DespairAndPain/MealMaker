from django.contrib import admin
from .models import RecipeIngredients, Recipe, Ingredients, Variations, Variation


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_display = ['recipe_name', 'recipe_id']


class IngredientsAdmin(admin.ModelAdmin):
    model = Ingredients
    list_display = ['ingredients_id', 'ingredient_name']


class VariationAdmin(admin.ModelAdmin):
    model = Variation
    list_display = ['variation_id']


class VariationsAdmin(admin.ModelAdmin):
    model = Variations
    list_display = ['variation_fk', 'ingredients_fk']


class RecipeIngredientsAdmin(admin.ModelAdmin):
    model = RecipeIngredients
    list_display = ['rec_rec', 'var_var_id']


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredients, IngredientsAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(Variations, VariationsAdmin)
admin.site.register(RecipeIngredients, RecipeIngredientsAdmin)

