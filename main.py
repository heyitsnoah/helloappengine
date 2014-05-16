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
import webapp2
import os
import logging

from google.appengine.ext.webapp import template
from model import Name

class PostHandler(webapp2.RequestHandler):
    # GET and POST are HTTP commands. 
    # They define whether we're just retrieving info or adding to database.
    def get(self):
        # Here we call the database. We are pulling all names out.
        names = Name.all()
        template_values = {"names":names} 
        path = os.path.join(os.path.dirname(__file__), 'templates/post.html')
        self.response.out.write(template.render(path, template_values))
    def post(self):
        # This grabs the post value called name that was passed.
        name = self.request.get('name')
        if name:
            # Here we create a new Name object in the database.
            # We assign the name field with the new name that was passed on in the POST.
            new_name = Name(name=name)
            # And here we save it to the database.
            new_name.put()
        # Finally, we redirect back to the original page (GET).
        self.redirect('/post')

class GetHandler(webapp2.RequestHandler):
    def get(self):
        # Check the query string to see if there is a variable called 'name'.
        name = self.request.get('name')
        # Pass name value to template.
        template_values = {"name":name}
        path = os.path.join(os.path.dirname(__file__), 'templates/get.html')
        self.response.out.write(template.render(path, template_values))

class MathHandler(webapp2.RequestHandler):
    def get(self):
        gold = 1294
        if self.request.get('dollars'):
            dollars = int(self.request.get('dollars'))
            pounds_of_gold = dollars / gold
            template_values = {"dollars":dollars,"pounds_of_gold":pounds_of_gold,"gold":gold}
        else:
            template_values = {"gold":gold}
        path = os.path.join(os.path.dirname(__file__), 'templates/math.html')
        self.response.out.write(template.render(path, template_values)) 

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<p>Hello world!</p>')
        self.response.write('<p><a href="/get">GET!</a></p>')
        self.response.write('<p><a href="/post">POST!</a></p>')
        self.response.write('<p><a href="/math">MATH!</a></p>')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/get',GetHandler),
    ('/post',PostHandler),
    ('/math',MathHandler)
], debug=True)
