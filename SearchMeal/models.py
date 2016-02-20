from django.db import models


class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    recipe_name = models.CharField(max_length=250)

    def __str__(self):
        return self.recipe_name


class Ingredients(models.Model):
    ingredients_id = models.AutoField(primary_key=True)
    ingredient_name = models.CharField(max_length=250)

    def __str__(self):
        return self.ingredient_name


class Variation(models.Model):
    variation_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return '{0}'.format(self.variation_id)


class Variations(models.Model):
    variation_fk = models.ForeignKey(Variation, verbose_name='Variation id')
    ingredients_fk = models.ForeignKey(Ingredients, verbose_name="Ingredients")


class RecipeIngredients(models.Model):
    rec_rec = models.ForeignKey(Recipe, verbose_name='Recipe')
    var_var_id = models.ForeignKey(Variation, verbose_name="Variation")








