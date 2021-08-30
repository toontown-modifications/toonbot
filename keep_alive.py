#***************************************************************************#
#                                                                           #
# TVS Bot - A Discord Bot For Our School.                                   #
# https://github.com/NoraHanegan/TVSBot                                     #
# Copyright (C) 2021 Nora Hanegan. All rights reserved.                     #
#                                                                           #
# License:                                                                  #
# MIT License https://www.mit.edu/~amini/LICENSE.md                         #
#                                                                           #
#***************************************************************************#

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "I am not dead."

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()
