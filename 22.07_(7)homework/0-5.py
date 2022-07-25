#1 task
file = open("dog_breeds.txt", "r")

print(file.read())
file.close()

#2-3 task
file = open("dog_breeds.txt", "a")

file.write("\n" + "text")
file.close()

#4 task
file = open("dog_breeds.txt", "a")

args = input("Input some text:" )

file.write("\n" + args)
file.close()

#5 task
file_in = open("dog_breeds.txt", "r")
file_out = open("dog_.txt", "a")
file_out.write(file_in.read())
