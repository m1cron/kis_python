class C32:
    def __init__(self):
        self.stage = "A"

    def exit(self):
        if self.stage == "A":
            return 1
        elif self.stage == "B":
            self.stage = "C"
            return 2
        elif self.stage == "C":
            self.stage = "D"
            return 3
        elif self.stage == "D":
            return 6
        elif self.stage == "E":
            self.stage = "F"
            return 8
        else:
            raise RuntimeError

    def hoard(self):
        if self.stage == "A":
            self.stage = "B"
            return 0
        elif self.stage == "C":
            self.stage = "E"
            return 4
        elif self.stage == "D":
            self.stage = "E"
            return 5
        else:
            raise RuntimeError

    def pull(self):
        if self.stage == "D":
            self.stage = "A"
            return 7
        else:
            raise RuntimeError