from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

import parser11
import parser22

import setup
#import export_tests
import generate_tests22
import pdf
#import import_test

import webbrowser

@app.route("/")
def main():
	print("i am in main")
	return render_template('index.html')

@app.route('/', methods=['POST'])
def main_post():		##BRAK PEVIEW!!!!!!
	file = request.files['file']
	if file:
		b = file.read()
		b=str(b,'utf-8')
		#print(b)
		a,title,date,description = parser11.parse(b)
		#print (a)

		#with( open('my_new_file.txt') ) as g:
		#	a = g.read()
		#print(a)
		#g.write(xd)

		#return render_template('index.html',entries='22222')
		
		number_of_line = parser22.check_errors(a)
		#print(number_of_line)

		if number_of_line:
			return render_template('index.html',entries=[str(number_of_line)])

		temp_q, temp_a, temp_i = parser22.prepare_to_parse(a)
		categories,groups,questions,answers = parser22.parse(temp_q,temp_a)
		
		#print(temp_i)
		img = list()
		for i in range(0,len(temp_i)):
			img.append(temp_i[i])
		session['categories'] = categories
		session['groups'] = groups
		session['questions'] = questions
		session['answers'] = answers
		session['images'] = img
		session['date'] = date
		session['title'] = title
		session['description'] = description
		#print(session['images'])


		return redirect(url_for('categories'))
	else:
		return render_template('index.html')


@app.route("/categories")
def categories():
	categories2 = session['categories']
	#print('i am in categories')
	for i in range(0,len(categories2)):
		categories2[i] = str(categories2[i])+'('+str(len(session['groups'][i]))+')'
	return render_template('index2.html', entries = categories2)

@app.route("/categories", methods=['POST'])
def categories_post():
	session['questionNumbers'] = request.form['text2']
	
	a = session['questionNumbers']
	a=a.split(',')
	suma = 0;
	if not a[len(a)-1]:
		a.pop()

	if len(a) is not len(session['categories']):
		categories3 = list()
		for word in session['categories']:
			categories3.append(word)
		for i in range(0,len(categories3)):
			categories3[i] = str(categories3[i])+'('+str(len(session['groups'][i]))+')'
		return render_template('index2.html', entries = categories3)

	for i in range(0,len(a)):
		if not setup.RepresentsInt(a[i]):
			categories3 = list()
			for word in session['categories']:
				categories3.append(word)
			for i in range(0,len(categories3)):
				categories3[i] = str(categories3[i])+'('+str(len(session['groups'][i]))+')'
			return render_template('index2.html', entries = categories3)

	for i in range(0,len(a)):
		if int(a[i]) > int(len(session['groups'][i])):
			categories3 = list()
			for word in session['categories']:
				categories3.append(word)
			for i in range(0,len(categories3)):
				categories3[i] = str(categories3[i])+'('+str(len(session['groups'][i]))+')'
			return render_template('index2.html', entries = categories3)

	for i in range (0,len(a)):
		suma += int(a[i])
	if suma > 20:
		categories3 = list()
		for word in session['categories']:
			categories3.append(word)
		for i in range(0,len(categories3)):
			categories3[i] = str(categories3[i])+'('+str(len(session['groups'][i]))+')'
		return render_template('index2.html', entries = categories3)

	session['questionNumbers'] = a
	#print (a)
	#print (session['questionNumbers'])
	
	return redirect(url_for('test'))


@app.route("/test")
def test():
	return render_template('special.html')

@app.route('/test', methods=['POST'])
def test_post():
	session['testSpecifications'] = request.form["text5"]

	#questionNumbers = session['questionNumbers'].split(',')
	
	if not setup.RepresentsInt(session['testSpecifications']):
		return render_template('special.html')

	print(session['testSpecifications'])

	listOfTests=list()
	for i in range(0,int(session['testSpecifications'])):
		q,a,c,i = generate_tests22.generate(session['categories'], session['groups'], session['questions'],
							session['answers'],session['questionNumbers'],session['testSpecifications'],session['images'])
		listOfTests.append([q,a,c,i])

	#print(listOfTests)
	import os
	if not os.path.isdir('myTest'):
		os.makedirs('myTest')
	
	path = os.path.join(os.getcwd(),'myTest','group')
	pdf.go(listOfTests,path,session['title'])
	pdf.go0(listOfTests,path,session['title'])
	for i in range(0,len(listOfTests)):
		pdf.go2(listOfTests,path,session['title'],i,session['date'],session['description'])





	return "test was created"







if __name__ == "__main__":
	webbrowser.open('http://localhost:5000')
	app.run()