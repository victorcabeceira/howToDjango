from django.contrib import admin

from .models import (Course, Lesson, Material, Enrollment, Announcement, Comment)

class CourseAdmin(admin.ModelAdmin):

  list_display = ['name', 'slug', 'start_date', 'created_at']
  search_fields = ['name', 'slug', 'description']
  prepopulated_fields = {'slug': ('name',)}


class MaterialInlineAdmin(admin.StackedInline):

  model = Material


class LessonAdmin(admin.ModelAdmin):

  list_display = ['name', 'number', 'course', 'release_date']
  search_fields = ['name', 'description', 'course__name']
  list_filter = ['created_at']

  inlines = [
    MaterialInlineAdmin
  ]

admin.site.register(Course, CourseAdmin)
admin.site.register([Enrollment, Announcement, Comment])
admin.site.register(Lesson, LessonAdmin)
