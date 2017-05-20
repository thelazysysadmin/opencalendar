from flask import Flask, url_for

class Services:

    app = Flask(__name__)

    def getcalanders(self):

        calanders = [

        {
        'cal_id': 1,
        'title': u'Home',
        'description': u'none',
        'cdate': u'date',
        'ctime':u'time',
        'author': u'author'
        },

        {
        'cal_id': 2,
        'title': u'Work',
        'description': u'none',
        'cdate': u'date',
        'ctime':u'time',
        'author': u'author'
        }
        ]

        return calanders

    def public_calander(self, calanders):
        new_public_calander = {}
        for field in calanders:
            if field == ['cal_id']:
                new_public_calander['uri'] = url_for('get_calanders', cal_id=calanders['cal_id'], _external=True)
            else:
                new_public_calander[field] = calanders[field]
            return new_public_calander
