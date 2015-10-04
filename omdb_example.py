#!/usr/bin/env python

# OMDb API
# Author: Md. Minhazul Haque
# URL: https://minhazulhaque.com

import json
import requests
import re

url = 'http://www.omdbapi.com/'
movie_list = 'movies.txt'

with open(movie_list) as file:
    for line in file.readlines():
        line = line.strip()
        
        #debug
        #if re.findall("^.*\(.*\)$", line):
            #pass
        #else:
            #print line
        #continue
        
        movie_name = line[:-7]
        movie_year = line[-6:].replace("(", "").replace(")", "")
        movie_year_i = int(movie_year)
        
        if movie_year_i > 1900 and movie_year_i < 2100:
            params = dict(t=movie_name, y=movie_year)
            resp = requests.get(url=url, params=params)
            data = json.loads(resp.text)
            
            if data['Response'] == 'True':
                print movie_name,"|",data['Genre']
            else:
                print movie_name,"| Unknown"
