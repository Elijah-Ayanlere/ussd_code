import time
import sys
ussd = input("\nUSSD code: ")
while ussd != "*312#":
      ussd = input('\nInvalid input!!\n \nTry again\n \nUSSD code: ')
class Page1:
    def __init__(self, name):
        self.name = name
        self.page2()
    
    def page2(self):
        print(f"\nWelcome to {self.name} data plan.")

        print("""
        \n1. Data plans \n2. Social Bundles \n3. Balance check \n4. Exit
        """)

        user = input("\nEnter your choice: ")
        if user == "1":
            self.data_plan()
        elif user == "2":
            self.social_bundle()
        elif user == "3":
            self.check_balance()
        elif user == "4":
            self.exit()
            
    def data_plan(self):
        ussd = input("\nBuy Data Plans\n \n1. Daily \n2. Weekly \n3. Monthly\n \nChoose your plan: ")
        if ussd == "1":
            ussd = input("\n1. #50 for 40MB \n2. #100 for 100MB \n3. #100 for 350MB(IG/TIKTOK/Youtube)\n \nChoose your plan: ")
            if ussd == "1":
                ussd = print("\nYou have successfully purchased 40MB for #50")
            elif ussd == "2":
                ussd = print("\nYou have successfully purchased 100MB for #100")
            elif ussd == "3":
                ussd = print("\nYou have successfully purchased 350MB(IG/TIKTOK/Youtube) for #100")
            else:
                print("Invalid input")
                time.sleep(2)
                    
        elif ussd == "2":
            ussd = input("\n1. #300 for 350MB \n2. #200 for 1GB(IG/TT/YT) \n3. #500 for 1.5GB\n \nChoose your plan: ")
            if ussd == "1":
                ussd = print("\nYou have successfully purchased 350MB for #300")
            elif ussd == "2":
               ussd = print("\nYou have successfully purchased 1GB for #200")
            elif ussd == "3":
                ussd = print("\nYou have successfully purchased 1.5GB for #500")
            else:
                print("Invalid input")
                time.sleep(2)
                    
        elif ussd == "3":
            ussd = input("\n1. #1,000 for 1.5GB \n2. #1200 for 2GB \n3. #1,500 for 3GB\n \nChoose your plan: ")
            if ussd == "1":
                ussd = print("\nYou have successfully purchased 1.5GB for #1,000")
            elif ussd == "2":
                ussd = print("\nYou have successfully purchased 2GB for #1200")
            elif ussd == "3":
                ussd = print("\nYou have successfully purchased 3GB for #1,500")
            else:
                print("Invalid input")
                time.sleep(2)
                                
    def social_bundle(self):
        ussd = input("\n1. WhatsApp \n2. Facebook \n3. Instagram \n \nChoose your plan: ")
        if ussd == "1":
            ussd = input("\nWhatsApp\n \n1. Daily @ #25 for 25MB \n2. Weekly @ #50 for 50MB \n3. Monthly @ #150 for 150MB\n \nChoose your plan: ") 
            if ussd == "1":
                ussd = print("\nYou have successfully purchased 25MB for #25 for WhatsApp")
            elif ussd == "2":
                ussd = print("\nYou have successfully purchased 50MB for #50 for WhatsApp")
            elif ussd == "3":
                ussd = print("\nYou have successfully purchased 150MB for #150 for WhatsApp")
            else:
                print("Invalid input")
                time.sleep(2)
                    
        elif ussd == "2":
            ussd = input("\nFacebook\n \n1. Daily @ #25 for 25MB \n2. Weekly @ #50 for 50MB \n3. Monthly @ #150 for 150MB\n \nChoose your plan: ") 
            if ussd == "1":
                ussd = print("\nYou have successfully purchased 25MB for #25 for Facebook")
            elif ussd == "2":
                ussd = print("\nYou have successfully purchased 50MB for #50 for Facebook")
            elif ussd == "3":
                ussd = print("\nYou have successfully purchased 150MB for #150 for Facebook")
            else:
                print("Invalid input")
                time.sleep(2)
                
        elif ussd == "3":
            ussd = input("\nInstagram\n \n1. #100 for 250MB/1 day \n2. #100 for 350MB \n3. #200 for 1GB \n4. #200 for 1GB/3-days\n \nChoose your plan: ") 
            if ussd == "1":
                ussd = print("\nYou have successfully purchased 250MB for #100")
            elif ussd == "2":
                ussd = print("\nYou have successfully purchased 350MB for #100")
            elif ussd == "3":
                ussd = print("\nYou have successfully purchased 1GB for #200")
            elif ussd == "4":
                ussd = print("\nYou have successfully purchased 1GB for #200 for 3-days")
            else:
                print("Invalid input")
                time.sleep(2)
                
    def check_balance(self):
        ussd = print("\nYour total balance is #1,000")
        time.sleep(2)


    def exit(self):
        sys.exit()
        time.sleep(2)
            

ussd = Page1("MTN")