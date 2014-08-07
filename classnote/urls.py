from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'classnote.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^shownotes/index/', include('shownotes.urls')),
    url(r'^shownotes/getContent/', 'shownotes.views.getContent'),
    url(r'^shownotes/getNoteList/', 'shownotes.views.getNoteList'),
    url(r'^shownotes/getSchoolList/', 'shownotes.views.getSchoolList'),
    url(r'^shownotes/getDepartmentList/', 'shownotes.views.getDepartmentList'),
    url(r'^editnote/edit', include('editnote.urls')),
    url(r'^editnote/save', 'editnote.views.save'),
    url(r'^accounts/login/$',  login),
    url(r'^accounts/logout/$', logout, {'next_page': '/shownotes/index'}),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/my_notes', 'accounts.views.my_notes'),
)
