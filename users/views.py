import logging

from rest_framework.decorators import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)


class RegisterNewUser(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")

        try:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
            )
            logger.info("{} created successfully".format(user.username))
            return Response({"message": "User created"})
        except:
            logger.warning("{} email failed on User creation".format(email))
            return Response({"message": "User creation failed or user already exists"})
