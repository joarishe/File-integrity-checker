import hashlib
def integritycheck(filepath): #function to check the integrity of the file.
 file=open(filepath,"rb")
 originalhash=hashlib.file_digest(file,"sha256")
#need to save hash then compare later, maybe two different functions? or if statement, 
#if empty yeahhhhh then add if not compare
#

def filecheck (filepath): #function to check if filepath exists in hashcheck file.
 Flag=False
 with open("hashcheck.txt","r") as h: #variable stuff
  while not Flag:
   data=h.readline()
   if data!=(""):
    temppath=data.split(",")[0]
    if temppath==filepath:
     Flag=True
     break
   else:
    break
 return Flag
#this function checks whether the filepath exists in the baseline file "hashcheck" and returns true or false.
  
 
 


#okay the plan is: i need a file to check the hash
#i need to check if the file that the user has inputted already exists in the hashcheck file
#if it doesn't function to add that file
#if it does function to check the hash of that file and compare it
#then later extra stuff