#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:12:01 2020

@author: tysun
"""

  
from flask import Flask
from flask_restful import Resource, Api
import AI


app = Flask(__name__)
api = Api(app)


class AI(Resource):
    def get(self):
        return AI.AI_analysis()
    
api.add_resource(AI,'/')    
    
if __name__ == '__main__':
    app.run(debug=True)
    
    