#!/usr/bin/python
# Encoding: UTF-8

from flask import Flask, request, render_template
app = Flask(__name__)

import pacparser

import sys
import os
import subprocess
import urllib, urllib2

from yoururls import defurls
from yourpacs import defpacs

@app.route('/')
def hello():
	return render_template('index.html',defpacs=defpacs)

@app.route('/pac',methods=['GET', 'POST'])
def pac():

	if request.method == 'GET':
		# get args
		url=request.args.get('url')
		url=urllib2.unquote(url)
		opt=request.args.get('opt')

		# get pac file immidiately
		try:
			print
#			cmd1="wget -O latest.pac " + opt  # changed to urllib coz didn't get exception
#			ret=os.system(cmd1)
#			print(ret)
			urllib.urlretrieve(opt, filename="latest.pac")

			# get pac's modified date
			ps = subprocess.Popen(('stat', "latest.pac"), stdout=subprocess.PIPE)
			stat = subprocess.check_output(('grep', 'Modif'), stdin=ps.stdout)
			print("stat->")
			print(stat)

		except Exception,e:
			# When couldn't download pac, return error page.
			error = "Pac file not found. Check your pac in `/app/yourpac.py` and correct access rights."
			return render_template('index.html',defpacs=defpacs, error=error)

	else:
		url="http://example.com/"
		opt="http://your-company/test.pac"

	# get pacparser response
	pacparser.init()

	try:
		res = pacparser.just_find_proxy("latest.pac", url)
	except:
		res = "not found"
	finally:
		print
		print(res)
		print

	pacparser.cleanup()

	# get defined check urls
	defres = getDefinedUrlResults()

	return render_template('index.html',url=url,opt=opt,res=res,stat=stat,defpacs=defpacs,defres=defres)


def getDefinedUrlResults():
	print("getDefinedUrlResults ->")

	pacparser.init()
	ret = []

	# get pacparser response
	for url in defurls:
		# print(url)
		try:
				res = pacparser.just_find_proxy("latest.pac", url)
		except:
				res = "pac file not found"
		finally:
				print
				# print(res)
				# print
		ret.append({ "url": url, "res": res })
	print("end for defurls <-")

	pacparser.cleanup()

	# print(ret)
	print("getDefinedUrlResults <-")
	return ret



if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True, port=80)

