from django.contrib import admin
from django.urls import path, include
from .views import (
    RecipesList,
    CreateRecipe,
    GetRecipe,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("recipes/create/", CreateRecipe.as_view(), name="create-recipe"),
    path("recipes/", RecipesList.as_view(), name="recipes-list"),
    path("recipes/<int:id>/", GetRecipe.as_view(), name="get-recipe"),
]
