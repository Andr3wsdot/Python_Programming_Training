class Grand:
    def skill(self):
        print("Reading Current Affairs")
class Father(Grand):
    def fatherskill(self):
        print("Makes Money")
class Son(Father):
    def sonskill(self):
        print("1.Watching Reels")

#Instance
son=Son()
son.sonskill()
son.fatherskill()
son.skill()