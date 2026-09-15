class User:
    def __init__(self, name, password, age):
        self.name = name
        self.__password = password
        self.age = age

    def login(self):
        name = input("User: ").strip()
        password = input("Password: ")

        while name != self.name or password != self.__password:
            print("Incorrect User or Password, try again...")
            name = input("User: ").strip()
            password = input("Password: ")

        print("You have been logged in correctly!")

    def public_comment(self, content, receiver):
        comment = Comment(content, self.name, receiver)
        print(f"{comment.text}, by {comment.author}, to {comment.receiver}")
        return comment

class Post:
    def __init__(self, title, content, type, author):
        self.title = title
        self.content = content
        self.type = type
        self.author = author

    def like(self):
        print(f"{self.title} \n {self.content} \n {self.type}")
        like = input("Do you want to like this post?(Y/N): ").strip().upper()

        while like != "Y" and like != "N":
            print("Incorrect input. Only Yes or No (Y/N)")
            like = input("Do you want to like this post?: ").strip().upper()

        if like == "Y":
            print("Okey :)")
        else:
            print("Okey :(")

    def create_post(self):
        print(f"Title: {self.title} \n Content: {self.content} \n By: {self.author}")

class Comment:
    def __init__(self, text, author, receiver):
        self.text = text
        self.author = author
        self.receiver = receiver

    def like_comment(self):
        print(f"Comment: {self.text} \n By: {self.author} \n From: {self.receiver}")
        like = input("Do you want to like this comment?(Y/N): ").strip().upper()

        while like != "Y" and like != "N":
            print("Incorrect input. Only Yes or No (Y/N)")
            like = input("Do you want to like this comment?: ").strip().upper()

        if like == "Y":
            print("Okey :)")
        else:
            print("Okey :(")


class Message:
    def __init__(self, sender, receiver, text):
        self.sender = sender
        self.receiver = receiver
        self.text = text

    def send(self):
        print(f"By: {self.sender} \n For: {self.receiver} \n Message: {self.text}")
        confirm = input("Do you want to send this message? (Y/N): ").strip().upper()

        while confirm != "Y" and confirm != "N":
            print("Incorrect Input. Only Yes or No (Y/N)")
            confirm = input("Do you want to send this message? (Y/N): ").strip().upper()

        if confirm == "Y":
            print("Message sent! :)")
        else:
            print("Message NOT sent :(")

user1 = User("Juan", "Pepito57", 17)
user2 = User("Lupita", "Pepita57", 19)

post1 = Post("Dead Space", "Buy it now! It is an epic game", "Reel", user1.name)
message1 = Message("Juan", "Lupita", "Hello Lupita :P")

user1.login()
post1.like()
post1.create_post()
message1.send()

user1.public_comment("Hola", user2.name)
