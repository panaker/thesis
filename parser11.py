
import os

import struct
import imghdr

def get_image_size(fname):
    '''Determine the image type of fhandle and return its size.
    from draco'''
    with open(fname, 'rb') as fhandle:
        head = fhandle.read(24)
        if len(head) != 24:
            return
        if imghdr.what(fname) == 'png':
            check = struct.unpack('>i', head[4:8])[0]
            if check != 0x0d0a1a0a:
                return
            width, height = struct.unpack('>ii', head[16:24])
        elif imghdr.what(fname) == 'gif':
            width, height = struct.unpack('<HH', head[6:10])
        elif imghdr.what(fname) == 'jpeg':
            try:
                fhandle.seek(0) # Read 0xff next
                size = 2
                ftype = 0
                while not 0xc0 <= ftype <= 0xcf:
                    fhandle.seek(size, 1)
                    byte = fhandle.read(1)
                    while ord(byte) == 0xff:
                        byte = fhandle.read(1)
                    ftype = ord(byte)
                    size = struct.unpack('>H', fhandle.read(2))[0] - 2
                # We are at a SOFn block
                fhandle.seek(1, 1)  # Skip `precision' byte.
                height, width = struct.unpack('>HH', fhandle.read(4))
            except Exception: #IGNORE:W0703
                return
        else:
            return
        return width, height


#print(t)

xd = ''

flaga_odpowiedzi = 0;

categories = list()
groups = list()
answers = list()

category = ''
category_old = ''
group = ''
group_old = ''
question = ''
answer = ''

def parse(t):

	print(os.getcwd())

	#print(len(t))

	#print('na wejscie')
	#print(t)

	t = str.replace(t, '\r\n', '\n');

	xd = ''

	flaga_odpowiedzi = 0;

	categories = list()
	groups = list()
	answers = list()

	category = ''
	category_old = ''
	group = ''
	group_old = ''
	question = ''
	answer = ''

	i = 0
	#for i in range(0,len(t)):
	flag = 0;
	tempor = ''
	date = ''
	description = ''
	while flag != 1:
		while t[i] != '[':
			i+=1
		i+=1
		while t[i]!= ']':
			tempor += t[i]
			i+=1
		title = tempor
		tempor = ''
		while t[i] != '[':
			i+=1
		i+=1
		while t[i]!= ']':
			tempor += t[i]
			i+=1
		date = tempor
		tempor = ''
		while t[i] != '[':
			i+=1
		i+=1
		while t[i]!= ']':
			tempor += t[i]
			i+=1
		description = tempor;
		flag = 1




	while i is not len(t)-1:

		if i==len(t)-1:
			break

		elif i == len(t)-2:
			if t[i+1] is '@':
				break

		elif t[i] is '@' and t[i+1] is 'C':
			print("C")
			print(os.getcwd())
			if category and group and question:
				xd+='['+category+']['+group+']['+question+']'
				for j in images:
					xd+='['+j+']'
				xd+='\n'
				for k in answers:
					xd+='['+k+']'
				xd+='\n'
				print(xd)
			group = ''
			question = ''
			images = list()
			answers = list()

			i+=2
			while t[i] is not '[':
				i+=1
			category = ''
			i+=1
			while t[i] is not ']':
				if t[i] is '\n':
					i+=1
				elif t[i] is '\t':
					i+=1
				else:
					category += t[i]
					i+=1
			categories.append(category)
			#print(i)
			#i+=1

		elif t[i] is '@' and t[i+1] is 'T':

			print("T")
			if category and group and question:
				xd+='['+category+']['+group+']['+question+']'
				for j in images:
					xd+='['+j+']'
				xd+='\n'
				for k in answers:
					xd+='['+k+']'
				xd+='\n'
				print(xd)
			
			question = ''
			images = list()
			answers = list()

			
			if category:
				i+=2
				while t[i] is not '[':
					i+=1
				group = ''
				i+=1
				while t[i] is not ']':
					if t[i] is '\n':
						i+=1
					elif t[i] is '\t':
						i+=1
					else:
						group += t[i]
						i+=1
			#print(i)
			#i+=1

		elif t[i] is '@' and t[i+1] is 'Q':
			print("Q")

			if question:
				#print(question)
				xd+='['+category+']['+group+']['+question+']'
				for j in images:
					xd+='['+j+']'
				xd+='\n'
				for k in answers:
					xd+='['+k+']'
				xd+='\n'
				#print(question)
				#print(xd)
			images = list()
			answers = list()


			if category and group:	

				i+=2
				while t[i] is not '[':
					i+=1
				question = ''
				i+=1
				while t[i] is not ']':
					if t[i] is '\n':
						i+=1
					elif t[i] is '\t':
						i+=1
					else:
						question += t[i]
						i+=1

				#print(question)
			#print(i)
		
		elif t[i] is '@' and t[i+1] is 'I':
			print("I")
			imageSizes = list()
			if category and group and question:
				i+=2
				images = list()
				while t[i] is not '@':
					image = ''
					if t[i] is '[':
						i+=1
						while t[i] is not ']':
							if t[i] is '\n':
								i+=1
							elif t[i] is '\t':
								i+=1
							else:
								image += t[i]
								i+=1
						image = os.path.join(os.path.dirname(os.path.abspath(__file__)),"images",image)
						images.append(image)
						w,h = get_image_size(image)
						#print(w)
						imageSizes.append(h)
						i+=1
					else:
						i+=1

			if question.count('@img') < len(imageSizes):
				imageSizes.pop()
			while(True):
				if question.find('@img') != -1:
					w,h = get_image_size(images[0])
					if h == max(imageSizes):
						question = question.replace('@img','<img src="'+images[0]+'" valign="top" height="'+str(h)+'"/>',1)
					else:
						question = question.replace('@img','<img src="'+images[0]+'" valign="top"/>',1)
					images.pop(0)
				else:
					break



			#print(images)
			#print(i)
		
		elif t[i] is '@' and t[i+1] is 'A':
			print("A")
			if category and group and question:
				i+=2
				tempImg = list()
				tempImgSize = list()
				flag = 0;
				answer = ''
				while t[i] is not '@':
					
					ima = ''
					if t[i] is '[' and flag==0:
						i+=1
						while t[i] is not ']':
							if t[i] is '\n':
								i+=1
							elif t[i] is '\t':
								i+=1
							else:
								answer += t[i]
								i+=1
						#answers.append(answer)
						flag = 1
						i+=1
					elif t[i] is '[' and flag==1:
						i+=1
						while t[i] is not ']':
							if t[i] is '\n':
								i+=1
							elif t[i] is '\t':
								i+=1
							else:
								ima += t[i]
								i+=1
						ima = os.path.join(os.path.dirname(os.path.abspath(__file__)),"images",ima)
						tempImg.append(ima)
						w,h = get_image_size(ima)
						#print(w)
						tempImgSize.append(h)
						flag = 1
						i+=1
					else:
						i+=1



				while(True):
					if answer.find('@img') != -1:
						w,h = get_image_size(tempImg[0])
						if h == max(tempImgSize):
							answer = answer.replace('@img','<img src="'+tempImg[0]+'" valign="top" height="'+str(h)+'"/>',1)
						else:
							answer = answer.replace('@img','<img src="'+tempImg[0]+'" valign="top"/>',1)
						tempImg.pop(0)
					else:
						break
				answers.append(answer)
				print(t[i])

		else:
			i+=1



	xd+='['+category+']['+group+']['+question+']'
	for j in images:
		xd+='['+j+']'
	xd+='\n'
	for k in answers:
		xd+='['+k+']'
	xd+='\n'

	#print(xd)
	#with( open('my_new_file.txt','w') ) as g:
	#	g.write(xd)
			
	return xd, title, date, description



#if __name__ == '__main__':
#	f = open('_corrupted_file.txt')
#	t = f.read()
#	print (t)



#	xd = parse(t)
#	print(xd)

#	g = open('my_new_file.txt','w')
#	g.write(xd)




		


