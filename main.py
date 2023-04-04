from cryptography.fernet import Fernet

class password_manager:

    def __init__(self):
        self.key =None
        self.password_file = None
        self.password_dict = {}

    def create_key(self, path):
        self.key = Fernet.generate_key()
        with open(path, 'wb') as f:
            f.write(self.key)

    def load_key(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()

    def create_pass_file(self, path, initial_values=None):
        self.password_file = path

        if initial_values is not None:
            for key, values in initial_values.items():
                self.add_password(key, values)

    def load_pass_file(self, path):
        self.password_file = path
        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(":")
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()
    def add_password(self,site, password):
        self.password_dict[site] =password

        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode() + "\n")

    def get_password(self, site):
        return self.password_dict[site]



def main():
    password = {
        "email": "1234567",
        "facebook" : "face123",
        "yahoo" : "yah321",
        "linkedin" : "softwarelinked123"
    }

    pass_mang = password_manager()

    #show the menu to the user

    print(""" Chose belong to the  number 
    [1] create new key
    [2] load exist key
    [3] create new pass file
    [4] load exist pass file
    [5] add new pass
    [6] get a pass 
    [e] exit 

    """)
    fContinue = False

    while not fContinue:
        choice = input("Enter: ")
        if choice == "1":
            path = input("Enter the path you where want to save: ")
            pass_mang.create_key(path)
        elif choice =="2":
            path = input("Enter the path you where want to save: ")
            pass_mang.load_key(path)
        elif choice =="3":
            path = input("Enter the path you where want to save: ")
            pass_mang.create_pass_file(path, password)
        elif choice == "4":
            path = input("Enter the path you where want to save: ")
            pass_mang.load_pass_file(path)
        elif choice == "5":
            site = input("Enter the site: ")
            password = input("Enter the password: ")
            pass_mang.add_password(site,password)
        elif choice == "6":
            site = input("Enter the site: ")
            print(f"password for {site} is {pass_mang.get_password(site)}")
        elif choice == "e":
            fContinue = True
            print("goodbye")

        else:
            print("Invalid option !")




if __name__ == "__main__":
    main()
