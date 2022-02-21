import jwt, datetime
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import generics
from rest_framework.response import Response

from .models import UserAccount
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        payload = {
            "uuid": str(user.uuid),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow(),
        }

        token = jwt.encode(payload, "secret", algorithm="HS256").decode("utf-8")

        response = Response()

        max_age = 365 * 24 * 60 * 60  # one year

        response.set_cookie(key="jwt", value=token, max_age=max_age, httponly=True)

        response.data = {
            "user": UserSerializer(user, context=self.get_serializer_context()).data
        }

        return response


# Login API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        max_age = 365 * 24 * 60 * 60  # one year

        payload = {
            "uuid": str(user.uuid),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60000),
            "iat": datetime.datetime.utcnow(),
        }

        token = jwt.encode(payload, "secret", algorithm="HS256").decode("utf-8")

        response = Response()

        response.set_cookie(key="jwt", value=token, max_age=max_age, httponly=True, domain="eprofa.com", samesite=None)

        response.data = {
            "user": UserSerializer(user, context=self.get_serializer_context()).data
        }

        return response


class LogoutAPI(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie("jwt")
        response.data = {"message": "success"}
        return response


class UserAPI(APIView):
    def get(self, request):
        token = request.COOKIES.get("jwt")

        if not token:
            raise AuthenticationFailed("Unauthenticated!")

        payload = jwt.decode(token, "secret", algorithm=["HS256"])

        user = UserAccount.objects.filter(uuid=payload["uuid"]).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)
