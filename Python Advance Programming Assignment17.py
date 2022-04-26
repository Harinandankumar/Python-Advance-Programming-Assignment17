#!/usr/bin/env python
# coding: utf-8

# 1. Create a function that transposes a 2D matrix.
# Examples
# transpose_matrix([
# [1, 1, 1],
# [2, 2, 2],
# [3, 3, 3]
# ]) ➞ [
# [1, 2, 3],
# [1, 2, 3],
# [1, 2, 3]
# ]
# transpose_matrix([
# [5, 5],
# [6, 7],
# [9, 1]
# ]) ➞ [
# [5, 6, 9],
# [5, 7, 1]
# ]
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[1]:


def transpose_matrix(in_list):
    output = []
    for ele_1 in range(len(in_list[0])):
        temp = []
        for ele_2 in in_list:
            temp.append(ele_2[ele_1])
        output.append(temp)
    print(f'transpose_matrix({in_list}) ➞ {output}')

transpose_matrix([[1, 1, 1],[2, 2, 2],[3, 3, 3]])
transpose_matrix([[5, 5],[6, 7],[9, 1]])


# 2. Create a function that determines whether a string is a valid hex code.
# A hex code must begin with a pound key # and is exactly 6 characters in
# length. Each character must be a digit from 0-9 or an alphabetic character
# from A-F. All alphabetic characters may be uppercase or lowercase.
# Examples
# is_valid_hex_code(&quot;#CD5C5C&quot;) ➞ True
# is_valid_hex_code(&quot;#EAECEE&quot;) ➞ True
# is_valid_hex_code(&quot;#eaecee&quot;) ➞ True
# is_valid_hex_code(&quot;#CD5C58C&quot;) ➞ False
# # Length exceeds 6
# is_valid_hex_code(&quot;#CD5C5Z&quot;) ➞ False
# # Not all alphabetic characters in A-F
# is_valid_hex_code(&quot;#CD5C&amp;C&quot;) ➞ False
# # Contains unacceptable character
# 
# is_valid_hex_code(&quot;CD5C5C&quot;) ➞ False
# # Missing #
#                   
#                   
#                   
#                   
#                   
#                   
#                   
#                   
#  ANs:-

# In[2]:


def is_valid_hex_code(in_string):
    out_string = True
    for ele in in_string:
        if ele.lower() not in '#abcdef0123456789' or len(in_string) != 7:
            out_string = False
    print(f'is_valid_hex_code({in_string}) ➞ {out_string}')

is_valid_hex_code("#CD5C5C")
is_valid_hex_code("#EAECEE")
is_valid_hex_code("#eaecee")
is_valid_hex_code("#CD5C58C")
is_valid_hex_code("#CD5C5Z")
is_valid_hex_code("#CD5C&C")
is_valid_hex_code("CD5C5C")


# 3. Given a list of math equations (given as strings), return the percentage of
# correct answers as a string. Round to the nearest whole number.
# Examples
# mark_maths([&quot;2+2=4&quot;, &quot;3+2=5&quot;, &quot;10-3=3&quot;, &quot;5+5=10&quot;]) ➞ &quot;75%&quot;
# mark_maths([&quot;1-2=-2&quot;]), &quot;0%&quot;
# mark_maths([&quot;2+3=5&quot;, &quot;4+4=9&quot;, &quot;3-1=2&quot;]) ➞ &quot;67%&quot;
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[3]:


import math
def mark_maths(in_list):
    out_list = []
    for ele in in_list:
        ele = ele.split("=")
        out_list.append(eval(ele[0]) == int(ele[1])) 
    print(f'mark_maths({in_list}) ➞ {str(math.ceil((sum(out_list)/len(out_list))*100))}%')
        
mark_maths(["2+2=4", "3+2=5", "10-3=3", "5+5=10"])
mark_maths(["1-2=-2"])
mark_maths(["2+3=5", "4+4=9", "3-1=2"])


# 4. There are two players, Alice and Bob, each with a 3-by-3 grid. A referee
# tells Alice to fill out one particular row in the grid (say the second row) by
# putting either a 1 or a 0 in each box, such that the sum of the numbers in that
# row is odd. The referee tells Bob to fill out one column in the grid (say the first
# column) by putting either a 1 or a 0 in each box, such that the sum of the
# numbers in that column is even.
# Alice and Bob win the game if Alice’s numbers give an odd sum, Bob’s give
# an even sum, and (most important) they’ve each written down the same
# number in the one square where their row and column intersect.
# Examples
# magic_square_game([2, &quot;100&quot;], [1, &quot;101&quot;]) ➞ False
# magic_square_game([2, &quot;001&quot;], [1, &quot;101&quot;]) ➞ True
# magic_square_game([3, &quot;111&quot;], [2, &quot;011&quot;]) ➞ True
# magic_square_game([1, &quot;010&quot;], [3, &quot;101&quot;]) ➞ False
# # Two lists, Alice [row, &quot;her choice&quot;], Bob [column, &quot;his choice&quot;]
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[4]:


def magic_square_game(in_one,in_two):
    output = False
    if in_two[1][in_one[0]-1] == in_one[1][in_two[0]-1]:
        output = True
    print(f'magic_square_game{in_one,in_two} ➞ {output}')
    
magic_square_game([2, "100"], [1, "101"])
magic_square_game([2, "001"], [1, "101"]) 
magic_square_game([3, "111"], [2, "011"]) 
magic_square_game([1, "010"], [3, "101"]) 


# 5. From point A, an object is moving towards point B at constant velocity va
# (in km/hr). From point B, another object is moving towards point A at constant
# velocity vb (in km/hr). Knowing this and the distance between point A and B
# (in km), write a function that returns how much time passes until both objects
# meet.
# Format the output like this:
# 
# &quot;2h 23min 34s&quot;
# Examples
# lets_meet(100, 10, 30) ➞ &quot;2h 30min 0s&quot;
# lets_meet(280, 70, 80) ➞ &quot;1h 52min 0s&quot;
# lets_meet(90, 75, 65) ➞ &quot;0h 38min 34s&quot;
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[5]:


import math
def lets_meet(in_dist,in_va,in_vb):
    total_time = in_dist/(in_va+in_vb)
    Hours = math.floor(total_time) 
    Minutes = math.floor((total_time-Hours)*60)
    Seconds = math.floor(((((total_time)-Hours)*60)-Minutes)*60)
    print(f'lets_meet{in_dist,in_va,in_vb} ➞ {Hours}h {Minutes}min {Seconds}s')
    
lets_meet(100, 10, 30)
lets_meet(280, 70, 80)
lets_meet(90, 75, 65)

