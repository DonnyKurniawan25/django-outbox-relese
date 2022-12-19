_Y='youtube'
_X='plain-text'
_W='extraPlugins'
_V='pasteFilter'
_U='toolbarCanCollapse'
_T='toolbar'
_S='bootstrap4'
_R='MEDIA_ROOT'
_Q='STATIC_ROOT'
_P='DB_NAME'
_O='DB_ENGINE'
_N='ENGINE'
_M='ALLOWED_HOSTS'
_L='SECRET_KEY'
_K='DB_PASSWORD'
_J='/id/dashboard/'
_I='key'
_H='secret'
_G='client_id'
_F='APP'
_E='default'
_D=False
_C='id'
_B='NAME'
_A=True
from pathlib import Path
import os
BASE_DIR=Path(__file__).resolve().parent.parent
from encryption import OutboxEncryption
lib=OutboxEncryption(BASE_DIR)
lib.set_keyword_local('django-outbox-dev')
lib.set_keyword_local('outbox')
lib.set_keyword_local('env_outbox')
lib.set_keyword_local('django_outbox_release_v2:3.8')
mplaint_key=[_K,_L]
mplaint_list=[_M]
key=lib.decrypt_environ(mplaint_key,mplaint_list)
if not key:raise Exception('No data found in environment, activate environment first!')
SECRET_KEY=key[_L]
DEBUG=key['DEBUG']
UNDER_CONSTRUCTION=key['UNDER_CONSTRUCTION']
ALLOWED_HOSTS=key[_M]
INSTALLED_APPS=['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','django.contrib.sites','django.contrib.humanize','core','education','region','menu','ckeditor','ckeditor_uploader','parler','hitcount','crispy_forms','corsheaders','allauth','allauth.account','allauth.socialaccount']
MIDDLEWARE=['django.middleware.security.SecurityMiddleware','django.contrib.sessions.middleware.SessionMiddleware','django.middleware.locale.LocaleMiddleware','corsheaders.middleware.CorsMiddleware','django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware','django.middleware.clickjacking.XFrameOptionsMiddleware','education.request_exposer.RequestExposerMiddleware','hitcount.request_exposer.RequestExposerMiddleware']
ROOT_URLCONF='django_outbox.urls'
TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[os.path.join(BASE_DIR,'templates')],'APP_DIRS':_A,'OPTIONS':{'context_processors':['django.template.context_processors.debug','django.template.context_processors.request','django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages','education.processor.context_outbox','backend.processor.context_outbox']}}]
WSGI_APPLICATION='django_outbox.wsgi.application'
DB_TYPE=key['DB_TYPE']
found=_D
if DB_TYPE:
	if DB_TYPE=='sqlite':found=_A;DATABASES={_E:{_N:key[_O],_B:key[_P]}}
if not found:DATABASES={_E:{_N:key[_O],_B:key[_P],'USER':key['DB_USER'],'PASSWORD':key[_K],'HOST':key['DB_HOST'],'PORT':key['DB_PORT']}}
AUTH_PASSWORD_VALIDATORS=[{_B:'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},{_B:'django.contrib.auth.password_validation.MinimumLengthValidator'},{_B:'django.contrib.auth.password_validation.CommonPasswordValidator'},{_B:'django.contrib.auth.password_validation.NumericPasswordValidator'}]
LANGUAGE_CODE=_C
TIME_ZONE='Asia/Makassar'
USE_I18N=_A
USE_L10N=_A
USE_TZ=_D
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
STATIC_URL='/static/'
tmp=key.get(_Q)
STATIC_ROOT=key[_Q]if tmp else os.path.join(BASE_DIR,'staticfiles')
STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]
MEDIA_URL='/media/'
tmp=key.get(_R)
MEDIA_ROOT=key[_R]if tmp else os.path.join(BASE_DIR,'media')
SITE_ID=1
LOGIN_REDIRECT_URL=_J
LOGOUT_REDIRECT_URL=_J
IMPORT_EXPORT_USE_TRANSACTIONS=_A
EMAIL_BACKEND='django.core.mail.backends.filebased.EmailBackend'
AUTH_USER_MODEL='core.User'
EMAIL_USE_TLS=_A
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER='auto.email.activation@gmail.com'
EMAIL_PORT=587
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS=1
ACCOUNT_EMAIL_REQUIRED=_A
ACCOUNT_LOGIN_ATTEMPTS_LIMIT=5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT=86400
ACCOUNT_LOGOUT_REDIRECT_URL='/id/accounts/login/'
ACCOUNT_LOGIN_REDIRECT_URL=_J
ACCOUNT_AUTHENTICATION_METHOD='email'
ACCOUNT_UNIQUE_EMAIL=_A
ACCOUNT_USER_MODEL_USERNAME_FIELD=None
ACCOUNT_USERNAME_REQUIRED=_D
ACCOUNT_LOGOUT_ON_GET=_A
CRISPY_TEMPLATE_PACK=_S
CKEDITOR_UPLOAD_PATH='uploads/'
CKEDITOR_BASEPATH='/static/ckeditor/ckeditor/'
CKEDITOR_RESTRICT_BY_USER=_A
CKEDITOR_CONFIGS={_E:{'width':'100%',_T:'full',_U:_A,_V:_X,'removePlugins':('exportpdf','scayt'),_W:','.join(['texttransform','html5audio','html5video','wordcount',_Y,'embedsemantic','autolink','codesnippet','previewgoogledrive','previewdocument'])},'embed_video':{_W:','.join([_Y]),_U:_A,_V:_X,_T:'Custom','toolbar_Custom':[['Source','Iframe'],['Youtube']]}}
SOCIALACCOUNT_PROVIDERS={'github':{_F:{_G:'85c0e07e059b13f51fa7',_H:'864b498f57989b0c9673d4c26ece9639da235799',_I:''}},'facebook':{_F:{_G:'1599138133769755',_H:'fce558238cc11cfb1e321e24dbdb808a',_I:''}},'instagram':{_F:{_G:'1661150634264663',_H:'d230d65cf872859e0b9c57d07491ed84',_I:''}},'google':{_F:{_G:'52853440607-t3jdk23e1ku0ic77r4fgkekgr7vpd75b.apps.googleusercontent.com',_H:'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',_I:''}}}
from django.utils.translation import gettext_lazy as _
LANGUAGES=(_C,_('Indonesia')),('en',_('English'))
LOCALE_PATHS=[os.path.join(BASE_DIR,'locale')]
PARLER_DEFAULT_LANGUAGE_CODE=_C
PARLER_LANGUAGES={1:({'code':_C},{'code':'en'}),_E:{'fallbacks':[_C],'hide_untranslated':_D}}
CRISPY_TEMPLATE_PACK=_S
HITCOUNT_KEEP_HIT_IN_DATABASE={'months':3}
HITCOUNT_KEEP_HIT_ACTIVE={'hours':1}
AUTHENTICATION_BACKENDS=['allauth.account.auth_backends.AuthenticationBackend']