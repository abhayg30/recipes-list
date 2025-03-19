from rest_framework import serializers
from .models import recipes_collection


class RecipesSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    ingredients = serializers.ListField(child=serializers.DictField())

    def create(self, validated_data):
        recipes_collection.insert_one(validated_data)
        return validated_data
