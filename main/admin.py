from django.contrib import admin
from .models import Blog, BlogComment, Contact

# Register your models here.
admin.site.register(Blog)
admin.site.register(BlogComment)
admin.site.register(Contact)