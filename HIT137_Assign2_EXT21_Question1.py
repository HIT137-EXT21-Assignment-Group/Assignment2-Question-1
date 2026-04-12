def main():
                                                #input file path aquisition    
    file_path = str(input("Enter file path :")) 
    print(f'_'*14,'START','_'*14)               #formatting to claify file text boundries
    
    with open(file_path,'r') as input_file:     #open file from file path to read as input_file
        initial_data = input_file.read()        #create copy of file for encryption 
        print(initial_data)
    print(f'_'*15,'END','_'*15)                 #formatting to claify file text boundries
    path = file_path.replace('raw_text','write_file') # alter read path to write path
    print("file path :",path)                   #print file path for write
    print(f'_'*14,'START','_'*64)               #formatting to claify file text boundries 
    encrypt_lst, index_list = encrypt_file(initial_data, path)            
    print(f'_'*85)
    with open(path,'w') as write_file:
        for item in encrypt_lst:
            write_file.write(f"{item}")
    with open(path,'r') as write_file:
        out_put_data = write_file.read()
    print(out_put_data)  
    print(f'_'*35)
    print(index_list)                                                
    print(f'_'*15,'END','_'*15) 
def encrypt_file(initial_data, path):
    def find_letter(list,letter):
        for i in range(len(list)):
            if letter == list[i]:
                index_letter = i
        return index_letter
    s1 = 14
    s2 = 14
    while not(s1 <= 12 and s2 <=12):                                    #input values for encrytion mechanic
        s1 = int(input("Enter the first amount of alphabetical letter shifts for this encryption :"))
        if not(s1 <=12) or s1 < 0:
            print("Error - Out of shift range enter a number between 1 and 12")
        s2 = int(input("Enter the second amount of alphabetical letter shifts for this encryption :"))
        if not(s2 <=12) or s2 < 0:
            print("Error - Out of shift range, enter a number between 1 and 12")      
    enc_lower1 = [chr(i) for i in range(ord('a'), ord('m') + 1)]        #create a string of letters from a to m
    full_alpha_lower = [chr(i) for i in range(ord('a'), ord('z') + 1)]  #create a string of letters from a to z
    enc_lower2 = [chr(i2) for i2 in range(ord('A'), ord('M') + 1)]      #create a string of letters from A to M
    enc_upper1 = [chr(i3) for i3 in range(ord('n'), ord('z') + 1)]      #create a string of letters from n to z
    full_alpha_upper = [chr(i) for i in range(ord('A'), ord('Z') + 1)]  #create a string of letters from A to Z
    enc_upper2 = [chr(i4) for i4 in range(ord('N'), ord('Z') + 1)]      #create a string of letters from N to Z
    
    index_list = []
    encrypted_string = []                                               #initialise variable to hold the results
    for char in initial_data:                                           #variable holds check value from input
        if char.isalpha():                                              #check for aphabetical character
            if char in enc_lower1:                                      #check value is in range a to m
                index = find_letter(full_alpha_lower,char)                #encrypt lowercase a to m method
                if (index + (s1*s2)) >= 25:
                    new_char = "z"
                else:
                    new_char = full_alpha_lower[index + (s1 *s2)]
            if char in enc_lower2:                                      #check letter is in range A to M
                index = find_letter(full_alpha_upper,char)                #encrypt uppercase A to N method
                                       
                if (index - (s1+s2)) < 0:
                    new_char = "A"
                else:
                    new_char = full_alpha_upper[index - (s1+s2)]
            if char in enc_upper1:                                      #check letter is in range n to z
                index = find_letter(full_alpha_lower,char)                #encrypt lowercase n to z method
                if (index -s1) <= 0:
                    new_char = "a"
                else:
                    new_char = full_alpha_lower[index-s1]            
            if char in enc_upper2:                                      #check letter is in range N to Z
                index = find_letter(full_alpha_upper,char)                 #encrypt uppercase M to Z method
                if (index + (s2*s2)) >= 25:
                    new_char = "Z"
                else:
                    new_char = full_alpha_upper[index +(s2*s2)]  
            next_index = index  
        else:
            new_char = char 
            next_index = char                                          #check value is not alphabetical save value
        encrypted_string.append(new_char)
        index_list.append(next_index)                               #add current vale to end of string
    return encrypted_string , index_list                                            #return encrypted string
    
                                                             
main()  
