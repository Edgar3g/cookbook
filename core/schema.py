
from core.settings import graphene
import ingredients.schema

class Query(ingredients.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)