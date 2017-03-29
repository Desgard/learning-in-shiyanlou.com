file_1 = File.open("secret.txt", "r")
file_1.syswrite("i am syswrite!")

file_1.close
