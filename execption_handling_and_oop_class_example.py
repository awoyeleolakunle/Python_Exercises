


try:
   file_ram = open("path", "w")

   file_ram.write("hello")

except IOError:
    print("files cannot write to a close file")
else:
    file_ram.close()
    print("successful")
