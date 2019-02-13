"""Lab 3: Regexes and reformatting."""

# Nicole Rasmussen

#######################################
# Instructions:
#
# The contact information below is not properly formatted.  Use regular expressions and Python code to reorganize the
# contact information into this format:
#
# Last name, First name, Middle Initial
# Location
# (xxx) xxx-xxxx
#
# Use regular expressions to decompose the data as much as possible and Python to reformat it.
#
# Print the reformatted information to show that it has been correctly reorganized.
#
# Extra Credit: Produce the reformatted contact info sorted programmatically by last name, ascending.
#
#######################################
import re

contacts = ["Kiayada D. Levy,(570)7924192,Sint-Laureins-Berchem",
            "Gretchen F. Manning,(1-656)-285-0869,Spoleto",
            "Ashton Richards,(974) 843-9297,Annapolis Royal",
            "Demetrius J. Ferguson,1-906-206-4323,Rea",
            "Blair Nelson,1-121-171-3665,Bertiolo",
            "Cynthia J. Farley,632 691 2180,Moen",
            "Nayda M. Lloyd,1-864-250-6977,Sarrev",
            "Miranda Edith Sexton,1-597-689-8316,Shipshaw",
            "Fulton Mays,(725)789-9517,Pierrefonds",
            "Shea Kim,1-697-854-4139,Bihain",
            "Emma-Mae Winters,1-137-630-5601,Gulfport",
            "Inez W. Depew,1-833-470-5664,Johnstone",
            "Darrel F. Key,1-878-918-2161,Olympia",
            "Tobias L. Stephens,1-119-939-6704,Unnao",
            "Elmo Pate,1-869-333-7341,Griesheim"]
name = ""
location = ""
phone_number = ""

print("*********************************")
for contact in contacts:
    
    ## Name
    name = contact.split(",")[0] # gets name on one line
    name = name.split(" ")
    if len(name) == 2:
        name = "Name: " + name[1] + ", " + name[0]
    else:
        name[1] = re.search(r"\w", name[1]).group() + "."
        name = "Name: " + name[2] + ", " + name[0] + ", " + name[1]
                       
        
    #Location  
    location = "Location: " + contact.split(",")[2]
    
    #Phone Number
    phone_number = contact.split(",")[1] # gets original phone number
    
    pattern = r"^\(1-|^1-\b"
    area_code = ""
    if re.search(pattern, phone_number):
        phone_number = re.sub("1-","", phone_number,1) # get rid of '1-'
    pattern = re.findall("\d{1}", phone_number)
    first_three = pattern[0] + pattern[1] + pattern[2]
    middle_three = pattern[3] + pattern[4] + pattern[5]
    last_digits = pattern[6] + pattern[7] + pattern[8] + pattern[9]
    phone_number = "Phone Number: (" + first_three  + ") " + middle_three + "-" + last_digits
    
    #Piece it together
    contact = name + "\n" + location + "\n" + phone_number
    print("Contact: \n" + contact)
    print("*********************************")
    
    
