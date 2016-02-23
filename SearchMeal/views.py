from django.shortcuts import render
from rest_framework import generics
from .serializer import RecipeIngredientsSerializer, VariationsSerializer
from .models import RecipeIngredients, Variations


class ViewsList(generics.ListAPIView):
    queryset = RecipeIngredients.objects.all()
    serializer_class = RecipeIngredientsSerializer


class VariationsList(generics.ListAPIView):
    serializer_class = VariationsSerializer

    def get_queryset(self):
        queryset = Variations.objects.all()
        var = self.request.query_params.get('var', None)
        if var is not None:
            queryset = queryset.filter(id)
        return queryset



def base(request):
    return render(request, "base.html")
