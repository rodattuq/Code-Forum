# Create your views here.

from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
#from django.contrib.auth.decorators import login_required
from models import Cont, Question


def question_list(request, limit = 100):
	question_list = Question.objects.all()
	t = loader.get_template('forum/list.html')
	c = Context({'question_list':question_list})
	return HttpResponse(t.render(c))

class QuestionForm(ModelForm):
	class Meta:
		model = Cont
		exclude = ['post','contributor']



@csrf_exempt
def cont_detail(request,id,showCont = False):
	question = Question.objects.get(pk = id)
	t = loader.get_template('forum/detail.html')
	
	if showCont:
		conts = Cont.objects.filter(post__pk=id)
	if request.method == 'POST':
		cont = Cont(post=question)
		cont.contributor = request.user
		form = QuestionForm(request.POST, instance=cont)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(request.path)
	else:
			form = QuestionForm()
	c = Context({'question':question,'conts':conts,'form':form.as_p(),'logged_in':request.user.is_authenticated})
	return HttpResponse(t.render(c))


'''
@csrf_exempt
def blog_detail(request,id,showComments=False):
	blog = Blog.objects.get(pk = id)
	t = loader.get_template('blog/detail.html')
	
	print blog.id, blog.title, blog.body


	if showComments:
		comments = Comment.objects.filter(post__pk=id)
#		author = request.user
		#my lines
		#author = request.POST['username']
		#print "and the author cum user is...",author
		
		print comments
	if request.method == 'POST':
		comment = Comment(post=blog)
		comment.author = request.user

		form = CommentForm(request.POST, instance=comment)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(request.path)
	else:		
		form = CommentForm()
		
	c = Context({'blog':blog,'comments':comments,'form':form.as_p(),'logged_in':request.user.is_authenticated,'author':request.user,'request':request})
	return HttpResponse(t.render(c))
'''


