from rest_framework import viewsets, pagination
from rest_framework.response import Response
from .models import Subject, Topic, Test, Question, Answer, Session, UserResponse
from .serializers import (
    SubjectSerializer,
    TopicSerializer,
    TestSerializer,
    QuestionSerializer,
    AnswerSerializer,
    SessionSerializer,
    UserResponseSerializer,
)
from django.utils import timezone
import random

class CustomPagination(pagination.PageNumberPagination):
    page_size_query_param = "page_size"  # Client can specify the page size using the 'page_size' query parameter
    max_page_size = 100  # Maximum page size (optional)

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    pagination_class = CustomPagination


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    pagination_class = CustomPagination


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    pagination_class = CustomPagination


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    pagination_class = CustomPagination


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    pagination_class = CustomPagination


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    pagination_class = CustomPagination

    def create(self, request, *args, **kwargs):
        # Custom create method to handle session creation with random questions
        test_id = request.data.get("test")
        test = Test.objects.get(pk=test_id)
        questions = list(test.questions.all())
        random_questions = random.sample(questions, test.random_questions_count)
        request.data["start_time"] = timezone.now()
        request.data["end_time"] = None
        request.data["user"] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        session = Session.objects.get(pk=serializer.data["id"])
        session.save()  # Save session to update start_time
        serializer = self.get_serializer(session)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        # Custom update method to handle session expiration and score calculation
        instance = self.get_object()
        instance.end_time = timezone.now()
        instance.save()
        instance.calculate_score()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class UserResponseViewSet(viewsets.ModelViewSet):
    queryset = UserResponse.objects.all()
    serializer_class = UserResponseSerializer
    pagination_class = CustomPagination
