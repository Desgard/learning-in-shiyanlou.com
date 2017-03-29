
def test
    puts "You are in the method"
    yield                #执行代码块
    puts "You are again back to the method"
    yield                #执行代码块
end
test {puts "You are in the block"}
