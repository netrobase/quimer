from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "subject"
        ordering = ["name"]


class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "topic"
        ordering = ["name"]


class Test(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    topics = models.ManyToManyField(Topic)
    questions = models.ManyToManyField("Question")
    random_questions_count = models.IntegerField(
        default=10
    )  # Number of random questions to select

    def __str__(self):
        return self.title

    class Meta:
        db_table = "test"
        ordering = ["title"]


class Question(models.Model):
    DIFFICULTY_CHOICES = [
        ("Easy", "Easy"),
        ("Medium", "Medium"),
        ("Hard", "Hard"),
    ]
    text = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    topics = models.ManyToManyField(Topic)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)

    def __str__(self):
        return self.text

    class Meta:
        db_table = "question"
        ordering = ["text"]


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    class Meta:
        db_table = "answer"
        ordering = ["text"]


class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    time_limit = models.IntegerField()  # Time limit in minutes
    score = models.FloatField(default=0)

    def __str__(self):
        return f"{self.user.username}'s session for {self.test.title}"

    def is_expired(self):
        if self.end_time:
            return True
        return timezone.now() > self.start_time + timezone.timedelta(
            minutes=self.time_limit
        )

    def calculate_score(self):
        total_questions = self.test.questions.count()
        correct_responses = self.userresponse_set.filter(
            chosen_answer__is_correct=True
        ).count()
        self.score = (correct_responses / total_questions) * 100
        self.save()

    class Meta:
        db_table = "session"
        ordering = ["-start_time"]


class UserResponse(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    chosen_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.session.user.username}'s response for {self.question.text}"

    class Meta:
        db_table = "user_response"
        ordering = ["-session"]
