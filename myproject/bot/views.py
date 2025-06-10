from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TelegramUser
from .serializers import TelegramUserSerializer

class RegisterUserAPIView(APIView):
    def post(self, request):
        serializer = TelegramUserSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            # Проверка, есть ли уже пользователь с этим ID
            user, created = TelegramUser.objects.update_or_create(
                user_id=user_id,
                defaults={'name': serializer.validated_data['name']}
            )
            response_serializer = TelegramUserSerializer(user)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)