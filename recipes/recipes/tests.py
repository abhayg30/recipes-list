from rest_framework.test import APITestCase
from django.urls import reverse
import pymongo


class RecipeAPITest(APITestCase):
    def setUp(self):
        self.client_mongo = pymongo.MongoClient(
            "mongodb://admin:password@localhost:27017/recipe_db?authSource=admin"
        )
        self.db = self.client_mongo["recipe_db"]
        self.recipes_collection = self.db["recipes"]
        self.recipe = {
            "id": 1,
            "title": "Pancakes",
            "ingredients": [
                {"name": "Eggs", "unit": "grams", "quantity": 100},
                {"name": "Sugar", "unit": "grams", "quantity": 50},
                {"name": "Flour", "unit": "grams", "quantity": 200},
            ],
        }
        self.recipes_collection.insert_one(self.recipe)

    def tearDown(self):
        self.recipes_collection.delete_many({})

    def test_recipes_list(self):
        response = self.client.get(reverse("recipes-list"))
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.data), 0)
        self.recipes_collection.delete_many({})

    def test_create_recipe(self):
        payload = {
            "id": 4,
            "title": "Pancakes",
            "ingredients": [
                {"name": "Eggs", "unit": "grams", "quantity": 100},
                {"name": "Sugar", "unit": "grams", "quantity": 50},
                {"name": "Flour", "unit": "grams", "quantity": 200},
            ],
        }
        response = self.client.post(reverse("create-recipe"), payload, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertIn("title", response.data)
        self.assertEqual(payload, response.data)

    def test_retrieve_ingredients_with_servings_and_units(self):
        response = self.client.get(
            reverse("get-recipe", kwargs={"id": 4}),
            data={"servings": 2, "units": "pounds, ounces"},
            format="json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data["ingredients"][0]["quantity"],
            200 * 0.00220462,
        )
        self.assertIn(response.data["ingredients"][0]["unit"], ["pounds", "ounces"])
        self.recipes_collection.delete_many({})
