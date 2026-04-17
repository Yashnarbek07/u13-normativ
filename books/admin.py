from django.contrib import admin

# Register your models here.

from .models import Books, Author, User

# admin.site.register(Books)
# admin.site.register(Author)

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ("title", "description")

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")


@admin.register(User)

class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "date_of_birth", "user_age")
    def user_age(self, obj):
        return obj.get_user_age()
    user_age.short_description = "Age"