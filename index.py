master_contact_list = []
file_name = "sample2.txt"


class contact :
    def __init__(self,name = None,email = None,number = None):
        if name == None and email == None and number == None :
            self.name = input("Enter Contact Name : ")
            self.email = input("Enter Contact Email : ")
            self.number = input("Enter Contact Phone Number : ")
            student_entry="{},{},{}\n".format(self.name,self.email,self.number)
            print("Contact added successfully")
            file=open(file_name,"a")
            file.write(student_entry)
            file.close()
        else : 
            self.name = name 
            self.email = email
            self.number = number


    def show(self):
        print("======================================================")
        print("Name : ",self.name)
        print("Email : ",self.email)
        print("Phone Number : ",self.number)
        print("======================================================")


    def update_contact(self):
    file=open("sample1.txt","r")
    Master_data=file.readlines()
    file.close()
    search_student = input("Enter Search Term :")
    for i in Master_data:
        print("Contact found")
        print(contact)

        
    def delete_contact():
        pass




def show_all_contact():
    file=open(file_name,"r")
    Master_data=file.readlines()
    file.close()
    for i in Master_data :
        show(self)(i)

def get_master_data() :
    global master_contact_list 
    file=open(file_name,"r")
    master_data=file.readlines()
    file.close()
    master_contact_list = master_data

def post_master_data():
    global master_contact_list
    file = open(file_name,"w")
    for i in master_contact_list :
        file.write(i)
    file.close()


def search_contact():
    get_master_data()
    search_term = input("Enter Search Term : ")
    for k in master_contact_list :
        if search_term in k : 
            k = k.replace("\n","")
            y = k.split(",")
            print(y)
            c1 = contact(y[0],y[1],y[2])
            c1.show()
            break  
    else :
        print("Contact Not Found")



get_master_data()
print(master_contact_list)
choice1 = True
while choice1 == True :
    choice=int(input("press 1 for add contact\npress 2 for search contact\npress 3 for show contact\npress 4 for update contact\npress 5 for delete contact\nenter a valid choice:"))
    if choice == 1:
        c1 = contact()
        #c1.show()
    elif choice == 2:
        search_contact()
    elif choice == 3:
        show_all_contact()
    elif choice == 4:
        update_contact()
    elif choice == 5:
        delete_contact()
    else:
        print("Invalid Choice")
    next_choice = input("Enter (y) or any key to continue and (n) to stop : ")
    if next_choice == "n"or next_choice == "N":
        choice1 = False 