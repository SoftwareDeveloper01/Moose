from django.contrib import admin
from .models import Blog, Contact, Comment


# website ni admin panelida ko'rinib turadigan narsalarni ro'yxatini shu yerga kiritamiz

class BlogAdmin(admin.ModelAdmin):
    # doim list_display degan o'zgaruvchini ichida yoziladi admin panelida ko'rinishi kerak bo'lgan narsalar 
    list_display = [
        'title',
        'created_at',
        'is_published',
        'author',
        'views'
    ]


class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'email',
        'subject',
        'is_solved',
        'created_at'
    ]
    
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'left_at',
        'is_solved'
    ]



admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Comment, CommentAdmin)
