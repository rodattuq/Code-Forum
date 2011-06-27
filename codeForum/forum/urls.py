from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^$', 'forum.views.home'),
#	url(r'^list/(\d+)?$', 'blog.views.forum_list'),
#	url(r'^(detail|info)/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'blog.views.blog_detail'),
#	url(r'^search/(.*)$', 'blog.views.blog_search'),
#	url(r'^editcomment/(\d+)$','blog.views.edit_comment'),
       # url(r'^login/$', 'reg.views.loginView'), #
        #url(r'^login/$', 'reg.views.logoutView'), #
	
)
