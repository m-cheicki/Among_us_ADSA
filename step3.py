def Floyd_Warshall(M):
    for k in range(len(M)):
        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j] > M[i][k] + M[k][j]:
                    M[i][j] = M[i][k] + M[k][j]

    for i in range(len(index)):
        for j in range(i+1, len(index)):
            print(f"{index[i]} - {index[j]} : {M[i][j]}")
        print()


index = ["Cafetaria", "Admin", "Storage", "Weapons", "Medbay",
         "O2", "Navigations", "Shield", "Communications", "Electrical",
         "Lower E.", "Security", "Reactor", "Upper E."]

n = 1000

Map_Crew = [[0, 2, 2, 1, 2, n, n, n, n, n, n, n, n, 4],
            [2, 0, 2, n, n, n, n, n, n, n, n, n, n, n],
            [2, 2, 0, n, n, n, n, 3, 3, 3, 6, n, n, n],
            [1, n, n, 0, n, 2, 5, 7, n, n, n, n, n, n],
            [2, n, n, n, 0, n, n, n, n, n, n, n, n, 4],
            [n, n, n, 2, n, 0, 5, 7, n, n, n, n, n, n],
            [n, n, n, 5, n, 5, 0, 6, n, n, n, n, n, n],
            [n, n, 3, 7, n, 7, 6, 0, 2, n, n, n, n, n],
            [n, n, 3, n, n, n, n, 2, 0, n, n, n, n, n],
            [n, n, 3, n, n, n, n, n, n, 0, 5, n, n, n],
            [n, n, 6, n, n, n, n, n, n, 5, 0, 3, 3, 5],
            [n, n, n, n, n, n, n, n, n, n, 3, 0, 2, 3],
            [n, n, n, n, n, n, n, n, n, n, 3, 2, 0, 3],
            [4, n, n, n, 4, n, n, n, n, n, 5, 3, 3, 0]]

Map_Imp = [[0, 0, 2, 1, 2, 4, 4, 2, n, n, n, n, n, 4],
           [0, 0, 2, 4, n, 4, 4, 2, n, n, n, n, n, n],
           [2, 2, 0, n, n, n, n, 3, 3, 3, 6, n, n, n],
           [1, 4, n, 0, n, 2, 0, 7, n, n, n, n, n, n],
           [2, n, n, n, 0, n, n, n, n, 0, n, 0, n, 4],
           [4, 4, n, 2, n, 0, 5, 7, n, n, n, n, n, n],
           [4, 4, n, 0, n, 5, 0, 0, n, n, n, n, n, n],
           [2, 2, 3, 7, n, 7, 0, 0, 2, n, n, n, n, n],
           [n, n, 3, n, n, n, n, 2, 0, n, n, n, n, n],
           [n, n, 3, n, 0, n, n, n, n, 0, 5, 0, n, n],
           [n, n, 6, n, n, n, n, n, n, 5, 0, 3, 0, 5],
           [n, n, n, n, 0, n, n, n, n, 0, 3, 0, 2, 3],
           [n, n, n, n, n, n, n, n, n, n, 0, 2, 0, 0],
           [4, n, n, n, 4, n, n, n, n, n, 5, 3, 0, 0]]


# Floyd-Warshall algorithm
Imposter = Map_Imp.copy()
Crewmate = Map_Crew.copy()


Floyd_Warshall(Imposter)
Floyd_Warshall(Crewmate)
