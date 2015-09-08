from django.conf.urls import patterns, include, url

from django.contrib import admin
from views import ExcelExport, TableView, CreateProductView, ExcelExportTable, AdjusterView

from views import TagFilterView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'practica.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^table/', TableView.as_view()),
    url(r'^adjuster/', AdjusterView.as_view()),
    url(r'^tag-filter/', TagFilterView.as_view()),
    url(r'^productos/crear/?', CreateProductView.as_view()),
    url(r'^excelfile.xlsx/?', ExcelExportTable.as_view(), name='excelfile'),
)
