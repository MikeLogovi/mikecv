from django.contrib import admin
from .models import *
from django.utils.translation import gettext_lazy as _
admin.site.register(Service)
admin.site.register(Message)
admin.site.register(Client)
class ResumeInline(admin.TabularInline):
    model = Resume
    extra = 1
    fieldsets = (
        (None, {
            "fields": (
                ['degree_fr','degree_en','place_fr','place_en','description_fr','description_en','startTime','endTime']
            ),
        }),
    )
    verbose_name=_('Resume')
    
@admin.register(ResumeCategory)
class ResumeCategoryAdmin(admin.ModelAdmin):
    inlines=[ResumeInline]
    
class SkillInline(admin.TabularInline):
    model = Skill
    extra = 0
    fieldsets = (
        (None, {
            "fields": (
                ['name_fr','name_en','level']
            ),
        }),
    )
    verbose_name=_('Skill')
    verbose_name_plural=_('Skills')
     
@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    inlines=[SkillInline]
    
class  ImageInline(admin.TabularInline):
    model = Image
    extra = 0
    fieldsets = (
        (None, {
            "fields": (
                ['title_fr','title_en','description_fr','description_en','picture','appurl']
            ),
        }),
    )
    verbose_name="Image"
    verbose_name_plural="Images"
    
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    inlines=[ImageInline]