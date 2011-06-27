from django.conf.urls.defaults import *

urlpatterns = patterns('',
#	url(r'^$', 'forum.views.home'),
	url(r'^list/(\d+)?$', 'forum.views.question_list'),
	url(r'^(detail|info)/(?P<id>\d+)/((?P<showCont>.*)/)?$', 'forum.views.cont_detail'),
#	url(r'^search/(.*)$', 'blog.views.blog_search'),
#	url(r'^editcomment/(\d+)$','blog.views.edit_comment'),
       # url(r'^login/$', 'reg.views.loginView'), #
        #url(r'^login/$', 'reg.views.logoutView'), #
	
)
