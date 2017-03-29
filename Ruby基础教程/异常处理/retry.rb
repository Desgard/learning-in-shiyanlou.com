begin 
  file = open("/不存在的文件")
  if file 
    puts "File opened successfully"
  end
rescue
  fname = "./hello.txt"
  retry
end
