# see https://www.educative.io/blog/crack-coding-interview-real-world-problems for official article
# import numpy as np

# def DFS(users_array, n, visited, v):
#     for x in range(n):
#         if users_array[v,x] and visited[x] == 0:
#             if x != v:
#                 visited[x] = 1
#                 DFS(users_array, n, visited, x)

# def user_circle(users_array, n):
#     if n == 0: return 0

#     num_circles = 0

#     # create empty array of size n
#     vistited = np.zeros((n))

#     for i in range(n):
#         if vistited[i] == 0:
#             vistited[i] = 1
#             DFS(users_array, n , vistited, i)
#             num_circles += 1

#     return num_circles

# n = 4
# users_array = np.array([
#     [1,1,0,0],
#     [1,1,1,0],
#     [0,1,1,0],
#     [0,0,0,1]
# ])

# num_circles = user_circle(users_array, n)
# print(num_circles)


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
        'connectionIds': []
    },
]

for user in user_connections:
    print(user)
    user_id = user['id']
    connection_ids = user['connectionIds']