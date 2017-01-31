import setup
import import_test
import generate_tests
import export_tests
import cherrypy
import database


class HelloWorld(object):
    def index(self):
        return "Hello world!"
    index.exposed = True

def main():

    #SETUP
    questionPath, answersPath, returnPath, databasePath, testName, amount = setup.setup()


    #module1 import test from file
    questions, answers = import_test.collect_data(questionPath,answersPath)



    #
    #export_tests.remove(databasePath)

    #database.createDatabase(databasePath)
    #database.appendData(testName,questions,answers,databasePath)

    #names = database.getListOfTests(databasePath)
    #print(names)

    #questions2, answers2 = database.getFromDatabase(testName,databasePath)




    #moculde2 generate single test_group +  answer_group + correct answers
    #test_group, answer_group, correct_answers = create_test_group(questions2,answers2)
    #module2+3
    
    print(questions)
    print(answers)
    #export_tests.remove(returnPath)
    tests = generate_tests.create_tests(2,questions,answers,3)
    
    #print(len(tests[9]))


    #module4 export to txt files
    #export_tests.export_tests(tests,returnPath) #PROBABLY PATH AS WELL

    #MODULE5 put_data_to_database










if __name__ == "__main__":
    main()
    #cherrypy.quickstart(HelloWorld())