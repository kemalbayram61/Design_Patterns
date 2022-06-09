class session:
   __instance  = None
   __user_code = None
   __user_name = None
   __user_type = None

   @staticmethod
   def get_instance():
      if(session.__instance == None):
         session()
      return session.__instance

   def __init__(self):
      if(session.__instance != None):
         raise Exception("Sadece bir tane session nesnesi yaratılabilir.")
      else:
         self.__user_type   = "Admin"
         self.__user_name   = "testUser"
         self.__user_code   = "001"
         session.__instance = self

   def get_user_name(self):
      return self.__user_name

   def set_user_name(self, new_name):
      self.__user_name = new_name

   def get_user_code(self):
      return self.__user_code

   def set_user_code(self, new_code):
      self.__user_code = new_code

   def get_user_type(self):
      return self.__user_type

   def set_user_type(self, new_type):
      self.__user_type = new_type

session = session().get_instance()

print(session.get_user_name(), session.get_user_code(), session.get_user_type())
