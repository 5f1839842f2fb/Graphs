import random
import collections

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        names = {"Bob", "Dan", "Lisa", "Emily", "Phillip", "Billy", "Katy", "Julie", "Robert", "Dorothy"}
        if avg_friendships >= num_users:
            return "average friendships must be less than number of users"
        # Add users
        for i in range(0, num_users):
            name = names.pop()
            self.add_user(name)
        # Create friendships
        allPossible = []
        for user1 in self.users:
            for user2 in self.users:
                if user1 != user2 and (user2, user1) not in allPossible:
                    allPossible += [(user1, user2)]
        random.shuffle(allPossible)
        for i in range(0, avg_friendships*num_users):
            friendship = allPossible.pop()
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = set()  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        routes = collections.defaultdict(list)
        paths = [[user_id]]
        while len(paths) > 0: # 
            path = paths.pop(0)
            node = path[-1]
            if node not in visited:
                routes[node] += [path]
                visited.add(node)
                for edge in self.friendships[node]:
                    paths += [path + [edge]]
        routes.pop(user_id)
        return routes


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
