import os
import django.conf.global_settings as DEFAULT_SETTINGS


# here() gives us file paths from the root of the system to the directory
# holding the current file.
TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'auth.processor.current_user',
    'auth.processor.mkmonth_lst',
    'django.core.context_processors.request',
)



here = lambda * x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

PROJECT_ROOT = here("..")
# root() gives us file paths from the root of the system to whatever
# folder(s) we pass it starting at the parent directory of the current file.
root = lambda * x: os.path.join(os.path.abspath(PROJECT_ROOT), *x)


# Django settings for blog_project project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS


SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Calcutta'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"

MEDIA_ROOT = here("../..", "static")


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''
ADMIN_MEDIA_PREFIX = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.

    ('' ,  here("../..", "static")),

   
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


TINYMCE_JS_ROOT =  os.path.join(MEDIA_ROOT, "/js/tiny_mce/")
TINYMCE_JS_URL = os.path.join(MEDIA_ROOT, "/js/tiny_mce/utils.js")
#TINYMCE_JS_URL = here("../..", "static/js/tiny_mce/tiny_mce_src.js")
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
}
TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True


# Make this unique, and don't share it with anybody.
SECRET_KEY = 'blx1ppeqn%5&^xj&5h-7yu8-9!p&t$(q+twp_*j-##i=73-n#9'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'blog_project.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'blog_project.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    here("../..", "templates"),
)

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'suit',
    'django.contrib.admin',
    'haystack',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

CUSTOM_APPS = (
    # Apps that we create
    'blog',
    'news',
    'homepage',
    'auth',
    'contact_us'
)

THIRD_PARTY_APPS = (
    # Third Party Django Apps
    'tinymce',
    'django_extensions',
    'sorl.thumbnail',
    'newsletter',
    'imagefit',
)


INSTALLED_APPS = DJANGO_APPS + CUSTOM_APPS + THIRD_PARTY_APPS

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
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


# Newsletter Setting

# Email subscription confirmation setting
# NEWSLETTER_CONFIRM_EMAIL = False
# NEWSLETTER_CONFIRM_EMAIL_SUBSCRIBE = True
# NEWSLETTER_CONFIRM_EMAIL_UNSUBSCRIBE = True
# NEWSLETTER_CONFIRM_EMAIL_UPDATE = True


THUMBNAIL_DEBUG = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)


IMAGEFIT_ROOT = here("../../static/")




SUIT_CONFIG = {
    'ADMIN_NAME': 'MOOCS Magazine',
    'MENU': (

       

        # Rename app and set icon
        {'app': 'blog', 'label': 'Blog', 'icon':'icon-chevron-right'},

        {'app': 'news', 'label': 'News', 'icon':'icon-bullhorn'},
        # Separator
        '-',

        # Custom app, with models
        {'app': 'homepage', 'label': 'Newsletter Subscribers', 'icon':'icon-chevron-right'},
        # Separator
        '-',
        'auth',

        'sites',
        # Separator
        '-',
    )
}

