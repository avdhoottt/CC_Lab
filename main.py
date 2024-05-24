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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<h1>Welcome to My Web App!</h1>'
                            '<p><a href="/about">About</a></p>'
                            '<p><a href="/contact">Contact</a></p>')

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<h1>About Page</h1>'
                            '<p>This is a simple web app using Google App Engine.</p>'
                            '<p><a href="/">Home</a></p>'
                            '<p><a href="/contact">Contact</a></p>')

class ContactHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<h1>Contact Page</h1>'
                            '<p>Feel free to reach out to us at contact@mywebapp.com.</p>'
                            '<p><a href="/">Home</a></p>'
                            '<p><a href="/about">About</a></p>')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/about', AboutHandler),
    ('/contact', ContactHandler)
], debug=True)

#  import webapp2
#  class MainHandler(webapp2.RequestHandler):
#      def get(self):
#           self.response.write("Hello World")
# app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)
# 
# app.yml 
# runtime: python27
# api_version: 1
# threadsafe: False

# handlers:
# - url: /
#   script: test.app




