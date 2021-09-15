
class InvalidLevel(Exception):
    def __init__(self,msg):
        self.msg= msg
level = -1
try:
    if level<1:
        raise InvalidLevel("invalid level:{}".format(level))
except InvalidLevel as e:
        print(e.msg)
            
