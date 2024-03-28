import os
from django.contrib import admin
from api.models import (
    Subject,
    Topic,
    Test,
    Question,
    Answer,
    Session,
    UserResponse,
)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ("title", "subject", "description")
    search_fields = ("title", "subject__name", "description")
    list_filter = ("subject",)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "subject", "difficulty")
    search_fields = ("text", "subject__name", "difficulty")
    list_filter = ("subject", "difficulty")


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("text", "question", "is_correct")
    search_fields = ("text", "question__text")
    list_filter = ("question", "is_correct")


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ("user", "test", "start_time", "end_time", "score")
    search_fields = ("user__username", "test__title")
    list_filter = ("test",)


@admin.register(UserResponse)
class UserResponseAdmin(admin.ModelAdmin):
    list_display = ("session", "question", "chosen_answer")
    search_fields = ("session__user__username", "question__text", "chosen_answer__text")
    list_filter = ("session",)


# Admin Dashboard Settings
admin.site.site_header = os.getenv("SITE_HEADER", default="Quimer Admin Dashboard")
admin.site.site_title = os.getenv("SITE_TITLE", default="Quimer")
admin.site.index_title = os.getenv("SITE_INDEX_TITLE", default="Quimer System")
