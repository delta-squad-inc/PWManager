import redismodel 
import redis


def main():
    #asd = {"key": [124514155144844, 151518541851]}
    pwmanager = redismodel.PasswordManager(6379, 'localhost', 0, _password="pwd1111")
    #pwmanager.setValue("facebook", "pwd123456789")
    #response = pwmanager.getValue("facebook")
    #pwmanager.setHash("gmail", ('111', '112', '15'))
    #pwmanager.setHash('gmail', 'pw123456')
    #response = pwmanager.delValue("gmail")
    response = pwmanager.getHash("gmail")
    #response = pwmanager.delHash("gmail")
    print(response)
if __name__ == "__main__":
    main()