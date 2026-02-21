import graphene
import graphql_jwt
from graphql_jwt.utils import jwt_encode
from graphql_jwt.settings import jwt_settings
from graphql_jwt.refresh_token.models import RefreshToken
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

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)

    def mutate(self, info, username, password, email, first_name, last_name):
        user = get_user_model()(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save()

        payload = jwt_settings.JWT_PAYLOAD_HANDLER(user)
        # Generate JWT token after registration
        token = jwt_encode(payload)

        refresh_token = RefreshToken.objects.create(user=user)

        return CreateUser(user=user, token=token, refresh_token=refresh_token.token)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
