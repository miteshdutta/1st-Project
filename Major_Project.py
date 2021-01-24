import csv
import time
localtime = time.asctime( time.localtime(time.time()) )
print("\n")
print("----------------------------------------")
print("Welcome to Student Administration Program")
print("----------------------------------------")
print ("Time :", localtime)
print("----------------------------------------")
print("\n")
def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
    
        if csv_file.tell()==0:
            writer.writerow(["First Name","Last Name", "Age", "Contact Number", "E-Mail ID"])
        writer.writerow(info_list)
if __name__== '__main__':
    
    condition = True
    student_num = 1
    
    while(condition):
        student_info = input ("Enter student information for student #{} in the following format (First_Name Last_Name Age Contact_Number E-mail_ID): ".format(student_num)) 

        student_info_list = student_info.split(' ')

        print ("Entered information is :\nFirst Name: {}\nLast Name: {}\nAge: {}\nContact Number: {}\nE-Mail ID: {} "
                .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3],student_info_list[4]))
        
        Check=input("Is the entered information correct? (yes/no): ")
        
        if Check=="yes":
            write_into_csv(student_info_list)
            
            condition_check = input("Enter (yes/no) if you want to enter information for another student: ") 
            if condition_check == "yes":
                condition = True
                student_num = student_num + 1
            elif condition_check == "no": 
                condition = False
        elif Check=="no":
            print('Re-enter the information')
print('\n')
print('Thank You for using School Administration Program.\nHave a Wonderful Day!')
print('\n')