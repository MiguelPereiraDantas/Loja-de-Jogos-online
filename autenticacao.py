INSTALLED_APPS = [
    # outros apps
    'rest_framework',
    'rest_framework_simplejwt',
    # outros apps
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # outras classes de autenticação
    ),
}