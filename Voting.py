
class Voting_system:
    def __init__(self):
        print("Working in Voting special method or constructor ")
        self.students = {0: {"name": "James", "v_mark": 0, "voter": []},
                         1: {"name": "John", "v_mark": 0, "voter": []},
                         2: {"name": "Rooney", "v_mark": 0, "voter": []},
                         3: {"name": "Ronaldo", "v_mark": 0, "voter": []},
                         4: {"name": "Messi", "v_mark": 0, "voter": []}
                         }
        self.db: dict = {}
        self.id: int = 0
        self.R_money: int = 0
        self.user_points: int = 0

        self.l_id: int = 0

    def main_option(self):
        option = 0
        try:
            option = int(input("Press 1 to Register\nPress 2 to Login\nPress 3 to Exit"))
        except Exception as err:
            # print(err)
            print("Pls insert only Integer eg:1,2,3")

        if option == 1:
            self.register()
        elif option == 2:
            self.login()
        elif option == 3:
            self.recording_data()
            exit(1)
        else:
            print("Invalid Option")
            self.main_option()

    def register(self):
        print("This is register option ")
        pass_match = False
        try:
            r_email = input("Enter your email address to register!")
            r_name = input("Enter your name to register!")
            r_phone = input("Enter your phone to register!")
            r_address = input("Enter your address:")
            r_money = int(input("Enter your amount:"))
            r_points = 0

            while r_money < 500:
                print("Amount too low")
                r_money = int(input("Enter your amount again:"))

            if r_money >= 500:
                self.R_money = r_money

            #            print(r_money)

            while pass_match is False:
                r_pass1 = input("Enter your password to register!")
                r_pass2 = input("Retype your password:")

                if r_pass1 != r_pass2:
                    print("Your passwords not match")

                else:
                    print("Your passwords was recorded!")
                    self.id = len(self.db)
                    data_form: dict = {self.id: {"email": r_email, "name": r_name, "phone": r_phone,
                                                 "address": r_address, "password": r_pass1, "money": self.R_money,
                                                 "user_points": r_points}}

                    self.db.update(data_form)

                    pass_match = True
        except Exception as err:
            print("Invalid User Input!Try Again Sir!")
            self.register()

        print("Registration success :", self.db[self.id]["name"])

        r_option = False
        while r_option is False:
            try:
                user_option = int(input("Press 1 to Login!\nPress 2 Main Option:\nPress3 to Exit!:"))
                if user_option == 1:
                    self.login()
                    break
                elif user_option == 2:
                    self.main_option()
                    break
                elif user_option == 3:
                    self.recording_data()
                    exit(1)
                else:
                    print("Pls read again for option!")

            except Exception as err:
                print("Invalid Input!", err)

    def buy_points(self, l_id):
        print("You can buy points with your money")
        if self.R_money < 500:
            print("Insufficient amount")
            r_opt = False
            while r_opt is False:
                try:
                    buy_options = int(input("Press 1 to Top up more"))
                    if buy_options == 1:
                        self.top_up()
                        break
                    else:
                        print("Invalid")
                except Exception as err:
                    print("Only type integers", err)
        else:
            print(
                "Please tell us how many points you want to buy\n$500 for one point!\nYou can buy up to 100 points per one time!")
            print("This is your current amount", self.R_money)
            p_opt = False
            while p_opt is False:
                try:
                    b_points = int(input("Type the amount of points"))
                    if 1 <= b_points <= 100:
                        if b_points * 500 > self.R_money:
                            print("You do not have enough money\nGo to top up more")
                            self.top_up()
                            break
                        else:
                            self.R_money = self.R_money - (b_points * 500)
                            self.user_points = self.user_points + b_points
                            self.db[l_id]["money"] = self.R_money
                            self.db[l_id]["user_points"] = self.user_points

                            print("You have successfully bought {} points".format(b_points))
                            print("This is your current points {}.".format(self.user_points))
                            print("This is your current money {}".format(self.R_money))
                            break
                    else:
                        print("Invalid point amount!")
                except Exception as err:
                    print("Only type integers", err)

    def top_up(self):
        print("This is from top up")
        t_money = int(input("Enter the amount of money you want to top up"))
        self.R_money = self.R_money + t_money
        print("Top up succeed\nYour new amount {}".format(self.R_money))
        t_opt = False
        while t_opt is False:
            try:
                option = int(input("Press 1 to top again\nPress 2 to go back"))
                if option == 1:
                    self.top_up()
                    break
                elif option == 2:
                    self.buy_points(self.l_id)
                    break
                else:
                    print("Invalid")
            except Exception as err:
                print("Only type integers", err)

    def login(self):
        print("This is login option ")
        length = len(self.db)
        try:
            l_email = input("Enter your email to Login:")
            l_pass = input("Enter your pass to Login:")
            self.l_id = -1
            for i in range(length):
                if l_email == self.db[i]["email"] and l_pass == self.db[i]["password"]:
                    self.l_id = i
                    break
            if self.l_id != -1:
                self.user_sector(self.l_id)
            else:
                print("Username or Password incorrect!")
                self.login()

        except Exception as err:
            print(err, "\nInvalid input:")

    def recording_data(self):
        with open("Voting.txt", 'w') as votefile:
            for i in range(len(self.students)):
                student_name = self.students[i]["name"]
                student_vote_mark = self.students[i]["v_mark"]
                student_voter = []
                for j in range(len(self.students[i]["voter"])):
                    student_voter.append(self.students[i]["voter"][j])

                total_student_data = student_name + ' ' + str(student_vote_mark) + ' ' + str(student_voter) + '\n'

                votefile.write(total_student_data)

            votefile.write('\n')

            for i in range(len(self.db)):
                voter_email = self.db[i]["email"]
                voter_name = self.db[i]["name"]
                voter_phone = self.db[i]["phone"]
                voter_address = self.db[i]["address"]
                voter_password = self.db[i]["password"]
                voter_money = self.db[i]["money"]
                voter_points = self.db[i]["user_points"]

                total_voters_data = voter_email + ' ' + voter_name + ' ' + str(voter_phone) + ' ' + voter_address + ' ' + str(voter_password) + ' ' + str(voter_money) + ' ' + str(voter_points) + '\n'
                votefile.write(total_voters_data)

    def user_sector(self, l_id):
        self.R_money = self.db[l_id]["money"]
        self.user_points = self.db[l_id]["user_points"]
        print("Welcome", self.db[l_id]["name"])
        if self.user_points == 0:
            self.buy_points(l_id)

        print("Please select one!")
        for i in range(len(self.students)):
            print("Id:{} - Name {} - Current Vote Mark: {}".format(i, self.students[i]["name"],
                                                                   self.students[i]["v_mark"]
                                                                   ))

        try:
            print("You have {} points".format(self.user_points))
            v_id = int(input("Just Enter Id number to vote:"))
            points = int(input("Enter the vote amounts:"))
            if points > self.user_points:
                print("You do not have enough points\nBuy more points")
                self.buy_points(l_id)
                print("You have bought enough points")
                self.user_sector(l_id)
            else:

                self.user_points = self.user_points - points
                self.db[l_id]["user_points"] = self.user_points

                self.students[v_id]["v_mark"] += points
                for i in range(points):
                    self.students[v_id]["voter"].append(self.db[l_id]["name"])

                print("Congratulation you are voted!")
                print("{} now voting mark is : {}".format(self.students[v_id]["name"], self.students[v_id]["v_mark"]))

                for i in range(len(self.students[v_id]["voter"])):
                    print("Voter: ", self.students[v_id]["voter"][i])


        except Exception as err:
            print(err)

        while True:
            try:
                vote_option = int(input("Press 1 to Vote Again!\nPress 2 to get Main Option!\nPress 3 to Force Quit:"))

                if vote_option == 1:
                    self.user_sector(l_id)
                    break
                elif vote_option == 2:
                    self.user_points = 0
                    self.R_money = 0
                    self.main_option()
                    break
                elif vote_option == 3:
                    self.recording_data()
                    exit(1)
                else:
                    print("Invalid option after vote!")
            except Exception as err:
                print(err)


if __name__ == '__main__':
    voting = Voting_system()
    voting.main_option()

# ဆက်ရေး ရန် 8-5-2023
# voter များအား စာရင်း မှတ်ပေးရန်
# file ထဲ တွင် အားလုံး သိမ်းရန်
# top up method ရေး
