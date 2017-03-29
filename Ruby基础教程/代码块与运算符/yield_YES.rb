
def test
    yield 5            #执行代码块
    puts "You are in the method test"
    yield 100            #执行代码块
end
test {|i| puts "You are in the block #{i}"}
