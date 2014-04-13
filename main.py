#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import random
from google.appengine.ext.webapp import template
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # self.response.write('Hello world!')
        temp = os.path.join(os.path.dirname(__file__), 'templates/index.html')
        outstr = template.render(temp, {'resp': 'Buena Suerte'})
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(outstr)

    def post(self):
        estimacion = self.request.get('resp')
        msg = ''
        resp = -1
        try:
            resp = int(estimacion)
        except:
            resp = -1
        answer = random.randint(1, 100)
        if resp < answer:
            msg = 'Tu numero es demasiado bajo'
        if resp is answer:
            msg = 'Has acertado campeon, toma un pin!'
        if resp > answer:
            msg = 'Tu numero es demasiado alto'
        temp = os.path.join(os.path.dirname(__file__), 'templates/estimacion.html')
        outstr = template.render( temp, {'real': msg, 'estimacion': estimacion})
        self.response.out.write(outstr)
app = webapp2.WSGIApplication([('/index.html', MainHandler)], debug=True)