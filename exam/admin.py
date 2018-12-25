# from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from exam.models import talk, grammar, short_conversation, noun, reading, Document, exam, UserProfile, System_administrator, Score_reviewers, Questions_bank_administrator, Questions_bank_operator, Exam_administrator, Examinees, Score, Company, Department, topic, member,post

# class UserProfileAdmin(ImportExportModelAdmin):
#     pass
# class talkAdmin(ImportExportModelAdmin):
#     pass
# class grammarAdmin(ImportExportModelAdmin):
#     pass
# class short_conversationAdmin(ImportExportModelAdmin):
#     pass
# class nounAdmin(ImportExportModelAdmin):
#     pass
# class readingAdmin(ImportExportModelAdmin):
#     pass

admin.site.register(talk)
admin.site.register(grammar)
admin.site.register(short_conversation)
admin.site.register(noun)
admin.site.register(reading)
admin.site.register(Document)
admin.site.register(exam)
admin.site.register(UserProfile)
admin.site.register(System_administrator)
admin.site.register(Score_reviewers)
admin.site.register(Questions_bank_administrator)
admin.site.register(Questions_bank_operator)
admin.site.register(Exam_administrator)
admin.site.register(Examinees)
admin.site.register(Score)
admin.site.register(Department)
admin.site.register(Company)
admin.site.register(topic)
admin.site.register(member)
admin.site.register(post)


