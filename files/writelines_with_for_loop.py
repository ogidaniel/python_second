# This program uses the writelines method to save
 # a list of strings to a file.

def main():

    #creating lists of strings
    cities = ['geogia', 'oklahoma', 'york', 'new jersey']

    #open a file for writing

    output_file = open('cities.txt','w')

    for i in cities:
        # Write the list to the file.
        output_file.write(i + '\n')
    
    # Close the file.
    output_file.close()
    

#closing mainn function
main()