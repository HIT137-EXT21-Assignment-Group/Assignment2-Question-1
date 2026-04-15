# Simple Encryption and Decryption Progam
#==============================================================================================================================================
# This progam will read a text file from a file path entered by the user. 
# The program will display the file contents then prompt the user for two integer values which will be used to inform the encryption mechanic. 
# Once the encrytption is completed a two outputs will be produced.
# The encrypted file will be created and an array containing all the no alphabetic characters and the index values from the input file will be 
# returned to the main program. 
# The encrypted file will the be used as input for the decryption mechanic.
# Once the decryption mechanic is complete the resulting file will created and compared to the initial input file.
# A message will be printed to screen indicting the sucess or failure of the decrytion.
#===============================================================================================================================================
def main():
                                                                  #input file path aquisition    
    file_path = str(input("Enter file path :")) 
    print(f'_'*14,'START','_'*14)                                 #display formatting to claify file text boundries
    
    with open(file_path,'r') as input_file:                       #open file from file path to read as input_file
        initial_data = input_file.read()                          #create copy of file for encryption 
        print(initial_data)
    print(f'_'*15,'END','_'*15)                                   #formatting to claify file text boundries
    path = file_path.replace('raw_text','write_file')             #alter read path to write path
    print("file path :",path)                                     #print file path for write
    print(f'_'*14,'START','_'*64)                                 #formatting to claify file text boundries 
    encrypt_lst, index_list = encrypt_file(initial_data, path)    #call encrypt function and return two values            
    print(f'_'*85)                                                #display formatting to claify file text boundries
    with open(path,'w') as write_file:                            #open write file for write 
        for item in encrypt_lst:                                  #interation to write file
            write_file.write(f"{item}")
    with open(path,'r') as write_file:                            #open file for read
        out_put_data = write_file.read()                          #read file
    print(out_put_data)                                           #print encrypted file                             
    print(f'_'*35)                                                #display formatting to claify file text boundries
    print(index_list)                                             #print array of index values before encryption for decryption                    
    print(f'_'*15,'END','_'*15)                                   #display formatting to claify file text boundries

def encrypt_file(initial_data, path):                             #def to encrypt a file shifting letter values
    def find_letter(list,letter):                                 #def to find the index of an alpha char
        for i in range(len(list)):
            if letter == list[i]:
                index_letter = i
        return index_letter
    s1 = 14                                                     #initialise s1 variable for false condition
    s2 = 14                                                     #initialise s2 variable for false condition
    while not(s1 <= 12 and s2 <=12):                            #interation to input shift values for encrytion mechanic
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
            next_index = index                                      # current index value 
        else:
            new_char = char                                         #check value is not alphabetical and save value
            next_index = char                                       #save alphabetical index value or other character
        encrypted_string.append(new_char)                           #add encrypted value to end of string
        index_list.append(next_index)                               #add current index value or other character to string
    return encrypted_string , index_list                            #return encrypted string
    
                                                             
main()
