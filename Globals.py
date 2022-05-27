
def init():
    global Bug
    Bug = False

def VerifyField(field, value, id):
    if value != value:
        print("  ERROR: " + field + " - " + str(id + 2) + " ->  " + str(value) )
        return False
    else:
        return True
