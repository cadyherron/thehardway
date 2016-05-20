from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)  # moves to the first byte

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "Here's the whole file:\n"
print_all(current_file)

print "Rewind!"
rewind(current_file)

print "Print more stuff:\n"
print_a_line(1, current_file)
print_a_line(2, current_file)
