#!/usr/bin/env python3
import connexion
from misc import check_settings

check_settings.check_all()
app = connexion.FlaskApp('config-worker')
app.add_api('api/spec.yaml',
            arguments={'title': 'MT-WAN config-worker'})
# start werkzeug server instead of "$ uwsgi uwsgi.ini"
#app.run() 
