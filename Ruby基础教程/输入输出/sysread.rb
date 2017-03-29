file_1 = File.open("secret.txt", "r")

words = file_1.sysread(20)
puts words

file_1.close
