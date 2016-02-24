from django.shortcuts import render
from rest_framework import generics
from .serializer import RecipeIngredientsSerializer, VariationsSerializer
from .models import RecipeIngredients, Variations


class ViewsList(generics.ListAPIView):
    queryset = RecipeIngredients.objects.all()
    serializer_class = RecipeIngredientsSerializer


class VariationsList(generics.ListAPIView):
    serializer_class = VariationsSerializer

    # Параметры из url для поиска по ключю variation_id в Variation через Variations
    def get_queryset(self):
        queryset = Variations.objects.all()
        var = self.request.query_params.get('var', None)
        if var is not None:
            queryset = queryset.filter(variation_fk__variation_id=var)
        return queryset



def base(request):
    return render(request, "base.html")
