from django.contrib import admin
from quiz.models import QuestionPool, MCQOptions, Quiz


# class QuestionPoolAdmin(admin.ModelAdmin):

#     class Meta:
#         pass


# class QuestionOptionsAdmin(admin.ModelAdmin):

#     class Meta:
#         pass

class QuizAdmin(admin.ModelAdmin):

    class Meta:
        pass

# admin.site.register(QuestionPool, QuestionPoolAdmin)
# admin.site.register(MCQOptions, QuestionOptionsAdmin)
admin.site.register(Quiz, QuizAdmin)
