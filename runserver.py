from waitress import serve

from MarketingNotes.wsgi import application
# documentation: https://docs.pylonsproject.org/projects/waitress/en/stable/api.html

# Change port here (default: 8080, production was: 80)
serve(application, host = 'localhost', port='8080')
