import os
import pathlib

import django.utils.translation
import dotenv

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
dotenv_path = BASE_DIR.joinpath("lyceum/example.env")
dotenv.load_dotenv(dotenv_path=dotenv_path)

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", default="very_secret_data")

DEBUG = os.environ.get("DJANGO_DEBUG", default="false").lower() in {
    "true",
    "yes",
    "on",
    "1",
    "y",
}

ALLOW_REVERSE = os.environ.get(
    "DJANGO_ALLOW_REVERSE",
    default="true",
).lower() in {
    "true",
    "yes",
    "on",
    "1",
    "y",
    "",
}
DJANGO_MAIL = os.environ.get("DJANGO_MAIL", "example@email.com")

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "*").split(",")

INSTALLED_APPS = [
    "about.apps.AboutConfig",
    "catalog.apps.CatalogConfig",
    "download.apps.DownloadConfig",
    "homepage.apps.HomepageConfig",
    "feedback.apps.FeedbackConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_cleanup.apps.CleanupConfig",
    "sorl.thumbnail",
    "tinymce",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "lyceum.middleware.MyMiddleware",
]
if DEBUG:
    MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")
    INSTALLED_APPS.append("debug_toolbar")

INTERNAL_IPS = ["127.0.0.1"]

ROOT_URLCONF = "lyceum.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "lyceum.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static_dev",
]
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"
DOWNLOAD_URL = "/download/"

CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"

CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "full",
        "height": 300,
        "width": 300,
    },
}
LANGUAGES = (
    (
        "en",
        django.utils.translation.gettext_lazy("English"),
    ),
    (
        "ru",
        django.utils.translation.gettext_lazy("Русский"),
    ),
    (
        "de",
        django.utils.translation.gettext_lazy("Deutsch"),
    ),
    (
        "es",
        django.utils.translation.gettext_lazy("Espanol"),
    ),
)

LOCALE_PATHS = [
    BASE_DIR / "locale",
]

EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"

EMAIL_FILE_PATH = BASE_DIR / "send_mail"

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

EMAIL_HOST = DJANGO_MAIL
