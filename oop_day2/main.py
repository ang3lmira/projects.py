class User:
    def __init__(self, user_id, user_name, user_height):
        self.id = user_id
        self.user_name = user_name
        self.user_height = user_height
        self.followers = 0
        self.following = 0
        print("A new user has been created")

    def follow(self, user):
        user.followers += 1
        self.following += 1


person = User("001", "Omoyeni", "5'3")
#person.id = "001"
#person.name = "Omoyeni"
#person.height = "5'3"
print(person)
