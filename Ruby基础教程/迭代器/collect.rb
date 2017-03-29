shuzu = Array[1, 2, 3, 4]

shuzu_each = shuzu.each {|n| n = 2 * n}

shuzu_collect = shuzu.collect {|n| n = 2 * n}

puts "#{shuzu}"
puts "#{shuzu_each}"
puts "#{shuzu_collect}"
puts "#{shuzu}"

