from django.contrib import admin
from django.db import models

# Create your models here.
class Question(models.Model):
	title  = models.CharField(max_length=60)
	body = models.TextField()
        contributor =  models.CharField(max_length=60)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.title

class Cont(models.Model):
	body =  models.TextField()

	author =  models.CharField(max_length=60)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	post = models.ForeignKey(Question )
	def __unicode__(self):
		return self.body
		#return self.author+"on "+self.updated+": "+self.body
		#return self.author
	def body_first_60(self):
		return self.body[:60]



class CommentInline(admin.TabularInline):
	model = Cont

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('title','created','updated')
	search_fields = ('title','body')
	list_filter = ('created',)
	inlines = [ContInline]	

class ContAdmin(admin.ModelAdmin):
	list_display = ('post','author','body_first_60','created','updated')
	list_filter = ('created',)


#Admin.site.register(Book, BookAdmin)



#first_name = models.CharField(max_length=50)

#admin.site.register(Blog)
#admin.site.register(Comment)
admin.site.register(Question,QuestionAdmin)
#admin.site.register(BlogInline)
admin.site.register(Cont,ContAdmin)
