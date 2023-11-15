from django_hosts import patterns, host
from django.contrib import admin

host_patterns = patterns(
    '',
    host(r'', 'anmaabank.urls', name=' '),
    host(r'anmaabank', 'anmaabankApp.urls', name='anmaabankApp'),
    # host(r'admin', admin.site.urls, name='admin'),
    # host(r'admin', "AdminApp.urls", name='AdminApp'),

    # host(r'', 'anmaabank.urls', name='www'),

    # path('admin-web/', ),

)
