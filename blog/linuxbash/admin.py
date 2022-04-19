from django.contrib import admin
from .models import Post, Category, SubCategory, UploadFile

# Регистрация моделей для отображения в админке
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(UploadFile)