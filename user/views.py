from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import logout

from .models import AuthUser
from .serializers import RegisterAuthUserSerializer


class UserLogIn(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        print(user)

        token_tuple = Token.objects.get_or_create(user=user)

        token = token_tuple[0]

        if not token:
            return Response({
                "message": "Invalid credentials"
            }, status=403)

        return Response({
            'token': token.key,
            'id': user.pk,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'role': user.role,
        })


class UserRegister(generics.CreateAPIView):
    queryset = AuthUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterAuthUserSerializer


class UserLogOut(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # request.user.auth_token.delete()
        logout(request)
        return Response({"message": 'User Logged out successfully'})
