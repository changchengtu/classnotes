from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'classnote.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^shownotes/index/', include('shownotes.urls')),
    url(r'^shownotes/getContent/', 'shownotes.views.getContent'),
    url(r'^editnote/edit', include('editnote.urls')),
    url(r'^editnote/save', 'editnote.views.save'),
)
