#
# import httplib
# import json
#
# data = '{"source_blob": {"url": "https://github.com/keithsktang/herokuDeployment/archive/master.tar.gz", "version": "3d24155a7bc99be4962a48faa3a4c1906be9f2d9"}}'
# headers = {"Accept": "application/vnd.heroku+json; version=3",
#           "Content-Type": "application/json",
#           "Authorization": "Bearer 05094439-e12b-4997-bf7f-eb6f44bb1d5f"}
# conn = httplib.HTTPSConnection('api.heroku.com')
# conn.request("POST", '/apps/pure-beach-57030/builds', data, headers)
# response = conn.getresponse()
# print response.read()
# conn.close()
