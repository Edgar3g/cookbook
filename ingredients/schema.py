from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Category, Ingredient

class CategoryNode(DjangoObjectType):

    class Meta:

        model = Category
        filter_fields = ['name', 'ingredients']
        interfaces = (relay.Node, )

class IngredientNode(DjangoObjectType):

    class Meta:

        model = Ingredient
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'notes': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact']
        }
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):

    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    ingredient =  relay.Node.Field(IngredientNode)
    all_ingredients = DjangoFilterConnectionField(IngredientNode)