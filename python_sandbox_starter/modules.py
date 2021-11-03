# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# core modules
import datetime
import time
from datetime import date
from time import time

# pip module
from camelcase import CamelCase

# import user module
from validator import validate_email

today = datetime.date.today()
today = date.today()
# timestamp = time.time()
timestamp = time()

c = CamelCase()
print(today)
print(c.hump("time " + str(timestamp)))
print(("email invalid", "email valid")[bool(validate_email("gab@wp.pl"))])
