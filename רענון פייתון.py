

#1
def greet():
    print ('Hello, World!')

#2

def print_pairs(text):
    answer=''
    for i in range(len(text)):
        if i<(len(text)-1):
            if i%2==0:
                answer=answer+text[i]+text[i+1]+' '
    print (answer)

#3
    
def calc_weighted_avg(grades, weights):
    count=0
    for i in range(len(grades)):
        count+=grades[i]*weights[i]
    return count/sum(weights)

#4
import math
def log10_inplace(l):
    for i in range(len(l)):
        l[i]=math.log10(l[i])

#5
def reverse_file(input_file,output_file):
    f1=open(input_file,'r')
    x=f1.read()
    f1.close()
    f2=open(output_file,'w')
    f2.write(x[::-1])
    f2.close()
    
#6
import numpy as np
def load_data(input_file):
    f=open(input_file,'r')
    x=f.read()
    a=np.array(x)
    rows_header=a[0,:]
    columns_header=a[:,0]
    numeric=a[1:,1:]
    return rows_header,columns_header,numeric
    

#7
def get_most_frequent_char(text):
    char_count={}
    for char in text:
        count= char_count.get(char,0)+1
        char_count[char]=count
    sorted_chars=sorted(char_count, key=char_count.get)
    return sorted_chars[-1]

#8
def swap_student_courses(name_to_courses):
    courses_to_name={}
    for key in name_to_courses:
        for i in name_to_courses.get(key):
            if i not in courses_to_name:
                courses_to_name[i]=[]
            courses_to_name[i].append(key)
    return courses_to_name

