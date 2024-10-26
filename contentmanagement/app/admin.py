from django.contrib import admin
from .models import User, Content, Category

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'role', 'phone', 'address', 'city', 'state', 'country', 'pincode')
    search_fields = ('email', 'first_name', 'last_name', 'role', 'phone', 'address', 'city', 'state', 'country', 'pincode')
    list_filter = ('role',)
    ordering = ('id',)

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'body', 'summary', 'document', 'get_categories')  # Removed created_at
    search_fields = ('title', 'summary', 'author__email', 'body')
    list_filter = ('author', 'categories')
    ordering = ('-id',)  # Order by ID, you can change it later if you add created_at

    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])  # Join category names
    get_categories.short_description = 'Categories'  # Column header in admin

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
