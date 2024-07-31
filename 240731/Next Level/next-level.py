class game:
    def __init__(self, user_id = "codetree", user_lv = '10'):
        self.user_id = user_id
        self.user_lv = user_lv

a, b = map(str, input().split())
user1 = game()
print("user " + user1.user_id + " lv " + user1.user_lv)
user2 = game(a, b)
print("user " + user2.user_id + " lv " + user2.user_lv)