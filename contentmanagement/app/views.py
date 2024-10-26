from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import User, Content, Category
from .serializers import UserSerializer, ContentSerializer, CategorySerializer
from .permissions import IsAuthorOrAdmin  
from django.contrib.auth import get_user_model

import logging
logger = logging.getLogger(__name__)

class UserRegisterView(APIView):
    def post(self, request):
        logger.info("Received registration request: %s", request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "user": UserSerializer(user).data,
                "token": token.key
            }, status=status.HTTP_201_CREATED)
        logger.error("Registration error: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomAuthToken, self).post(request, *args, **kwargs)
        
        # Check if the token is present
        token = response.data.get('token')
        if not token:
            return Response({"error": "Invalid credentials."}, status=400)

        user = User.objects.get(id=Token.objects.get(key=token).user_id)
        return Response({'token': token, 'user': UserSerializer(user).data})


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ['title', 'body', 'summary', 'categories__name']  # Search by title, body, summary, and category names

    def get_queryset(self):
        # If the user is an author, filter content by that author
        if self.request.user.role == 'author':
            return self.queryset.filter(author=self.request.user)
        return self.queryset  # Admin can see all content

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.IsAuthenticated()]
        return [permissions.IsAuthenticated(), IsAuthorOrAdmin()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
