from modeltranslation.translator import register, TranslationOptions
from .models import *
@register(ResumeCategory)
class ResumeCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Resume)
class ResumeTranslationOptions(TranslationOptions):
    fields = ('degree','place','description',)

@register(Skill)
class SkillTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(SkillCategory)
class SkillCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('name','description',)
    
@register(Portfolio)
class PortfolioTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Image)
class ImageTranslationOptions(TranslationOptions):
    fields = ('title','description',)