# Readlines() example
"""input_file = open("hello.txt", "w")

lines_to_write = [
    "This is line 1\n",
    "This is line 2\n",
    "This is line 2\n"
]
input_file.writelines(lines_to_write)
input_file.close()

output_file = open("hello.txt", "r")
read_data = output_file.readlines()

for line in read_data:
    print(line)

output_file.close()"""

# Readline() example
"""
input_file = open("hello.txt", "r")

file_input = input_file.readline()

while file_input != "":
    print(file_input)
    file_input = input_file.readline()

input_file.close()
"""

"""
with open("hello.txt", "r") as input_file, open("hello_out.txt", "w") as output_file:
    for line in input_file.readlines():
        output_file.write(line)
        print(line)
"""
"""
file_handle = open("poem.txt", "r")

output_file = file_handle.readline()

while output_file != "":
    print(output_file)
    output_file = file_handle.readline()

file_handle.close()
"""
"""
with open("poem.txt", "r") as file_handle, open("output.txt", "w") as output_handle:
    for line in file_handle.readlines():
        print(line)
        output_handle.write(line)
"""

file_handle = open("output.txt", "a")
file_handle.write("\nHello World")









