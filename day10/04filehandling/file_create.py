# f= open("filehandle.txt","x")   to create a file
f = open("filehandle.txt","w")
f.write("yeaaaa! it's just a demo file")
f.close()

# open the file after overwrite

f= open("filehandle.txt","r")

print(f.read())