import numpy as np
from collections import defaultdict
import math


matrix = []
# with open("dataset1.txt", 'r') as f:
with open("dataset2.txt", 'r') as f:
    a = f.readlines()
    for i in a:
        a = i.replace("(", "").replace(")", "")
        b = a.split()
        matrix.append(b)

for j in matrix:
    for i in range(0, len(j)):
        j[i] = int(j[i])

'''
Question A
'''

print("Adjacency matrix",matrix)

# result_path = "result-1.txt"
# # result_path = "result-2.txt"
# output_file = open(result_path, "w")
# output_file.write("Number\n")
# # output_file.write("Intial Transition Probability matrix\n")
# output_file.write("(")
# count = len(matrix)
# for j in matrix:
#     count1 = len(j)
#     for i in j:
#         output_file.write(str(round(i,2)))
#         count1 = count1 - 1
#         if count1 != 0:
#             output_file.write(" ")
#
#     count = count - 1
#     if count != 0:
#         output_file.write("\n ")
#
# output_file.write(")\n")


for j in matrix:
    count = 0
    for i in range(0, len(j)):
        if j[i] == 1:
            count+= 1
    for i in range(0, len(j)):
        if j[i] == 1:
            j[i] = 1/count

print("Intial Transition Probability matrix",matrix)


# result_path = "result-1.txt"
result_path = "result-2.txt"
output_file = open(result_path, "w")
output_file.write("51\n")
# output_file.write("Intial Transition Probability matrix\n")
output_file.write("(")
count = len(matrix)
for j in matrix:
    count1 = len(j)
    for i in j:
        output_file.write(str(round(i,2)))
        count1 = count1 - 1
        if count1 != 0:
            output_file.write(" ")

    count = count - 1
    if count != 0:
        output_file.write("\n ")

output_file.write(")\n")

'''
End of Question A
'''

'''
Start of Question B
'''

print("Non-Stochastic Matrix", matrix)
for j in matrix:
    if all(i==0 for i in j):
        val = len(j)
        for k in range(len(j)):
            j[k] = 1/val

print("Stochastic Matrix", matrix)
# output_file.write("Stochastic Matrix\n")
output_file.write("(")
count = len(matrix)
for j in matrix:
    count1 = len(j)
    for i in j:
        output_file.write(str(round(i,2)))
        count1 = count1 - 1
        if count1 != 0:
            output_file.write(" ")

    count = count - 1
    if count != 0:
        output_file.write("\n ")

output_file.write(")\n")

if "1" in result_path:
    vari = True
else:
    vari = False


'''
 End of Question B
'''

'''
dAt
'''


k = len(matrix)

def transpose(matrix):
    for i in range(k):
        for j in range(i + 1, k):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

transpose_matrix = matrix[:][:]
transpose(matrix)

d = 0.9
for j in matrix:
    for i in range(0, len(j)):
        j[i] = j[i]*d
# print("dAt", matrix)

'''
end of dAt
'''

one_minus_d = 1 - d
mat_val = one_minus_d * (1/len(matrix))
E_matrix = []
for i in range(0, len(matrix)):
    k_list = []
    for j in range(0, len(matrix)):
        k_list.append(mat_val)
    E_matrix.append(k_list)
# print("E_matrix", E_matrix)

result_matrix = []
for i in range(0, len(matrix)):
    n_list = []
    for j in range(0, len(matrix)):
        n_list.append(0)
    result_matrix.append(n_list)

for i in range(len(E_matrix)):
    for j in range(len(E_matrix[0])):
        result_matrix[i][j] = round(E_matrix[i][j] + matrix[i][j],2)
print("result_matrix", result_matrix)

# output_file.write("Irreducible Matrix\n")
output_file.write("(")
count = len(result_matrix)
for j in result_matrix:
    count1 = len(j)
    for i in j:
        output_file.write(str(i))
        count1 = count1 - 1
        if count1 != 0:
            output_file.write(" ")

    count = count - 1
    if count != 0:
        output_file.write("\n ")

output_file.write(")\n")

e_mat = []
for i in range(0, len(matrix)):
    e_mat.append(1/len(matrix))
print("e_mat", e_mat)


# D_list = []
def PageRank(matrix):
    P0 = e_mat
    print("P00000", P0)
    P1 = []
    for j in matrix:
        list2 = []
        for i in range(0, len(j)):
            v = j[i] * P0[i]
            list2.append(v)
        P1.append(sum(list2))
    print("P1 **********", P1)
    P2 = []
    for j in matrix:
        list3 = []
        for i in range(0, len(j)):
            w = j[i] * P1[i]
            list3.append(round(w,3))
        # P2.append(round(sum(list3),2))
        P2.append(sum(list3))
    print("P2 final **********", P2)
    # print("nw_list***", nw_list)

    return P2

pagerank_list = PageRank(result_matrix)
print("pagerank_list", pagerank_list)
# output_file.write("PageRank Value\n")
output_file.write("(")
count2 = len(pagerank_list)
for i in pagerank_list:
    if vari:
        a_float = round((math.floor(i * 10 ** 2) / 10 ** 2),2)
    else:
        a_float = round((math.ceil(i * 10 ** 2) / 10 ** 2), 2)
    output_file.write(str(a_float))
    count2 = count2 -1
    if count2 != 0:
        output_file.write(" ")
output_file.write(")")
