from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.template.defaultfilters import slugify
# Create your models here.

class ResumeCategory(models.Model):
    name = models.CharField(_("name"),max_length=200, blank=False, null=False,unique=True)
    class Meta:
        verbose_name=_("Categories of resume")
    
class Resume(models.Model):
    degree = models.CharField(max_length=200, blank=False, null=False)
    place = models.CharField(max_length=200, blank=False, null=False)
    description=models.TextField(null=True)
    startTime=models.DateTimeField()
    endTime=models.DateTimeField(_("endTime"), auto_now=False, auto_now_add=False)
    resumeCategory=models.ForeignKey(ResumeCategory, verbose_name=_("resume category"), on_delete=models.CASCADE,related_name='resumes')
  
class SkillCategory(models.Model):
    name= models.CharField(_("name"), max_length=100,unique=True)
    class Meta:
        verbose_name=_("Categories of skill")
        
class Skill(models.Model):
    name=models.CharField(_("name"), max_length=100,unique=True)
    level=models.IntegerField(_("level"))
    skillCategory=models.ForeignKey(SkillCategory, verbose_name=_("Skill Category"), on_delete=models.CASCADE,null=True,related_name='skills')
    
class Service(models.Model):
    name=models.CharField(_("name"), max_length=100,unique=True)
    picture=models.URLField(_("picture"))
    description=models.TextField(_("description"))
    class Meta:
        verbose_name=_("Service")
 
class Portfolio(models.Model):
    name= models.CharField(_("name"), max_length=100,unique=True)
    slug=models.SlugField(_("slug"),null=True)
    


class Image(models.Model):
    title=models.CharField(_("title"), max_length=50)
    description=models.TextField(_("description"))
    picture=models.URLField(_("picture"), max_length=200)
    appurl=models.URLField(_("appurl"), max_length=200,null=True)
    portfolio=models.ForeignKey(Portfolio, verbose_name=_("Portfolio"), on_delete=models.CASCADE,null=True,related_name='images')
        

class Message(models.Model):
    name=models.CharField(_("name"), max_length=50)
    email=models.EmailField(_("email"), max_length=254)
    comment=models.TextField(_("comment"))
    

class Client(models.Model):
    picture=models.URLField(_("picture"))
    
class Customer(models.Model):   
    name=models.CharField(_("name"), max_length=50)
    picture=models.URLField(_("picture"))
    job=models.CharField(_("job"), max_length=50)
    comment=models.TextField(_("comment"))
    

class CertificationCategory(models.Model):
    name= models.CharField(_("name"), max_length=100,unique=True)
    slug=models.SlugField(_("slug"),null=True)

    class Meta:
        verbose_name=_("Categories of certification")
        
class Certification(models.Model):
    name=models.CharField(_("name"), max_length=100,unique=True)
    slug=models.SlugField(_("slug"),null=True)
    school=models.CharField(_("school"), max_length=100)
    school_url=models.CharField(_("school_url"), max_length=100,null=True)
    picture_branding=models.URLField(_("picture_branding"), max_length=200)
    picture_certification=models.URLField(_("picture_certification"), max_length=200,null=True)
    link_certification=models.URLField(_("link_certification"), max_length=200)
    description=models.TextField(_("description"))
    CertificationCategory=models.ForeignKey(CertificationCategory, verbose_name=_("Certification Category"), on_delete=models.CASCADE,null=True,related_name='certifications')
    