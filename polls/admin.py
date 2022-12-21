from django.contrib import admin
from polls.models import Question ,Choice

admin.site.site_header = " Welcome to The Polls App Admin"
admin.site.site_title = "Polls App Admin"
admin.site.index_title = "Polls App Admin Phase "


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{
            'fields':['question_text']
        }),
        ('Date Information',{
            'fields':['pub_date'],'classes':['collapse']
        }),
    ] 
    inlines = [ChoiceInline]   
admin.site.register(Question,QuestionAdmin)



#  Normal way of registering the models 

#       admin.site.register(Question)
#       admin.site.register(Choice)
