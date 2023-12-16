
from pathlib import Path
import os
from pathlib import Path
import platform
from django.contrib import admin

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_FILE_PATH = BASE_DIR.joinpath('testssss').joinpath('email')
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'anmaqbank@gmail.com'
# EMAIL_HOST_PASSWORD = 'zxcv$12345'
EMAIL_HOST_PASSWORD = 'wcqhikkdekylirxh'


EMAIL_PORT = 587

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(fjc8681t$5fa7_8-nys)1w94pg3x7fca)nps!w$*z%#4-!fqp'
# SECRET_KEY = os.environ["SECRET_KEY"]
# SECRET_KEY_FALLBACKS = [
#     os.environ["OLD_SECRET_KEY"],
# ]
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = False

# security.W018
# DEBUG = False

# # security.W016
# CSRF_COOKIE_SECURE = False

# # security.W012
# SESSION_COOKIE_SECURE = False

# # security.W008
# SECURE_SSL_REDIRECT = False

# # security.W004
# SECURE_HSTS_SECONDS = 31536000  # One year in seconds

# # Another security settings
# SECURE_HSTS_INCLUDE_SUBDOMAINS = False
# SECURE_HSTS_PRELOAD = False
# SECURE_CONTENT_TYPE_NOSNIFF = False
# CORS_REPLACE_HTTPS_REFERER = False
# HOST_SCHEME = "http://"
# SECURE_PROXY_SSL_HEADER = None
# SECURE_SSL_REDIRECT = False
# SESSION_COOKIE_SECURE = False
# CSRF_COOKIE_SECURE = False
# SECURE_HSTS_SECONDS = None
# SECURE_HSTS_INCLUDE_SUBDOMAINS = False
# SECURE_FRAME_DENY = False
# security.W022
# I think it won't be needed. Because there are many ways.

ALLOWED_HOSTS = ['*',]


# # Application definition
# AUTHENTICATION_BACKENDS = [
#     # Needed to login by username in Django admin, regardless of `allauth`
#     'django.contrib.auth.backends.ModelBackend',

#     # Django-allauth
#     # `allauth` specific authentication methods, such as login by e-mail
#     # https://django-allauth.readthedocs.io/en/latest/installation.html
#     'allauth.account.auth_backends.AuthenticationBackend',
# ]

# SITE_ID = 1

# LOGIN_URL = "account/login"
# LOGIN_REDIRECT_URL = "/"
# LOGOUT_REDIRECT_URL = "/"


# Django-allauth
# https://django-allauth.readthedocs.io/en/latest/configuration.html
# ACCOUNT_AUTHENTICATION_METHOD = "username_email"
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
# ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
RECAPTCHA_PUBLIC_KEY = '6LdQys8oAAAAAIZUzE8L5PkE82Ak2eUzgvrhH9fM'
RECAPTCHA_PRIVATE_KEY = '6LdQys8oAAAAAIZUzE8L5PkE82Ak2eUzgvrhH9fM'

INSTALLED_APPS = [
    # 'core',  # Here

    # "crispy_formdeps",
    # "crispy_bootstrap4",
    # 'dal',
    # 'dal_select2',
    'pygmentify',


    'import_export',

    'django_select2',

    "selectable",

    # 'grappelli',
    'tinymce',

    #   'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'django.contrib.auth',
    # 'django.contrib.sites',
    # 'django.contrib.flatpages',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    # 'django.contrib.sites',

    "crispy_bootstrap5",

    # 'bootstrap3',

    # "liststyle",
    'django.contrib.admin',
    #

    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    'crispy_forms',
    # "ckeditor",
    'adsense.apps.AdsenseConfig',
    'anmaabankApp.apps.AnmaabankAppConfig',
    'anmaabankApp.templatetags.poll_extras',
    'clients.apps.ClientsConfig',
    'Partners.apps.PartnersConfig',
    'FrequentlyAskedQuestions.apps.FrequentlyaskedquestionsConfig',
    'teams.apps.TeamsConfig',
    "OurNewsletter.apps.OurnewsletterConfig",
    'Testimonials.apps.TestimonialsConfig',
    'SendEmile.apps.SendemileConfig',
    # 'tinymce',
    'ckeditor',  # CKEditor config
    'ckeditor_uploader',


    # 'liststyle',

    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.linkedin_oauth2',
    # 'allauth.socialaccount.providers.github',
    'django_cleanup.apps.CleanupConfig',
    # 'storages',
    # "career.apps.CareerConfig",
    "django_countries",

    'Awards.apps.AwardsConfig',
    'OurMarch.apps.OurmarchConfig',
    'OurVision.apps.OurvisionConfig',
    'OurMission.apps.OurmissionConfig',
    'AdminApp.apps.AdminAppConfig',


    'django_user_agents',
    'django_hosts',
    'settingapp',
    'servicesapp',
    "branches",
    'country_regions',
    "phonenumber_field",
    'portfolioapp',
    'sectionpage',
    'django_admin_generator',
    'navbarapp',
    'autocomplete_all',
    'blogapp',
    'currencies',
    'jopapp',
    'loan_app',
    'content_library'








    # CKEditor media uploader
]
INSTALLED_APPS += [
    'widget_tweaks',
]
INSTALLED_APPS += [

    "django.contrib.humanize",
]
PHONENUMBER_DEFAULT_REGION = "YE"

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:8000',
#     }
# }
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
# Name of cache backend to cache user agents. If it not specified default
# cache alias will be used. Set to `None` to disable caching.
USER_AGENTS_CACHE = 'default'
CKEDITOR_UPLOAD_PATH = "uploads/"

# CKEDITOR_CONFIGS = {
#     'default': {

#         'toolbar_Custom': [
#             {'name': 'document', 'items': [
#                 'Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
#             {'name': 'clipboard', 'items': [
#                 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
#             {'name': 'editing', 'items': [
#                 'Find', 'Replace', '-', 'SelectAll']},
#             {'name': 'forms',
#              'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
#                        'HiddenField']},
#             '/',
#             {'name': 'basicstyles',
#              'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
#             {'name': 'paragraph',
#              'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
#                        'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
#                        'Language']},
#             {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
#             {'name': 'insert',
#              'items': ['Image', 'Youtube', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
#             '/',
#             {'name': 'styles', 'items': [
#                 'Styles', 'Format', 'Font', 'FontSize']},
#             {'name': 'colors', 'items': ['TextColor', 'BGColor']},
#             {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
#             {'name': 'about', 'items': ['CodeSnippet']},
#             {'name': 'about', 'items': ['About']},
#             '/',  # put this to force next toolbar on new line
#             {'name': 'yourcustomtools', 'items': [
#                 # put the name of your editor.ui.addButton here
#                 'Preview',
#                 'Maximize',

#             ]},
#         ],
#         'toolbar': 'Custom',  # put selected toolbar config here
#         'toolbarGroups': [{'name': 'document', 'groups': ['mode', 'document', 'doctools']}],
#         'height': 400,
#         # 'width': '100%',
#         'filebrowserWindowHeight': 725,
#         'filebrowserWindowWidth': 940,
#         'toolbarCanCollapse': True,
#         'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
#         'tabSpaces': 4,
#         'extraPlugins': ','.join([
#             'uploadimage',  # the upload image feature
#             # your extra plugins here
#             'div',
#             'autolink',
#             'autoembed',
#             'embedsemantic',
#             'autogrow',
#             'devtools',
#             'widget',
#             'lineutils',
#             'clipboard',
#             'dialog',
#             'dialogui',
#             'elementspath',
#             'codesnippet',
#         ]),
#     }
# }


# <script src="" referrerpolicy="origin"></script>
# TINYMCE_JS_URL = "https://anmaqbank.pythonanywhere.com/static/assets/tinymce/tinymce.min.js"
# CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
#   <script src="" referrerpolicy="origin"></script>
# TINYMCE_JS_URL = "https://cdn.tiny.cloud/1/pxi8iu9cpmoaxzsbp1ph3bb14kjjxi9pegd9u6i0l8vdtckd/tinymce/6/tinymce.min.js"
# REFERRER_POLICY = "origin"
# TINYMCE_JS_URL ="https://cdn.tiny.cloud/1/pxi8iu9cpmoaxzsbp1ph3bb14kjjxi9pegd9u6i0l8vdtckd/tinymce/6/plugins.min.js"
# TINYMCE_JS_URL = os.path.join(BASE_DIR, "/static/asset/tinymce/tinymce.min.js")
# STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
# print(str(BASE_DIR) + "/static/asset/tinymce/tinymce.min.js")
REFERRER_POLICY = True
CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True


CSRF_TRUSTED_ORIGINS = [

]

CORS_REPLACE_HTTPS_REFERER = True

# CSRF_COOKIE_DOMAIN = 'bluemix.net'

CORS_ORIGIN_WHITELIST = (
    'https://front.bluemix.net/',
    'front.bluemix.net',
    'bluemix.net',
    'https://site.lv',
    'https://www.site.lv',
    "https://tiny.cloud",
    "https://www.tiny.cloud",
    "https://cdn.tiny.cloud",
)
CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_ALLOW_ALL = True
# TINYMCE_JS_URL = 'https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js'
TINYMCE_COMPRESSOR = False
CORS_ALLOW_CREDENTIALS = True
TINYMCE_COMPRESSOR = False
TINYMCE_DEFAULT_CONFIG = {
    "theme": "silver",
    # 'theme': 'modern',
    "content_css": 'static/assets/css/mycontent.css',


    "resize": "true",
    "menubar": "file edit view insert format tools table help",
    "toolbar": "link paste pastetext undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | a11ycheck ltr rtl | showcomments addcomment code typography | aligncenter alignjustify alignleft alignnone alignright| anchor | blockquote blocks | backcolor | bold | copy | cut | fontfamily fontsize forecolor h1 h2 h3 h4 h5 h6 hr indent | italic | language | lineheight | newdocument | outdent | paste pastetext | print | redo | remove removeformat | selectall | strikethrough | styles | subscript superscript underline | undo | visualaid | a11ycheck advtablerownumbering typopgraphy anchor restoredraft casechange charmap checklist code codesample addcomment showcomments ltr rtl editimage fliph flipv imageoptions rotateleft rotateright emoticons export footnotes footnotesupdate formatpainter fullscreen help image insertdatetime link openlink unlink bullist numlist media mergetags mergetags_list nonbreaking pagebreak pageembed permanentpen preview quickimage quicklink quicktable cancel save searchreplace spellcheckdialog spellchecker | table tablecellprops tablecopyrow tablecutrow tabledelete tabledeletecol tabledeleterow tableinsertdialog tableinsertcolafter tableinsertcolbefore tableinsertrowafter tableinsertrowbefore tablemergecells tablepasterowafter tablepasterowbefore tableprops tablerowprops tablesplitcells tableclass tablecellclass tablecellvalign tablecellborderwidth tablecellborderstyle tablecaption tablecellbackgroundcolor tablecellbordercolor tablerowheader tablecolheader | tableofcontents tableofcontentsupdate | template typography | insertfile | visualblocks visualchars | wordcount",
    # "menubar": 'file edit view insert format tools table help',
    #   "toolbar": 'undo redo | bold italic underline strikethrough | fontfamily fontsize blocks | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist | forecolor backcolor removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | insertfile image media template link anchor codesample | ltr rtl',
    "toolbar_sticky": True,
    "autosave_ask_before_unload": True,
    "autosave_interval": "30s",
    "autosave_prefix": "{path}{query}-{id}-",
    "autosave_restore_when_empty": True,
    "autosave_retention": "30s",
    "image_advtab": True,
    "content_css": [
        #        'https//www.tiny.cloud/css/codepen.min.css',
        'https://fonts.googleapis.com/css?family=Lato:300,300i,400,400i,500,500i,700,700i,600,600i',
        'https://fonts.googleapis.com/css?family=Consolas:300,300i,400,400i,500,500i,700,700i,600,600i',
        'https://www.tinymce.com/css/codepen.min.css',
        'https://cdn.jsdelivr.net/npm/prismjs@1.18.0/components/prism-bash.js'
    ],
    # "link_list": [
    #     {"title": 'My page 1', "value": 'http://www.tinymce.com'},
    #     {"title": 'My page 2', "value": 'http://www.moxiecode.com'}
    # ],
    "image_list": [
        {"title": 'My page 1', "value": 'http://www.tinymce.com'},
        {"title": 'My page 2', "value": 'http://www.moxiecode.com'}
    ],
    "image_class_list": [
        {"title": 'None', "value": ''},
        {"title": 'Some class', "value": 'class-name'}
    ],
    "importcss_append": True,
    #   "file_picker_callback": function (callback, value, meta) {
    # /* Provide file and text for the link dialog */
    # if (meta.filetype === 'file') {
    #   callback('https://www.google.com/logos/google.jpg', { text: 'My text' });
    # }

    # /* Provide image and alt text for the image dialog */
    # if (meta.filetype === 'image') {
    #   callback('https://www.google.com/logos/google.jpg', { alt: 'My alt text' });
    # }

    # /* Provide alternative source and posted for the media dialog */
    # if (meta.filetype === 'media') {
    #   callback('movie.mp4', { source2: 'alt.ogg', poster: 'https://www.google.com/logos/google.jpg' });
    # }
    #   },
    # "templates": [
    #     {"title": 'New Table', "description": 'creates a new table',
    #         "content": '<div class="mceTmpl"><table width="98%%"  border="0" cellspacing="0" cellpadding="0"><tr><th scope="col"> </th><th scope="col"> </th></tr><tr><td> </td><td> </td></tr></table></div>'},
    #     {"title": 'Starting my story', "description": 'A cure for writers block',
    #      "content": 'Once upon a time...'},
    #     {"title": 'New list with dates', "description": 'New List with dates',
    #      "content": '<div class="mceTmpl"><span class="cdate">cdate</span><br /><span class="mdate">mdate</span><h2>My List</h2><ul><li></li><li></li></ul></div>'}
    # ],
    # "template_cdate_format": '[Date Created (CDATE): %m/%d/%Y : %H:%M:%S]',
    # "template_mdate_format": '[Date Modified (MDATE): %m/%d/%Y : %H:%M:%S]',
    "height": 520,
    "image_caption": True,
    "quickbars_selection_toolbar": 'bold italic | quicklink h2 h3 blockquote quickimage quicktable',
    "noneditable_noneditable_class": "mceNonEditable",
    "toolbar_mode": 'sliding',



    "paste_block_drop": False,
    'paste_enable_default_filters': True,
    "paste_merge_formats": True,
    "paste_filter_drop": False,
    "paste_tab_spaces": 2,
    "smart_paste": True,
    "paste_data_images": True,
    "paste_remove_styles_if_webkit": False,
    # "paste_webkit_styles": 'color font-size',



    "browser_spellcheck": True,






    "contextmenu": "link image imagetools table undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | a11ycheck ltr rtl | showcomments addcomment code typography",
    # "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | a11ycheck ltr rtl | showcomments addcomment code typography",
    # "plugins": """
    #  textcolor save link image media preview codesample contextmenu
    # table code lists fullscreen insertdatetime nonbreaking
    # contextmenu directionality searchreplace wordcount visualblocks
    # visualchars code fullscreen autolink lists charmap print hr
    # anchor pagebreak advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code fullscreen insertdatetime media table powerpaste advcode help wordcount spellchecker typography
    # """,
    "plugins": """link paste preview importcss searchreplace autolink autosave save directionality code visualblocks visualchars fullscreen image link media template codesample table charmap pagebreak nonbreaking anchor insertdatetime advlist lists wordcount help charmap quickbars emoticons 
    textcolor save link image media preview  contextmenu
    table code lists fullscreen insertdatetime nonbreaking
    contextmenu directionality searchreplace wordcount visualblocks
    visualchars code fullscreen autolink lists charmap print hr
    anchor pagebreak advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code fullscreen insertdatetime media table powerpaste advcode help wordcount spellchecker typography
    """,
    "link_assume_external_targets": True,

    "codesample_global_prismjs": True,

    'toolbar1': '''
        fullscreen preview bold italic underline | fontselect,
        fontsizeselect | forecolor backcolor | alignleft alignright |
        aligncenter alignjustify | indent outdent | bullist numlist table |
        | link image media | codesample |
    ''',
    'toolbar2': '''
        visualblocks visualchars |
        charmap hr pagebreak nonbreaking anchor | code | 
        undo redo | formatpainter casechange blocks | bold italic backcolor |  
          alignleft aligncenter alignright alignjustify | 
          bullist numlist checklist outdent indent | removeformat | a11ycheck code table help

    ''',
    # "selector": "textarea",  

    "codesample_languages": [
        # {"text": 'HTML/XML', "value": 'markup'},
        # {"text": 'JavaScript', "value": 'javascript'},
        # {"text": 'CSS', "value": 'css'},
        # {"text": 'PHP', "value": 'php'},
        # {"text": 'Ruby', "value": 'ruby'},
        # {"text": 'Python', "value": 'python'},
        # {"text": 'Java', "value": 'java'},
        # {"text": 'C', "value": 'c'},
        # {"text": 'C#', "value": 'csharp'},
        # {"text": 'C++', "value": 'cpp'},







        {"text": "Shell", "value": "sh"},
        # {"text": "console", "value": "console"},
        # lang-sh


        {"text": 'HTML/XML', "value": 'markup'},
        {"text": "XML", "value": "xml"},
        {"text": "HTML", "value": "markup"},
        {"text": "mathml", "value": "mathml"},
        {"text": "SVG", "value": "svg"},
        {"text": "CSS", "value": "css"},
        {"text": "Clike", "value": "clike"},
        {"text": "Javascript", "value": "javascript"},
        {"text": "ActionScript", "value": "actionscript"},
        {"text": "apacheconf", "value": "apacheconf"},
        {"text": "apl", "value": "apl"},
        {"text": "applescript", "value": "applescript"},
        {"text": "asciidoc", "value": "asciidoc"},
        {"text": "aspnet", "value": "aspnet"},
        {"text": "autoit", "value": "autoit"},
        {"text": "autohotkey", "value": "autohotkey"},
        {"text": "bash", "value": "bash"},
        {"text": "basic", "value": "basic"},
        {"text": "batch", "value": "batch"},
        {"text": "c", "value": "c"},
        {"text": "brainfuck", "value": "brainfuck"},
        {"text": "bro", "value": "bro"},
        {"text": "bison", "value": "bison"},
        {"text": "C#", "value": "csharp"},
        {"text": "C++", "value": "cpp"},
        {"text": "CoffeeScript", "value": "coffeescript"},
        {"text": "ruby", "value": "ruby"},
        {"text": "d", "value": "d"},
        {"text": "dart", "value": "dart"},
        {"text": "diff", "value": "diff"},
        {"text": "docker", "value": "docker"},
        {"text": "eiffel", "value": "eiffel"},
        {"text": "elixir", "value": "elixir"},
        {"text": "erlang", "value": "erlang"},
        {"text": "fsharp", "value": "fsharp"},
        {"text": "fortran", "value": "fortran"},
        {"text": "git", "value": "git"},
        {"text": "glsl", "value": "glsl"},
        {"text": "go", "value": "go"},
        {"text": "groovy", "value": "groovy"},
        {"text": "haml", "value": "haml"},
        {"text": "handlebars", "value": "handlebars"},
        {"text": "haskell", "value": "haskell"},
        {"text": "haxe", "value": "haxe"},
        {"text": "http", "value": "http"},
        {"text": "icon", "value": "icon"},
        {"text": "inform7", "value": "inform7"},
        {"text": "ini", "value": "ini"},
        {"text": "j", "value": "j"},
        {"text": "jade", "value": "jade"},
        {"text": "java", "value": "java"},
        {"text": "JSON", "value": "json"},
        {"text": "jsonp", "value": "jsonp"},
        {"text": "julia", "value": "julia"},
        {"text": "keyman", "value": "keyman"},
        {"text": "kotlin", "value": "kotlin"},
        {"text": "latex", "value": "latex"},
        {"text": "less", "value": "less"},
        {"text": "lolcode", "value": "lolcode"},
        {"text": "lua", "value": "lua"},
        {"text": "makefile", "value": "makefile"},
        {"text": "markdown", "value": "markdown"},
        {"text": "matlab", "value": "matlab"},
        {"text": "mel", "value": "mel"},
        {"text": "mizar", "value": "mizar"},
        {"text": "monkey", "value": "monkey"},
        {"text": "nasm", "value": "nasm"},
        {"text": "nginx", "value": "nginx"},
        {"text": "nim", "value": "nim"},
        {"text": "nix", "value": "nix"},
        {"text": "nsis", "value": "nsis"},
        {"text": "objectivec", "value": "objectivec"},
        {"text": "ocaml", "value": "ocaml"},
        {"text": "oz", "value": "oz"},
        {"text": "parigp", "value": "parigp"},
        {"text": "parser", "value": "parser"},
        {"text": "pascal", "value": "pascal"},
        {"text": "perl", "value": "perl"},
        {"text": "PHP", "value": "php"},
        {"text": "processing", "value": "processing"},
        {"text": "prolog", "value": "prolog"},
        {"text": "protobuf", "value": "protobuf"},
        {"text": "puppet", "value": "puppet"},
        {"text": "pure", "value": "pure"},
        {"text": "python", "value": "python"},
        {"text": "q", "value": "q"},
        {"text": "qore", "value": "qore"},
        {"text": "r", "value": "r"},
        {"text": "jsx", "value": "jsx"},
        {"text": "rest", "value": "rest"},
        {"text": "rip", "value": "rip"},
        {"text": "roboconf", "value": "roboconf"},
        {"text": "crystal", "value": "crystal"},
        {"text": "rust", "value": "rust"},
        {"text": "sas", "value": "sas"},
        {"text": "sass", "value": "sass"},
        {"text": "scss", "value": "scss"},
        {"text": "scala", "value": "scala"},
        {"text": "scheme", "value": "scheme"},
        {"text": "smalltalk", "value": "smalltalk"},
        {"text": "smarty", "value": "smarty"},
        {"text": "SQL", "value": "sql"},
        {"text": "stylus", "value": "stylus"},
        {"text": "swift", "value": "swift"},
        {"text": "tcl", "value": "tcl"},
        {"text": "textile", "value": "textile"},
        {"text": "twig", "value": "twig"},
        {"text": "TypeScript", "value": "typescript"},
        {"text": "verilog", "value": "verilog"},
        {"text": "vhdl", "value": "vhdl"},
        {"text": "wiki", "value": "wiki"},
        {"text": "YAML", "value": "yaml"}
    ],
    # "codesample_dialog_height": 400,
    # "codesample_dialog_width": 600,
    # "skin": "oxide-dark",
    # "content_css": "dark",
    "language": "ar",
    "directionality":  ['rtl', 'ltr'],

    "content_langs": [
        {"title": 'English', "code": 'en'},
        {"title": 'Arabic', "code": 'Ar'},

    ],
    # 'cleanup_on_startup': True,
    # 'custom_undo_redo_levels': 20,
    # # "tinycomments_mode": 'embedded',
    "tinycomments_author": 'Ibrahim Shaher Saeed ',
    # "mergetags_list": [
    #     {"value": 'First.Name', "title": 'Ibrahim Shaher Saeed'},
    #     {"value": 'Email', "title": 'ibrhm.shahr@gmail.com'},
    # ]
}

from django.utils.translation import ugettext_lazy as _

LOCALE_PATHS = [    
    os.path.join(BASE_DIR, "locale")
    ,
]
LANGUAGE_CODE ="ar"
# LANGUAGE_COOKIE_NAME = "alinma-lang"
LANGUAGES = [
    ("ar", _("Arabic")),
    ("en", _("English")),
]
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django_hosts.middleware.HostsRequestMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    "django.contrib.admindocs.middleware.XViewMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # "subdomains.middleware.SubdomainURLRoutingMiddleware",
    # "django.middleware.csrf.CsrfResponseMiddleware",
    # 'current_user.CurrentUserMiddleware',
    # 'tutorial.current_user.CurrentUserMiddleware',
    # "anmaabank.middleware.SaveInfoIpMiddleware",
    # 'django_hosts.middleware.HostsResponseMiddleware',
]
# MIDDLEWARE_CLASSES = (
#     # other middlewares...
#     'django_user_agents.middleware.UserAgentMiddleware',
# )
SITE_ID = 1  # define the site id
ROOT_URLCONF = 'anmaabank.urls'
# ROOT_URLCONF = 'anmaabank.urls'

ROOT_HOSTCONF = 'anmaabank.hosts'
DEFAULT_HOST = ' '

USER_AGENTS_CACHE = 'default'
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }
X_FRAME_OPTIONS = 'ALLOWALL'

XS_SHARING_ALLOWED_METHODS = ['POST', 'GET', 'OPTIONS', 'PUT', 'DELETE']


LOGIN_REDIRECT_URL = "/"
CRISPY_TEMPLATE_PACK = 'bootstrap4'
# ADMINS = (
#     ('deusdies', 'b@bo.vc'),
# )

# MANAGERS = ADMINS
# USE_I18N = True

# SUBDOMAIN_URLCONFS = {
#     # None: "anmaabank.urls",
#     "www": "anmaabank.urls",
#     # "api": "anmaabank.urls.api",
#     # "admin": admin.site.urls,
# }
USE_THOUSAND_SEPARATOR = True


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': ["templates"],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'app.apptemplates.load_setting',



            ],
            'libraries':{
                'to_and': 'anmaabankApp.templatetags.poll_extras',
                'check_share_url': 'anmaabankApp.templatetags.poll_extras',
                'to_lat': 'anmaabankApp.templatetags.poll_extras',
                'to_str': 'anmaabankApp.templatetags.poll_extras',
                "in_column_navbar_chield": 'anmaabankApp.templatetags.poll_extras',

                "in_type_services": 'anmaabankApp.templatetags.poll_extras',
                "in_categories_services": 'anmaabankApp.templatetags.poll_extras',
                'intToword': 'anmaabankApp.templatetags.poll_extras',



            }
        },
    },
]

WSGI_APPLICATION = 'anmaabank.wsgi.application'
MIDDLEWARE_CLASSES = (
    # other middlewares...
    'django_user_agents.middleware.UserAgentMiddleware',
)

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'alinmabank',
        # 'USER': 'root',
        'USER': 'djangouser',
        'PASSWORD': 'MYSQL@2030',
        'HOST':'127.0.0.1',
        'PORT':'3306',
        
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# CACHES = {
#     # … default cache config and others
#     "select2": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/2",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }

# Tell select2 which cache configuration to use:
# SELECT2_CACHE_BACKEND = "select2"
# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ar'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# STATIC_URL = 'static/'
# django_heroku.settings(locals())
# STATIC_URL = '/static/'
# if DEBUG:
#     STATICFILES_DIRS = [
#         os.path.join(BASE_DIR, 'static')
#     ]
# else:
#     STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# LOCALE_PATHS = [
#     os.path.join(BASE_DIR, 'locale')
# ]
STATIC_ROOT = BASE_DIR / "staticfiles"

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# if DEBUG:
#     STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#     STATICFILES_DIRS = [
#         # os.path.join(BASE_DIR, 'staticfiles'),
#         os.path.join(BASE_DIR, 'staticfiles'),

#     ]
#     MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# else:
#     STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#     STATICFILES_DIRS = [
#         os.path.join(BASE_DIR, 'staticfiles'),
#     ]
#     MEDIA_ROOT = os.path.join(BASE_DIR, "media")

MEDIA_URL = "/media/"

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_DIRS = (str(BASE_DIR.joinpath('static')),)  # new
# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
# STATIC_ROOT = '/home/projects/site/assets/'
# STATICFILES_DIRS = (str(BASE_DIR.joinpath('static')),)
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# new
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # new
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'  # new
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'  # new


GOOGLE_MAPS_API_KEY = os.environ.get('AIzaSyATg_isuGSCHIlJamrxAXfkFDTYhIz7ytM')
# GEOPOSITION_GOOGLE_MAPS_API_KEY = 'AIzaSyDH4Y9rnt-Ui5FGTT5G1ivY2tlNFc9jr'

GEOPOSITION_GOOGLE_MAPS_API_KEY = 'AIzaSyATg_isuGSCHIlJamrxAXfkFDTYhIz7ytM'

USER_AGENTS_CACHE = 'default'
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }
X_FRAME_OPTIONS = 'ALLOWALL'

XS_SHARING_ALLOWED_METHODS = ['POST', 'GET', 'OPTIONS', 'PUT', 'DELETE']


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


X_FRAME_OPTIONS = 'ALLOWALL'

XS_SHARING_ALLOWED_METHODS = ['POST', 'GET', 'OPTIONS', 'PUT', 'DELETE']


LOGIN_REDIRECT_URL = "/"
CRISPY_TEMPLATE_PACK = 'bootstrap4'


XS_SHARING_ALLOWED_METHODS = ['POST', 'GET', 'OPTIONS', 'PUT', 'DELETE']
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap3"

CRISPY_TEMPLATE_PACK = "bootstrap4"
SELECT2_JS = "https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.12/js/select2.min.js"
SELECT2_CSS = "https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.12/css/select2.min.css"
SELECT2_I18N_PATH = "https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.12/js/i18n"

# SELECT2_JS = ['static/assets/js/select2.min.js']
# SELECT2_CSS = [
#     'static/assets/css/select2.css',
#     'static/assets/css/select2-theme.css',
# ]
# SELECT2_CACHE_BACKEND = "select2"

# SELECT2_I18N_PATH = 'assets/js/i18n'
# CACHES = {
#     # "default": {
#     #     "BACKEND": "django_redis.cache.RedisCache",
#     #     "LOCATION": "redis://127.0.0.1:6379/1",
#     #     "OPTIONS": {
#     #         "CLIENT_CLASS": "django_redis.client.DefaultClient",
#     #     }
#     # },
#     # 'select2': {
#     #     "BACKEND": "django_redis.cache.RedisCache",
#     #     "LOCATION": "redis://127.0.0.1:6379/2",
#     #     "OPTIONS": {
#     #         "CLIENT_CLASS": "django_redis.client.DefaultClient",
#     #     }
#     # },


# }

# Set the cache backend to select2
# SELECT2_CACHE_BACKEND = 'select2'
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
