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
    encrypt_lst = encrypt_file(initial_data, path)            
    print(f'_'*85)
    with open(path,'w') as write_file:
        for item in encrypt_lst:
            write_file.write(f"{item}")
    with open(path,'r') as write_file:
        out_put_data = write_file.read()
    print(out_put_data)                                                  
    print(f'_'*15,'END','_'*15) 
def encrypt_file(initial_data, path):
    def find_letter(list,letter):
        for i in range(len(list)):
            if letter == list[i]:
                index_letter = i
        return index_letter
    s1 = 14
    s2 = 14
    while not(s1 <= 12 and s2 <=12):
        s1 = int(input("Enter the first amount of alphabetical letter shifts for this encryption :"))
        if not(s1 <=12) or s1 < 0:
            print("Error - Out of shift range enter a number between 1 and 12")
        s2 = int(input("Enter the second amount of alphabetical letter shifts for this encryption :"))
        if not(s2 <=12) or s2 < 0:
            print("Error - Out of shift range, enter a number between 1 and 12")      
    enc_lower1 = [chr(i) for i in range(ord('a'), ord('m') + 1)]
    enc_lower2 = [chr(i2) for i2 in range(ord('A'), ord('M') + 1)]
    enc_upper1 = [chr(i3) for i3 in range(ord('n'), ord('z') + 1)]
    enc_upper2 = [chr(i4) for i4 in range(ord('N'), ord('Z') + 1)]
    
    encrypted_string = []
    for char in initial_data:
        if char.isalpha():
            if char in enc_lower1:
                index = find_letter(enc_lower1,char)                #encrypt lowercase a to n method
                if (index + (s1*s2)) >= 12:
                    new_char = "m"
                else:
                    new_char = enc_lower1[index + (s1 *s2)]
            if char in enc_lower2:
                index = find_letter(enc_lower2,char)                #encrypt uppercase A to N method
                                       
                if (index - (s1+s2)) < 0:
                    new_char = "A"
                else:
                    new_char = enc_lower2[index - (s1+s2)]
            if char in enc_upper1:   
                index = find_letter(enc_upper1,char)                #encrypt lowercase m to z method
                if (index -s1) <= 0:
                    new_char = "n"
                else:
                    new_char = enc_upper1[index-s1]            
            if char in enc_upper2:  
                index = find_letter(enc_upper2,char)                 #encrypt uppercase M to Z method
                if (index + (s2*s2)) >= 12:
                    new_char = "Z"
                else:
                    new_char = enc_upper2[index +(s2*s2)]  
              
        else:
            new_char = char
        encrypted_string.append(new_char)
    return encrypted_string 
main()
