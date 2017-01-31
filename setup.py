def setup():

    questionPath = 'C:/Users/ostr/Desktop/inz/test of my life.txt'
    answersPath = 'C:/Users/ostr/Desktop/inz/test of my life - answers.txt'
    returnPath = 'C:/Users/ostr/Desktop/inz/my test'
    databasePath = 'C:/Users/ostr/Desktop/inz/database'
    testName = 'Test2'
    amount = 10;

    return questionPath,answersPath,returnPath,databasePath,testName,amount

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False