from django.contrib import admin
from django.db import models

# Create your models here.
class Question(models.Model):
	title  = models.CharField(max_length=60)
        author =  models.CharField(max_length=60)
	text = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.title




class Cont(models.Model):
	contributor =  models.CharField(max_length=60)
	contribution =  models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	post = models.ForeignKey(Question)
	def __unicode__(self):
		return self.contribution
		#return self.author+"on "+self.updated+": "+self.body
		#return self.author
	def text_first_60(self):
		return self.contribution[:60]



class ContInline(admin.TabularInline):
	model = Cont

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('author','title','created','updated')
	search_fields = ('title','text')
	list_filter = ('created',)
	inlines = [ContInline]	

class ContAdmin(admin.ModelAdmin):
	list_display = ('post','contributor','text_first_60','created','updated')
	list_filter = ('created',)


class Ratings(models.Model):
	rating = models.IntegerField()
	link = models.ForeignKey(Cont)
	like = models.BooleanField()
	dislike = models.BooleanField()

#Admin.site.register(Book, BookAdmin)



#first_name = models.CharField(max_length=50)

#admin.site.register(Blog)
#admin.site.register(Comment)
admin.site.register(Question,QuestionAdmin)
#admin.site.register(BlogInline)
admin.site.register(Cont,ContAdmin)
