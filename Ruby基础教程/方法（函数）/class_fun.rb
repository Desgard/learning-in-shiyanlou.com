class Class_fun            #创建一个Class_fun类
    def fun1
        puts "This is the first test for class."
    end
    def fun2
        puts "This is the second test for class."
    end                #类中包括两个成员函数
end
test1=Class_fun.new
test2=Class_fun.new    #创建类Class_fun的两个对象
test1.fun1            #对象调用类的成员函数
test2.fun2
