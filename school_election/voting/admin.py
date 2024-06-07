from django.contrib import admin
from .models import Post, Candidate, Vote

class CandidateInline(admin.TabularInline):
    model = Candidate
    extra = 1
    fields = ['photo', 'name']

class PostAdmin(admin.ModelAdmin):
    inlines = [CandidateInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Candidate)
admin.site.register(Vote)
