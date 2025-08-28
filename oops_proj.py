class chatbot:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=False
        self.menu()

    def menu(self):
        user_input=input("""Welcome how would you like to proceed?
                         1.press 1 to signup
                         2.press 2 to sigin
                         3.press 3 to write a post
                         4.press 4 to message a friend
                         5.press any key to exit
                         
                         """)
        if user_input=='1':
            self.signup()
        elif user_input=='2':
            self.signin()
        elif user_input=='3':
            self.mypost()
        elif user_input=='4':
            self.send_message()
        else:
            exit()
    
    def signup(self):
        email=input("please enter your mail:")
        pwd=input("please enter your password:")
        self.username=email
        self.password=pwd
        print("you've successfully loggedin")
        print("\n")
        self.menu()

    def signin(self):
        if self.username=='' and self.password=='':
            print("please press 1 in main menu to signup first")
        else:
            uname=input("please enter your mail:")
            pwd=input("please enter your password:")
            if self.username==uname and self.password==pwd:
                print("you've signed in successfully")
                self.loggedin=True
            else:
                print("please enter correct credentials")

        print("\n")
        self.menu()

    def mypost(self):
        if self.loggedin==True:
            text=input("please enter your content here")
            print(f"the following content has been posted {text}")
        else:
            print("please sign in to proceed....")
        print("\n")
        self.menu()

    def send_message(self):
        if self.loggedin==True:
            text=input("please enter your content here")
            frnd=input("please enter the name of your friend whome you want to send")
            print(f"your message has been sent to {frnd}")
        else:
            print("please sign in to proceed....")
        print("\n")
        self.menu()


    
#obj=chatbot()