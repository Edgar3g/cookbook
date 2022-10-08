app_name = "ingredients"
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView
from ingredients.schema import schema
urlpatterns = [
    path("api/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
