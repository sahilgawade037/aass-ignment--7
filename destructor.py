class emp:
    
    def __init__(self):
        print("Emp is created")
  
    def __del__(self):
        print("Destructor called")

obj = emp()
del obj