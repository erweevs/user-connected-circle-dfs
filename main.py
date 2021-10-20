import numpy as np

def DFS(users_array, n, visited, v):    
    for x in range(n):
        if users_array[v,x] : connected_users_matrix.append([v,x])
        if users_array[v,x] and visited[x] == 0:            
            if x != v:
                visited[x] = 1
                DFS(users_array, n, visited, x)
    

def user_circle(users_array, n):
    if n == 0: return 0

    global users_in_circle
    users_in_circle = []

    global connected_users_matrix

    num_circles = 0

    # create empty array of size n
    vistited = np.zeros((n))

    for i in range(n):
        if vistited[i] == 0:
            vistited[i] = 1
            connected_users_matrix = []
            DFS(users_array, n , vistited, i)

            num_circles += 1

            connected_users = []

            for matrix, value in connected_users_matrix:
                if value not in connected_users:
                    connected_users.append(value)

            users_in_circle.append({
                'circle': num_circles,
                'users' : connected_users
            })

    return num_circles

def find_users_to_connect(circle, userId):
    user_new_connections = []
    for user in circle:
        if user not in user_new_connections and user != userId: user_new_connections.append(user)
    
    return user_new_connections

user_connections = [
    {
        'id': 0,
        'name': 'Nick',
        'connectionIds': [1]
    },
    {
        'id': 1,
        'name': 'Amy',
        'connectionIds': [0,2]
    },
    {
        'id': 2,
        'name': 'Mat',
        'connectionIds': [1]
    },
    {
        'id': 3,
        'name': 'Mario',
        'connectionIds': [4,5]
    },
    {
        'id': 4,
        'name': 'James',
        'connectionIds': [3]
    },
    {
        'id': 5,
        'name': 'Annie',
        'connectionIds': [3]
    }
]

size = len(user_connections)

matrix = np.zeros(shape=(size, size))

index = 0
final_matrix = []
for user in user_connections:
    connection_matrix = [0] * size

    user_id = user['id']
    connection_ids = user['connectionIds']

    for column in range(size):
        if column in connection_ids:
            connection_matrix[column] = 1
    
    connection_matrix[user_id] = 1

    final_matrix.append(connection_matrix)

    index = index + 1

num_circles = user_circle(np.array(final_matrix), size)


for user in user_connections:
    user_id = user['id']
    connection_ids = user['connectionIds']

    for circle in users_in_circle:
        if user_id in circle['users']: 
            connections_they_might_know = find_users_to_connect(circle['users'], user_id)
            print('User Id: ', user_id)
            print('Might know: ', connections_they_might_know)