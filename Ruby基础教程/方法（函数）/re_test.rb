
def re_test
    i = 20
    j = 30
    k = i + j
    return k
end
re_var = re_test        #调用re_test方法，并将其返回值赋给var(局部变量，还记得起几种变量的定义方式了么？)
puts "return value: ",re_var
