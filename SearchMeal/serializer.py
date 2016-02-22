from rest_framework import serializers
from .models import Variations, Ingredients, Recipe, Variation, RecipeIngredients


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        field = ('recipe_id', 'recipe_name')


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        field = ('ingredients_id', 'ingredient_name')


class VariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variation
        field = ('variation_id',)


class VariationsSerializer(serializers.ModelSerializer):
    variation_fk = VariationSerializer()
    ingredients_fk = IngredientsSerializer()

    class Meta:
        model = Variations
        field = ('variation_fk', 'ingredients_fk')


class RecipeIngredientsSerializer(serializers.ModelSerializer):
    rec_rec = RecipeSerializer()
    var_var_id = Variation

    class Meta:
        model = RecipeIngredients
        field = ('rec_rec', 'var_var_id')