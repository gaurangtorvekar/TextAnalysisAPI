import os
SETTINGS_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')
STATIC_PATH = os.path.join(PROJECT_PATH, 'text_analysis_api/static')
DATABASE_PATH = os.path.join(PROJECT_PATH, 'brands.db')
STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#ly)cq4nb+9^6w*25l4g=t7p#qgr8y^r7$^j2a@4%lpp+5%2i+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'brand_profiles',
    'rest_framework',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'text_analysis_api.urls'

WSGI_APPLICATION = 'text_analysis_api.wsgi.application'

TEMPLATE_DIRS = (
    TEMPLATE_PATH,
)

STATICFILES_DIRS = (
    STATIC_PATH,
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASE_PATH,
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGINATE_BY': 10
}

# ======= Configuration for Heroku =============
# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/1.7/howto/static-files/

# STATIC_URL = '/static/'

# # Parse database configuration from $DATABASE_URL
# import dj_database_url
# DATABASES['default'] =  dj_database_url.config()

# # # Honor the 'X-Forwarded-Proto' header for request.is_secure()
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# # # Allow all host headers
# ALLOWED_HOSTS = ['*']

# # # Static asset configuration
# import os
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# STATIC_ROOT = 'staticfiles'
# STATIC_URL = '/static/'

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )