from django.contrib import admin
from board.models import Notice,From_mark,To_mark,Freetalk,Auth,Question,Inquiry,Report
from board.models import To_mark_Comment,Freetalk_Comment,Auth_Comment,Question_Comment,Inquiry_Comment,Report_Comment
from django_summernote.admin import SummernoteModelAdmin


class NoticeAdmin(SummernoteModelAdmin):
    list_display = ('id', 'subject', 'name', 'memo', 'hits', 'create_date')


class From_markAdmin(SummernoteModelAdmin):
    list_display = ('id', 'subject', 'name', 'memo', 'hits', 'create_date')


class To_markAdmin(SummernoteModelAdmin):
    list_display = ('id', 'subject', 'name', 'memo', 'hits', 'create_date')

class To_mark_CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'text', 'created_date')


class FreetalkAdmin(SummernoteModelAdmin):
    list_display = ('id', 'subject', 'name', 'memo', 'hits', 'create_date')

class Freetalk_CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'text', 'created_date')


class AuthAdmin(SummernoteModelAdmin):
    list_display = ('id', 'subject', 'name', 'memo', 'hits', 'create_date')

class Auth_CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'text', 'created_date')


class QuestionAdmin(SummernoteModelAdmin):
    list_display = ('id', 'subject', 'name', 'memo', 'hits', 'create_date')

class Question_CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'text', 'created_date')

class InquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'created_date')

class Inquiry_CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'text', 'created_date')

class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'created_date')

class Report_CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'text', 'created_date')            
          


admin.site.register(Notice,NoticeAdmin)

admin.site.register(From_mark,From_markAdmin)

admin.site.register(To_mark,To_markAdmin)
admin.site.register(To_mark_Comment,To_mark_CommentAdmin)

admin.site.register(Freetalk,FreetalkAdmin)
admin.site.register(Freetalk_Comment,Freetalk_CommentAdmin)

admin.site.register(Auth,AuthAdmin)
admin.site.register(Auth_Comment,Auth_CommentAdmin)

admin.site.register(Question,QuestionAdmin)
admin.site.register(Question_Comment,Question_CommentAdmin)

admin.site.register(Inquiry,InquiryAdmin)
admin.site.register(Inquiry_Comment,Inquiry_CommentAdmin)

admin.site.register(Report,ReportAdmin)
admin.site.register(Report_Comment,Report_CommentAdmin)