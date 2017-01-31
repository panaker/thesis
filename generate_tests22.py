#module2 create single test group + module3 create many tests  ### AKA GENERATE TESTS
def create_tests(amount,questions, answers,qAmount):
    tests = list();
    for i in range (0,amount):
        tests.append(create_test_group(questions,answers,qAmount))
    return tests

def create_test_group(questions,answers,qAmount):
    test_group = list()
    answer_group = list()
    correct_answers = list()
    import random
    questionsSequence = random.sample(range(len(questions)),len(questions))

    generated_tests=0;
    i = 0;
    listOfCategories=list()
    #for i in range (0,len(questionsSequence)):
    while True:
        if not questions[questionsSequence[i]].split('.')[0] in listOfCategories:
            listOfCategories.append(questions[questionsSequence[i]].split('.')[0])
            answersSequence = random.sample(range(len(answers[questionsSequence[i]])),len(answers[questionsSequence[i]]))
            test_group.append(questions[questionsSequence[i]].split('.')[1])
            temp = list()
            for j in range (0,len(answers[questionsSequence[i]])):
                temp.append(answers[questionsSequence[i]][answersSequence[j]])
                if answers[questionsSequence[i]][0] == answers[questionsSequence[i]][answersSequence[j]]:
                    correct_answers.append( [answers[questionsSequence[i]][answersSequence[j]],j])
            answer_group.append(temp)
            generated_tests += 1
        i+=1
        if generated_tests == qAmount:
            break

    return [test_group, answer_group, correct_answers]

def generate(categories,groups,questions,answers,questionNumbers,testSpecifications,images):

#2,1,3,2,1
#questionNumbers=[2,1,3,2,1,11]
#chce: 1,1,2,1,1
    #print('witamy w piekle ')
    for i in range(0,len(questionNumbers)):
        questionNumbers[i] = int(questionNumbers[i])
    #print(questionNumbers)
    testSpecifications = int(testSpecifications)
    #print(testSpecifications)
    #print(images)

    #print (answers)
    import random
    questionsList = list()
    answersList = list()
    imgList = list()

    for i in range (0, len(images)):
        tempList = list()
        tempList.append(categories.index(images[i][0]))
        tempList.append(groups[tempList[0]].index(images[i][1]))
        tempList.append(questions[tempList[0]][tempList[1]].index(images[i][2]))
        tempList.append(images[i][3])
        imgList.append(tempList)

    

    imgList2 = list()

    for i in range(0,len(questionNumbers)): #i to numer kategorii 
        groupsSequence = random.sample(range(len(groups[i])),questionNumbers[i])
        #print(groupsSequence)
        for j in range (0,len(groupsSequence)):
            question = random.sample(range(len(questions[i][groupsSequence[j]])),1)
            question = question[0]
            questionsList.append(questions[i][groupsSequence[j]][question])
            answersList.append(answers[i][groupsSequence[j]][question])
            for k in range (0,len(imgList)):
                if imgList[k][0] is i:
                    if imgList[k][1] is groupsSequence[j]:
                        if imgList[k][2] is question:
                            imgList2.append([len(questionsList)-1,imgList[k][3]])
    #print(imgList2)

    imgList3 = list()

    questionsList2 = list()
    answersList2 = list() #odpowiedzi niepomieszane odpowiednie do nowo ułożonych pytań
    answersList3 = list() #temporary list
    answersList4 = list()
    correctAnswers = list()
    sequence = random.sample(range(len(questionsList)),len(questionsList))

    for i in range(0,len(sequence)):
        for j in range (0,len(imgList2)):
            if sequence[i] is imgList2[j][0]:
                imgList3.append([i,imgList2[j][1]])

    #print (imgList3)

    for i in range(0,len(sequence)):
        questionsList2.append(questionsList[sequence[i]])
        answersList2.append(answersList[sequence[i]])
    
    for i in range (0,len(answersList2)):
        answersList3=list()
        sequence = random.sample(range(len(answersList2[i])),len(answersList2[i]))
        for j in range(0,len(sequence)):
            answersList3.append(answersList2[i][sequence[j]])
        answersList4.append(answersList3)

    for i in range(0,len(answersList4)):
        for j in range(0,len(answersList4[i])):
            if answersList4[i][j] == answersList2[i][0]:
                correctAnswers.append(j) ##OR J+1 if in human-readable form



    #print(questionsList2)
    #print(answersList4)
    #print(correctAnswers)

    return questionsList2, answersList4, correctAnswers, imgList3




    
