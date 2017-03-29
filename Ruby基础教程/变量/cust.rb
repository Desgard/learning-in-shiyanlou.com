class Customer
    def initialize(id, name, addr)
        @cust_id=id        #定义一个cust_id实例变量
        @cust_name=name
        @cust_addr=addr
    end
    def display_details()
        puts "Customer id #@cust_id"
        puts "Customer name #@cust_name"
        puts "Customer address #@cust_addr"
        #访问实例变量
    end
end

cust1=Customer.new("1", "John", "Wisdom Apartments, Ludhiya")
cust2=Customer.new("2", "Poul", "New Empire road, Khandala")
#创建两个对象
cust1.display_details()        #调用成员函数，成员函数调用实例变量
cust2.display_details()
