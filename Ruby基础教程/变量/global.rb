$global_var = 10        #定义全局变量
class Class1
    def print_global
        puts "Global variable in Class1 is #$global_var."
        #通过在变量或常量的前面放置”#”，可以实现对任何变量或常量的访问
    end
end
class Class2
    def print_global
        puts "Global variable in Class2 is #$global_var."
    end
end

class1obj = Class1.new    #创建一个对象
class1obj.print_global    #对象调用成员函数，成员函数调用全局变量
class2obj = Class2.new
class2obj.print_global
