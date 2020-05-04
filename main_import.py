# coding: utf-8
"""
main programm to
- create database
- import data from api and insertion in database
"""
from importdata import create_db
from importdata import import_api

# create database
create_db.main()

# import data from api
import_api.main()
