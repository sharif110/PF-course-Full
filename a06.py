## IMPORTS GO HERE
import os

#### YOUR CODE FOR text_count FUNCTION GOES HERE ####

def text_count(directory,file_name,parameter3 = False,parameter4 = False):
    import os
    file_path=os.path.join(directory,file_name)
    read=open (file_name,"r")
    number_of_words=0
    if parameter4 == True:
         number_of_word=len(open(file_name,"r").read())
    if parameter3 == True:
        for i in read:
            words=i.strip().split(" ")
            for j in words:
                if j.islower():
                    number_of_words += 1
                    number_of_word=number_of_words  
    elif parameter4 == True:
        number_of_word=len(open(file_name,"r").read())
    else:
        for line in read:
            line=line.strip("\n")
            words=line.split()
            number_of_words += len(words)
            number_of_word = number_of_words
    read.close()
    return number_of_word
    
    
    
    
        
        
#### End OF MARKER

#### YOUR CODE FOR copy_lines FUNCTION GOES HERE ####
def copy_lines(input_file,output_file,number):
    with open(input_file, "r") as file1:
        with open(output_file, "w") as file2:
            list1=[]
            for readline in file1:
                readline=readline.strip()
                if readline == "":
                    list1.append("\n\n")
                else:
                    list1.append(readline)
            for range_n in range(0,number):
                file2.write(list1[range_n])
            
    
    
#### End OF MARKER



