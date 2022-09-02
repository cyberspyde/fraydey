from waitress import serve

from MarketingNotes.wsgi import application
# documentation: https://docs.pylonsproject.org/projects/waitress/en/stable/api.html

serve(application, host = 'localhost', port='80')
