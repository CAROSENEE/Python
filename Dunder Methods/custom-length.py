class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

team = Team(["mahin", "Ayesha", "Rafi"])
print(len(team)) # Output: 3