filename = "text.txt"


print "Opening the file..."
#target = open(filename, 'w')	# Overwrite
target = open(filename, 'a')	# append

print "Truncating the file.  Goodbye!"
target.truncate()

line1 = "Hello"
line2 = "mydear"
line3 = "how are you"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()