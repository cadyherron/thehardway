from sys import argv

script, filename = argv

print "Opening the file..."
target = open(filename, 'w')

print "Let's write to the file now..."
line = raw_input("Thing to write: ")
target.write(line)

print "And finally, we close it."
target.close()
