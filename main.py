#!/usr/bin/env python

import webapp2
#from functions.py import *
form =  
'''
			<form method="post">
            Enter your birthday <br/>
            <label>
            Day
				<input type="text" name="day">
            </label>
            <label>
            Month
                <input type="text" name="month">
            </label>
            <label>
            Year
                <input type="text" name="year">
			</label>
            	<input type="submit">
			</form>
'''
months =['January','February','March']  

def valid_day(day):
    if (day and day.isdigit()):
        day = int(day)
        if day > 0 and day <=31:
            return day

def valid_month(month):
    if month:
        month = month.capitalize()
        if (month in months):
            return month

def valid_year(year):
    if (year and year.isdigit()):
        year = int(year)
        if (year > 1900 and year <=2016):
            return year

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)
    
    

    def post(self):
        month = valid_month(self.request.get('month'))
        day = valid_month(self.request.get('day'))
        year = valid_month(self.request.get('year'))

        if not(month and year and day):
            self.response.out.write(form)
        else:
            self.response.out.write("Thanks for entering the information")    
           
    


class TestHandler(webapp2.RequestHandler):
    def post(self):
        #self.response.write(form)
        #self.response.headers['Content-Type']= 'text/plain'
        #self.response.out.write(self.request)

        username = self.request.get("username")
        self.response.out.write("<h1>"+username+"</h1>")


app = webapp2.WSGIApplication([
    ('/', MainHandler),('/confirmation',TestHandler)
], debug=True)


