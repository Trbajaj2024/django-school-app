from django.contrib import admin
from .models import Carousel, Program, Event, LiveClass, Course, Achievement

# Register your models here to make them accessible in the Django admin interface.

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'image')
    list_editable = ('order',)
    search_fields = ('title', 'subtitle')
    list_per_page = 20

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'is_featured')
    list_filter = ('is_featured',)
    search_fields = ('title', 'description')
    list_per_page = 20

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'image')
    list_filter = ('date',)
    search_fields = ('title', 'description')
    date_hierarchy = 'date'
    list_per_page = 20

@admin.register(LiveClass)
class LiveClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'link')
    list_filter = ('date',)
    search_fields = ('title', 'description')
    date_hierarchy = 'date'
    list_per_page = 20

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'image')
    list_filter = ('is_featured',)
    search_fields = ('title', 'description')
    list_per_page = 20

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'image')
    list_filter = ('date',)
    search_fields = ('title', 'description')
    date_hierarchy = 'date'
    list_per_page = 20 