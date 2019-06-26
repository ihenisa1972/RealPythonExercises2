input_file = open("hello.txt", "w")

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

output_file.close()



