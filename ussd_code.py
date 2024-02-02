import time
import sys

ussd = input("\nUSSD code: ")
while ussd != "*312#":
    print('\nInvalid input!!\n \nTry again\n')
    ussd = input('USSD code: ')

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
                print("\nYou have successfully purchased 40MB for #50")
            elif ussd == "2":
                print("\nYou have successfully purchased 100MB for #100")
            elif ussd == "3":
                print("\nYou have successfully purchased 350MB(IG/TIKTOK/Youtube) for #100")
            else:
                print("Invalid input")
            time.sleep(2)

        # ... (similar changes in other methods)

    def check_balance(self):
        print("\nYour total balance is #1,000")
        time.sleep(2)

    def exit(self):
        sys.exit()
        time.sleep(2)

ussd = Page1("MTN")
