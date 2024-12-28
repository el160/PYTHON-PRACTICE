# Django has no built in library for serving static files in production when DEBUG is set to False.
# WhiteNoise is a simple solution for serving static files in production.
# we start by installing WhiteNoise using in the virtual environment
# pip install whitenoise
# then we add WhiteNoise to the middleware classes in the settings.py file
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',
# ]