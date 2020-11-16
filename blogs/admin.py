from django.contrib import admin
from .models import Category,Tag,Post,ContentImage

class ContentImageInline(admin.TabularInline):
    model = ContentImage
    extra = 0

class PostAdmin(admin.ModelAdmin):
    inlines =  [
        ContentImageInline,
    ]

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post,PostAdmin)


