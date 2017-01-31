def check_errors(t_string):

	#print(t_string)
	temp_str = t_string

	temp_q=list()
	temp_a=list()

	temp_str=temp_str.strip()
	temp_str=temp_str.split('\n')
	for i in range (0,len(temp_str)):
		temp_str[i]=temp_str[i].strip()
		temp_str[i]=temp_str[i].split(']')
		if len(temp_str[i])==5:
			temp_str[i].pop()

	for i in range (0,len(temp_str)):
		if len(temp_str[i]) is not 4:
			print('a')
			return i+1

	for i in range (0,len(temp_str)):
		if not i%2: #question
			if len(temp_str[i])>5:
				print("b")
				return i+1
			if temp_str[i][len(temp_str[i])-1]:
				import os
				if not os.path.exists(os.path.join(os.getcwd(),temp_str[i][len(temp_str[i])-1][1:])):
					print (temp_str[i][len(temp_str[i])-1][1:])
					print('c)')
					return i+1
		else:
			if len(temp_str[i]) is not 4:
				print('d')
				return i+1


	temp_list_ans=list()
	for i in range(0,int(len(temp_str)/2)):
		temp_q.append(temp_str[i*2])
		if temp_q[i][0][0]=='[':
			temp_q[i][0]=temp_q[i][0][1:]
		else:
			print("ERROR1 in "+str(i*2+1)+"line")
			return i*2+1
		if temp_q[i][1][0]=='[':
			temp_q[i][1]=temp_q[i][1][1:]
		else:
			print("ERROR2 in "+str(i*2+1)+"line")
			return i*2+1
		if temp_q[i][2][0]=='[':
			temp_q[i][2]=temp_q[i][2][1:]
		else:
			print("ERROR3 in "+str(i*2+1)+"line")
			return i*2+1
		if temp_q[i][3]:
			if temp_q[i][3][0]=='[':
				temp_q[i][3]=temp_q[i][3][1:]
			else:
				print("ERROR4 in "+str(i*2+1)+"line")
				return i*2+1
	return 0

def prepare_to_parse(t_string):

	temp_str = t_string
	#print("toparse")
	#print (t_string)

	temp_q=list()
	temp_a=list()
	temp_i=list()

	temp_str=temp_str.strip()
	temp_str=temp_str.split('\n')
	for i in range (0,len(temp_str)):
		temp_str[i]=temp_str[i].strip()
		temp_str[i]=temp_str[i].split(']')
		if len(temp_str[i])==5:
			temp_str[i].pop()

	for i in range (0,len(temp_str)):
		if not i%2: #question
			if temp_str[i][len(temp_str[i])-1]:
				temp_i.append(temp_str[i])
	#print("temp_i")
	#print(temp_i)


	temp_list_ans=list()
	for i in range(0,int(len(temp_str)/2)):
		#print(temp_str[i*2])
		temp_q.append(temp_str[i*2])
		if temp_q[i][0][0]=='[':
			temp_q[i][0]=temp_q[i][0][1:]
		else:
			print(temp_q[i][0][0])
			print("ERROR1 in "+str(i*2+1)+"line")
		if temp_q[i][1][0]=='[':
			temp_q[i][1]=temp_q[i][1][1:]
		else:
			temp_q[i][1][0]
			print("ERROR2 in "+str(i*2+1)+"line")
		if temp_q[i][2][0]=='[':
			temp_q[i][2]=temp_q[i][2][1:]
		else:
			temp_q[i][2][0]
			print("ERROR3 in "+str(i*2+1)+"line")
		if temp_q[i][3]:
			if temp_q[i][3][0]=='[':
				temp_q[i][3]=temp_q[i][3][1:]
			else:
				temp_q[i][3][0]
				print("ERROR4 in "+str(i*2+1)+"line")
		temp_list_ans=list()
		for j in range (0,len(temp_str[i*2+1])):
			temp_list_ans.append(temp_str[i*2+1][j][1:])
		temp_a.append(temp_list_ans)
	
	#print(temp_i)
	return temp_q, temp_a, temp_i


def parse(temp_q,temp_a):
	groups=list()
	temp_str = temp_q
	temp_ans = temp_a

	#print(temp_a)
	#create list of categories and prepare array for caregories groups
	categories=list()
	for i in range (0,len(temp_str)):
		if temp_str[i][0] not in categories:
			categories.append(temp_str[i][0])
			groups.append([])
	categories.sort()
	#print('\nwydrukuj kategorie:')
	#print (categories)

	#put groups into proper categories
	for i in range (0,len(categories)):
		for j in range(0,len(temp_str)):
			if temp_str[j][0]==categories[i] and (temp_str[j][1] not in groups[i]):
				groups[i].append(temp_str[j][1])
		groups[i].sort()
	#print('\nwydrukuj grupy')
	#print(groups)


	##create array for questions both with answers
	questions = list()
	answers = list()
	for i in range(0,len(categories)):
		questions.append([])
		answers.append([])
		for j in range(0,len(groups[i])):
			questions[i].append([])
			answers[i].append([])
	#and find questions from proper groups
	for k in range(0,len(temp_str)):
		questions[categories.index(temp_str[k][0])][groups[categories.index(temp_str[k][0])].index(temp_str[k][1])].append(temp_str[k][2])
		questions[categories.index(temp_str[k][0])][groups[categories.index(temp_str[k][0])].index(temp_str[k][1])].sort()
		answers[categories.index(temp_str[k][0])][groups[categories.index(temp_str[k][0])].index(temp_str[k][1])].append([])
	#print('\nwydrukuj pytania')
	#print(questions)

	##put questions:
	for k in range(0,len(temp_str)):
		qnumber = questions[categories.index(temp_str[k][0])][groups[categories.index(temp_str[k][0])].index(temp_str[k][1])].index(temp_str[k][2])
		answers[categories.index(temp_str[k][0])][groups[categories.index(temp_str[k][0])].index(temp_str[k][1])][qnumber].append(temp_ans[k])
	#print('\nwydrukuj odpowiedzi')
	#print(answers)



	#print all
	print('\nwydrukuj ladnie')
	for i in range (0,len(categories)):
		for j in range(0,len(groups[i])):
			for k in range(0,len(questions[i][j])):
				print(categories[i]+':'+groups[i][j]+':'+questions[i][j][k])
				answers[i][j][k]=answers[i][j][k][0]
				print(answers[i][j][k])
				print()

	return categories, groups, questions, answers


#if __name__ == "__main__":
#    temp_q,temp_a = prepare_to_parse()
#    categories, groups, questions, answers = parse(temp_q,temp_a)
    #cherrypy.quickstart(HelloWorld())