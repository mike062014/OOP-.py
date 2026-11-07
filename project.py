class dailymessage():
    
    def __init__(self):
        self.message = ""

    def get_message(self):
        self.message = input("Enter message")

    def print_message(self):
        print("Your message is",self.message.upper())
class helpsession():
    def __init__(self):
        print("Help session started")

    def __del__(self):
        print("Help session ended")
def createsession():
    print("Session in creation...")
    session_start = helpsession()
    print("Session done!!")
    return session_start
class pairfinder():
    