from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .serializers import RecipesSerializers
from .models import recipes_collection
from .util import *

import json


class RecipesList(APIView):
    def get(self, request):
        recipes = recipes_collection.find({}, {"_id": 0, "id": 1, "title": 1})
        return Response(list(recipes))


class CreateRecipe(APIView):
    def post(self, request):
        serializer = RecipesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetRecipe(APIView):
    def get(self, request, id):
        data = request.query_params
        servings = int(data.get("servings", 1))
        units = data.get("units", "")
        units = units.split(", ")
        recipe = recipes_collection.find_one({"id": int(id)}, {"_id": 0, "id": 0})
        if not recipe:
            return Response("Recipe not found", status=status.HTTP_404_NOT_FOUND)
        ingredients = recipe["ingredients"]
        converted_ingredients = convert_units_and_servings(ingredients, servings, units)
        recipe["ingredients"] = converted_ingredients
        return Response(recipe)


class DeleteRecipes(APIView):
    def delete(self, request):
        recipes_collection.delete_many({})
        return Response("All recipes deleted", status=status.HTTP_204_NO_CONTENT)


def convert_units_and_servings(ingredients, servings, units):
    for ingredient in ingredients:
        ingredient["quantity"] *= servings
        if ingredient["unit"] == "grams" or ingredient["unit"] == "pounds":
            if ingredient["unit"] not in units and "grams" in units:
                ingredient["quantity"] = pounds_to_grams(ingredient["quantity"])
                ingredient["unit"] = "grams"
            elif ingredient["unit"] not in units and "pounds" in units:
                ingredient["quantity"] = grams_to_pounds(ingredient["quantity"])
                ingredient["unit"] = "pounds"

        elif ingredient["unit"] == "milliliters" or ingredient["unit"] == "ounces":
            if ingredient["unit"] not in units and "milliliters" in units:
                ingredient["quantity"] = ounces_to_milliliters(ingredient["quantity"])
                ingredient["unit"] = "milliliters"
            elif ingredient["unit"] not in units and "ounces" in units:
                ingredient["quantity"] = milliliters_to_ounces(ingredient["quantity"])
                ingredient["unit"] = "ounces"
    return ingredients
