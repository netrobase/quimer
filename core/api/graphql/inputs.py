import graphene


class UserInput(graphene.InputObjectType):
    id = graphene.ID()
    username = graphene.String()
    email = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()
    password = graphene.String()


class SubjectInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()


class TopicInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()


class TestInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    description = graphene.String()
    subject_id = graphene.ID()
    topic_ids = graphene.List(graphene.ID)
    random_questions_count = graphene.Int()


class QuestionInput(graphene.InputObjectType):
    id = graphene.ID()
    text = graphene.String()
    subject_id = graphene.ID()
    topic_ids = graphene.List(graphene.ID)
    difficulty = graphene.String()


class AnswerInput(graphene.InputObjectType):
    id = graphene.ID()
    question_id = graphene.ID()
    text = graphene.String()
    is_correct = graphene.Boolean()


class SessionInput(graphene.InputObjectType):
    id = graphene.ID()
    user_id = graphene.ID()
    test_id = graphene.ID()
    start_time = graphene.String()
    end_time = graphene.String()
    time_limit = graphene.Int()
    score = graphene.Float()


class UserResponseInput(graphene.InputObjectType):
    id = graphene.ID()
    session_id = graphene.ID()
    question_id = graphene.ID()
    chosen_answer_id = graphene.ID()
