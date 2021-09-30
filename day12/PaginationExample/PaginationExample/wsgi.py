"""
WSGI config for PaginationExample project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
#import sys

#import django
from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PaginationExample.settings')

application = get_wsgi_application()



#import signal
#def my_signal_handler(sig, frame):
#signal.signal(signal.SIGINT, my_signal_handler)
#print('Press Ctrl+C')
#signal.pause()



#my_django_shutdown_signal = django.dispatch.Signal()


#def _forward_to_django_shutdown_signal(signal, frame):
#    my_django_shutdown_signal.send('system')
#    sys.exit(0)   # So runserver does try to exit
#signal.signal(signal.SIGINT, _forward_to_django_shutdown_signal)
