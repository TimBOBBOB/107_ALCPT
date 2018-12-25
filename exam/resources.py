from import_export import resources
from .models import talk, grammar, short_conversation, noun, reading, exam, UserProfile, Examinees, Score, Company, Department

class TalkResource(resources.ModelResource):
    class Meta:
        model = talk

class GrammarResource(resources.ModelResource):
    class Meta:
        model = grammar

class Short_conversationResource(resources.ModelResource):
    class Meta:
        model = short_conversation

class NounResource(resources.ModelResource):
    class Meta:
        model = noun

class ReadingResource(resources.ModelResource):
    class Meta:
        model = reading

class UserProfileResource(resources.ModelResource):
    class Meta:
        model = UserProfile

class ExamResource(resources.ModelResource):
    class Meta:
        model = exam

class ExaminessResource(resources.ModelResource):
    class Meta:
        modle = Examinees