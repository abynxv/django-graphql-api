import graphene
import graphql_jwt
from django.contrib.auth import get_user_model

class UserType(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    email = graphene.String()

class Query(graphene.ObjectType):
    me = graphene.Field(UserType)

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')
        return user

class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
