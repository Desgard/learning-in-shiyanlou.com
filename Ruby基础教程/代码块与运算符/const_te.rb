CONST = ' out there'            #定义常量
class Inside_one
    CONST = proc {' in there'}
    def where_is_my_CONST
        ::CONST + ' inside one'    #引用常量
    end
end
class Inside_two
    CONST = ' inside two'
    def where_is_my_CONST
        CONST
    end
end
puts Inside_one.new.where_is_my_CONST
puts Inside_two.new.where_is_my_CONST
puts Object::CONST + Inside_two::CONST
puts Inside_two::CONST + CONST
puts Inside_one::CONST
puts Inside_one::CONST.call + Inside_two::CONST
