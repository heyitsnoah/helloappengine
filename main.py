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
from google.appengine.ext.webapp import template
from model import Name

class PostHandler(webapp2.RequestHandler):
    def get(self):
        names = Name.all()
        template_values = {"names":names} 
        path = os.path.join(os.path.dirname(__file__), 'templates/post.html')
        self.response.out.write(template.render(path, template_values))
    def post(self):
        name = self.request.get('name')
        if name:
            new_name = Name(name=name)
            new_name.put()
        self.redirect('/post')

class GetHandler(webapp2.RequestHandler):
    def get(self):
        name = self.request.get('name')
        template_values = {"name":name}
        path = os.path.join(os.path.dirname(__file__), 'templates/get.html')
        self.response.out.write(template.render(path, template_values))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/get',GetHandler),
    ('/post',PostHandler)
], debug=True)
